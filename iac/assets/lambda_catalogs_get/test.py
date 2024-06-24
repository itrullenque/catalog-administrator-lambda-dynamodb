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
    "resource": "/catalogs",
    "path": "/catalogs",
    "httpMethod": "GET",
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
        "Postman-Token": "48ff70ab-9054-4878-8f30-36041193fae7",
        "User-Agent": "PostmanRuntime/7.37.3",
        "Via": "1.1 3afa128985f4497e8a212c0a2b56730a.cloudfront.net (CloudFront)",
        "X-Amz-Cf-Id": "OeClzqLinIEBXO6skmRVjT_lcRHgrnoLiapF8QXO1v899NMFzYUJMg==",
        "X-Amzn-Trace-Id": "Root=1-6679b9d1-6d0f45694268fb07517cabca",
        "X-Forwarded-For": "88.1.30.71, 15.158.31.21",
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
        "Postman-Token": ["48ff70ab-9054-4878-8f30-36041193fae7"],
        "User-Agent": ["PostmanRuntime/7.37.3"],
        "Via": ["1.1 3afa128985f4497e8a212c0a2b56730a.cloudfront.net (CloudFront)"],
        "X-Amz-Cf-Id": ["OeClzqLinIEBXO6skmRVjT_lcRHgrnoLiapF8QXO1v899NMFzYUJMg=="],
        "X-Amzn-Trace-Id": ["Root=1-6679b9d1-6d0f45694268fb07517cabca"],
        "X-Forwarded-For": ["88.1.30.71, 15.158.31.21"],
        "X-Forwarded-Port": ["443"],
        "X-Forwarded-Proto": ["https"],
    },
    "queryStringParameters": None,
    "multiValueQueryStringParameters": None,
    "pathParameters": None,
    "stageVariables": None,
    "requestContext": {
        "resourceId": "e3gi2g",
        "resourcePath": "/catalogs",
        "httpMethod": "GET",
        "extendedRequestId": "Z4n4yGsRoAMEPEA=",
        "requestTime": "24/Jun/2024:18:24:17 +0000",
        "path": "/dev/catalogs",
        "accountId": "051556718043",
        "protocol": "HTTP/1.1",
        "stage": "dev",
        "domainPrefix": "x40esp0c99",
        "requestTimeEpoch": 1719253457580,
        "requestId": "140493e4-1907-4a2a-8055-708a18896023",
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
        "deploymentId": "i9rp2x",
        "apiId": "x40esp0c99",
    },
    "body": None,
    "isBase64Encoded": False,
}


print(lambda_handler(event, context))
