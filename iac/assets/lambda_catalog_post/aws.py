import decimal
import json
import os
import sys

import boto3
from boto3.dynamodb.conditions import Attr, Key
from botocore.config import Config
from botocore.exceptions import ClientError, ParamValidationError


class DynamoDb:

    @staticmethod
    def resource_custom():
        my_config = Config(region_name="us-east-1", connect_timeout=3, read_timeout=3)
        resource = boto3.resource("dynamodb", config=my_config)
        return resource

    @staticmethod
    def object_post(table_name, object, resource):

        try:
            table = resource.Table(table_name)
            response = {}

            # Check if the item already exists
            condition_expression = (
                Attr("catalog_id").not_exists() & Attr("course_id").not_exists()
            )

            response = table.put_item(
                Item=object,
                ConditionExpression=condition_expression,
                ReturnValues="NONE",
            )

            response["code"] = "OK"
            return response

        except ClientError as e:
            if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
                return {"code": "CEX", "error_technical": "Item already exists"}
            else:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                err = "file: {} - line:{} - error: {} - {}".format(
                    fname, exc_tb.tb_lineno, str(e), exc_type
                )
                return {"code": "NOK", "error_technical": err}

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            err = "file: {} - line:{} - error: {} - {}".format(
                fname, exc_tb.tb_lineno, str(e), exc_type
            )
            return {"code": "NOK", "error_technical": err}
