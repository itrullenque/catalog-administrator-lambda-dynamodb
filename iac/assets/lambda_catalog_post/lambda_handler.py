import boto3
import json
import time
from io import BytesIO
from aws import DynamoDb

TABLE_NAME = "catalog"
resource_dynamo_db = DynamoDb.resource_custom()


def lambda_handler(event, context):

    try:
        catalog_id = event["catalog_id"]
        course_id = event["course_id"]

        # create the body
        catalog_item = {
            "catalog_id": catalog_id,
            "course_id": course_id,
            "creation_date": int(time.time()),
        }

        # save in dynamo
        dynamo_response = DynamoDb.object_post(
            resource_dynamo_db, TABLE_NAME, catalog_item
        )

        return {
            "statusCode": 200,
            "body": json.dumps("Catalog item created successfully"),
        }
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps(f"Error: {str(e)}")}
