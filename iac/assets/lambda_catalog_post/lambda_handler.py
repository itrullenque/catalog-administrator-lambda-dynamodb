import boto3
import json
import time
from io import BytesIO
from aws import DynamoDb

TABLE_NAME = "catalog"
resource_dynamo_db = DynamoDb.resource_custom()


def lambda_handler(event, context):

    try:
        print(f"Received event: {event}")
        query_params = event.get("queryStringParameters", {})

        # validation
        if set(query_params.keys()) != {"catalog_id", "course_id"}:
            return {
                "statusCode": 400,
                "body": json.dumps(
                    "Error: Error, input parameters are missing or incorrect."
                ),
            }

        catalog_id = query_params.get("catalog_id")
        course_id = query_params.get("course_id")
        # set the academic year
        academic_year = int(time.strftime("%Y"))

        # create the body
        catalog_item = {
            "catalog_id": catalog_id.lower(),
            "course_id": course_id.lower(),
            "creation_date": int(time.time()),
            "academic_year": academic_year,
        }

        # save in dynamo
        dynamo_response = DynamoDb.object_post(
            TABLE_NAME, catalog_item, resource_dynamo_db
        )

        if dynamo_response["code"] == "NOK":
            return {
                "statusCode": 500,
                "body": json.dumps(f"Error: {dynamo_response['error_technical']}"),
            }

        if dynamo_response["code"] == "CEX":
            return {
                "statusCode": 400,
                "body": json.dumps(f"Error: {dynamo_response['error_technical']}"),
            }

        return {
            "statusCode": 200,
            "body": json.dumps("Catalog item created successfully"),
        }
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps(f"Error: {str(e)}")}
