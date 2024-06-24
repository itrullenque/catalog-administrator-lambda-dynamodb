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
    function_name = "lambda_catalog_post"


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
        "CloudFront-Viewer-ASN": "3352",
        "CloudFront-Viewer-Country": "ES",
        "Host": "x40esp0c99.execute-api.us-east-1.amazonaws.com",
        "Postman-Token": "b3c44682-6263-460c-b7b2-4a8821be670f",
        "User-Agent": "PostmanRuntime/7.37.3",
        "Via": "1.1 62db9fb3b90983f59ae41bc4d453e556.cloudfront.net (CloudFront)",
        "X-Amz-Cf-Id": "mWSHADsAVjvpqDin-NR0JnMqX21f4EwM-_jb_d4VomiVLk61LIot4A==",
        "X-Amzn-Trace-Id": "Root=1-66798bf2-60de447224da8b630b767212",
        "X-Forwarded-For": "88.1.30.71, 15.158.31.9",
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
        "CloudFront-Viewer-ASN": ["3352"],
        "CloudFront-Viewer-Country": ["ES"],
        "Host": ["x40esp0c99.execute-api.us-east-1.amazonaws.com"],
        "Postman-Token": ["b3c44682-6263-460c-b7b2-4a8821be670f"],
        "User-Agent": ["PostmanRuntime/7.37.3"],
        "Via": ["1.1 62db9fb3b90983f59ae41bc4d453e556.cloudfront.net (CloudFront)"],
        "X-Amz-Cf-Id": ["mWSHADsAVjvpqDin-NR0JnMqX21f4EwM-_jb_d4VomiVLk61LIot4A=="],
        "X-Amzn-Trace-Id": ["Root=1-66798bf2-60de447224da8b630b767212"],
        "X-Forwarded-For": ["88.1.30.71, 15.158.31.9"],
        "X-Forwarded-Port": ["443"],
        "X-Forwarded-Proto": ["https"],
    },
    "queryStringParameters": {"catalog_id": "deck_1", "course_id": "aws_course"},
    "multiValueQueryStringParameters": {
        "catalog_id": ["deck_2"],
        "course_id": ["aws_course"],
    },
    "pathParameters": None,
    "stageVariables": None,
    "requestContext": {
        "resourceId": "sing8j",
        "resourcePath": "/catalog",
        "httpMethod": "DELETE",
        "extendedRequestId": "Z4LN7FYNIAMEUUA=",
        "requestTime": "24/Jun/2024:15:08:34 +0000",
        "path": "/dev/catalog",
        "accountId": "051556718043",
        "protocol": "HTTP/1.1",
        "stage": "dev",
        "domainPrefix": "x40esp0c99",
        "requestTimeEpoch": 1719241714442,
        "requestId": "d0337aed-e66f-4958-8b0d-c5fd761cfbb8",
        "identity": {
            "cognitoIdentityPoolId": None,
            "accountId": None,
            "cognitoIdentityId": None,
            "caller": None,
            "sourceIp": "88.1.30.71",
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
