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
    "httpMethod": "POST",
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
        "Host": "np0ky4itde.execute-api.us-east-1.amazonaws.com",
        "Postman-Token": "40a106a7-9df6-4db3-a44b-9d7494ec75a8",
        "User-Agent": "PostmanRuntime/7.37.3",
        "Via": "1.1 7c589e121113e58fcd11b4511aa7aa76.cloudfront.net (CloudFront)",
        "X-Amz-Cf-Id": "sdEGcH-QwLSKpDc2HoD75iNhelwsi1AGdLanzgKrrY9VbpsklDb72g==",
        "X-Amzn-Trace-Id": "Root=1-6679368c-262a8f6d238898ce428dbe80",
        "X-Forwarded-For": "165.85.220.37, 15.158.31.229",
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
        "Host": ["np0ky4itde.execute-api.us-east-1.amazonaws.com"],
        "Postman-Token": ["40a106a7-9df6-4db3-a44b-9d7494ec75a8"],
        "User-Agent": ["PostmanRuntime/7.37.3"],
        "Via": ["1.1 7c589e121113e58fcd11b4511aa7aa76.cloudfront.net (CloudFront)"],
        "X-Amz-Cf-Id": ["sdEGcH-QwLSKpDc2HoD75iNhelwsi1AGdLanzgKrrY9VbpsklDb72g=="],
        "X-Amzn-Trace-Id": ["Root=1-6679368c-262a8f6d238898ce428dbe80"],
        "X-Forwarded-For": ["165.85.220.37, 15.158.31.229"],
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
        "resourceId": "sxiff4",
        "resourcePath": "/catalog",
        "httpMethod": "POST",
        "extendedRequestId": "Z3V2CFPJIAMEslA=",
        "requestTime": "24/Jun/2024:09:04:12 +0000",
        "path": "/dev/catalog",
        "accountId": "051556718043",
        "protocol": "HTTP/1.1",
        "stage": "dev",
        "domainPrefix": "np0ky4itde",
        "requestTimeEpoch": 1719219852793,
        "requestId": "9cb65374-2471-42f5-a48a-7ad06d66d972",
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
        "domainName": "np0ky4itde.execute-api.us-east-1.amazonaws.com",
        "deploymentId": "016ir0",
        "apiId": "np0ky4itde",
    },
    "body": None,
    "isBase64Encoded": False,
}


print(lambda_handler(event, context))
