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
        if query_params is not None:
            return {
                "statusCode": 400,
                "body": json.dumps("Error: Error, input parameters are not supported."),
            }

        # scan in dynamo
        dynamo_response = DynamoDb.object_scan(TABLE_NAME, resource_dynamo_db)

        if dynamo_response["code"] == "OK":
            return {"statusCode": 200, "body": json.dumps(dynamo_response["item"])}

        if dynamo_response["code"] == "NOK":
            return {
                "statusCode": 500,
                "body": json.dumps(f"Error: {dynamo_response['error_technical']}"),
            }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"An unexpected error occurred: {str(e)}"}),
        }
