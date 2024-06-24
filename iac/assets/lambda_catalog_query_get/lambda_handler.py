import boto3
import json
from aws import DynamoDb
from boto3.dynamodb.conditions import Key

TABLE_NAME = "catalog"
resource_dynamo_db = DynamoDb.resource_custom()


def lambda_handler(event, context):

    try:
        print(f"Received event: {event}")

        query_params = event.get("queryStringParameters", {})
        if not query_params:
            return {
                "statusCode": 400,
                "body": json.dumps(
                    {
                        "error": "No query parameters provided. Please include either 'academic_year' or 'course_id'."
                    }
                ),
            }

        if "academic_year" in query_params and "course_id" in query_params:
            return {
                "statusCode": 400,
                "body": json.dumps(
                    {
                        "error": "Invalid query. Please provide either 'academic_year' or 'course_id', not both."
                    }
                ),
            }

        if "academic_year" in query_params:
            index = "academic_year-index"
            key_condition = Key("academic_year").eq(int(query_params["academic_year"]))
        elif "course_id" in query_params:
            index = "course_id-index"
            key_condition = Key("course_id").eq(query_params["course_id"])
        else:
            return {
                "statusCode": 400,
                "body": json.dumps(
                    {
                        "error": "Invalid query parameters. Please provide 'academic_year' or 'course_id'."
                    }
                ),
            }

        # query index in dynamo
        dynamo_response = DynamoDb.object_query_index(
            TABLE_NAME, key_condition, index, resource_dynamo_db
        )

        if dynamo_response["code"] == "OK":
            return {"statusCode": 200, "body": json.dumps(dynamo_response["Items"])}

        if dynamo_response["code"] == "NOK":
            return {
                "statusCode": 500,
                "body": json.dumps(f"Error: {dynamo_response['error_technical']}"),
            }

        if dynamo_response["code"] == "NOT_FOUND":
            return {
                "statusCode": 400,
                "body": json.dumps(f"Error: {dynamo_response['error_technical']}"),
            }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"An unexpected error occurred: {str(e)}"}),
        }
