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
    def object_query_index(table_name, key_condition, index_name, resource):

        try:
            response = {}
            table = resource.Table(table_name)
            response = table.query(
                IndexName=index_name, KeyConditionExpression=key_condition
            )

            if "Items" not in response or len(response["Items"]) < 1:
                response["code"] = "NOT_FOUND"
                response["error_technical"] = "Items not found"
                return response

            if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                response["Items"] = json.loads(
                    json.dumps(response["Items"], indent=4, cls=DecimalEncoder)
                )
                response["code"] = "OK"
                return response

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            err = "file: {} - line:{} - Error: {} - {}".format(
                fname, exc_tb.tb_lineno, exc_obj, exc_type
            )

            response["code"] = "NOK"
            response["error_technical"] = err
            return response


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)
