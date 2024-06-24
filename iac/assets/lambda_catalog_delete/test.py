# IMPORTA LIBRERIAS PYTHON
import json
import os

# IMPORTA LAMBDA HANLDER
from lambda_handler import lambda_handler


# GENERA CONTEXTO
class Context:
    invoked_function_arn = (
        "arn:aws:lambda:us-east-1:051556718043:function:lambda_summarize_transcript"
    )
    function_name = "lambda_catalog_delete"


context = Context()

event = {
    "resource": "/catalog",
    "path": "/catalog",
    "httpMethod": "DELETE",
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "CloudFront-Forwarded-Proto": "https",
        "CloudFront-Is-Desktop-Viewer": "true",
        "CloudFront-Is-Mobile-Viewer": "false",
        "CloudFront-Is-SmartTV-Viewer": "false",
        "CloudFront-Is-Tablet-Viewer": "false",
        "CloudFront-Viewer-ASN": "396982",
        "CloudFront-Viewer-Country": "ES",
        "Host": "x40esp0c99.execute-api.us-east-1.amazonaws.com",
        "Postman-Token": "6f1fea88-5b64-4186-9085-8399a0b5a1ab",
        "User-Agent": "PostmanRuntime/7.37.3",
        "Via": "1.1 95e221714a9b947612e0fb1cc46fd974.cloudfront.net (CloudFront)",
        "X-Amz-Cf-Id": "lvOjdYWfp5JVrgHJVM3QviYIz22WOqos8nJWTT-TBx6wWcICN18jRQ==",
        "X-Amzn-Trace-Id": "Root=1-667991d0-703931770be520ed4845c762",
        "X-Forwarded-For": "165.85.220.37, 15.158.31.14",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Proto": "https",
    },
    "multiValueHeaders": {
        "Accept": ["*/*"],
        "Accept-Encoding": ["gzip, deflate, br"],
        "CloudFront-Forwarded-Proto": ["https"],
        "CloudFront-Is-Desktop-Viewer": ["true"],
        "CloudFront-Is-Mobile-Viewer": ["false"],
        "CloudFront-Is-SmartTV-Viewer": ["false"],
        "CloudFront-Is-Tablet-Viewer": ["false"],
        "CloudFront-Viewer-ASN": ["396982"],
        "CloudFront-Viewer-Country": ["ES"],
        "Host": ["x40esp0c99.execute-api.us-east-1.amazonaws.com"],
        "Postman-Token": ["6f1fea88-5b64-4186-9085-8399a0b5a1ab"],
        "User-Agent": ["PostmanRuntime/7.37.3"],
        "Via": ["1.1 95e221714a9b947612e0fb1cc46fd974.cloudfront.net (CloudFront)"],
        "X-Amz-Cf-Id": ["lvOjdYWfp5JVrgHJVM3QviYIz22WOqos8nJWTT-TBx6wWcICN18jRQ=="],
        "X-Amzn-Trace-Id": ["Root=1-667991d0-703931770be520ed4845c762"],
        "X-Forwarded-For": ["165.85.220.37, 15.158.31.14"],
        "X-Forwarded-Port": ["443"],
        "X-Forwarded-Proto": ["https"],
    },
    "queryStringParameters": {"catalog_id": "deck_1", "course_id": "aws_course"},
    "multiValueQueryStringParameters": {
        "catalog_id": ["deck_1"],
        "course_id": ["aws_course"],
    },
    "pathParameters": None,
    "stageVariables": None,
    "requestContext": {
        "resourceId": "sing8j",
        "resourcePath": "/catalog",
        "httpMethod": "DELETE",
        "extendedRequestId": "Z4O4lFTKIAMEcig=",
        "requestTime": "24/Jun/2024:15:33:36 +0000",
        "path": "/dev/catalog",
        "accountId": "051556718043",
        "protocol": "HTTP/1.1",
        "stage": "dev",
        "domainPrefix": "x40esp0c99",
        "requestTimeEpoch": 1719243216283,
        "requestId": "3f07a741-ae22-4708-84cd-4dbe748ec057",
        "identity": {
            "cognitoIdentityPoolId": None,
            "accountId": None,
            "cognitoIdentityId": None,
            "caller": None,
            "sourceIp": "165.85.220.37",
            "principalOrgId": None,
            "accessKey": None,
            "cognitoAuthenticationType": None,
            "cognitoAuthenticationProvider": None,
            "userArn": None,
            "userAgent": "PostmanRuntime/7.37.3",
            "user": None,
        },
        "domainName": "x40esp0c99.execute-api.us-east-1.amazonaws.com",
        "deploymentId": "3ye4xa",
        "apiId": "x40esp0c99",
    },
    "body": None,
    "isBase64Encoded": False,
}


print(lambda_handler(event, context))
