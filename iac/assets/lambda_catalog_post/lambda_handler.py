def lambda_handler(event, context):
    # Process the event here
    print("Event received:", event)

    # Return a response
    return {"statusCode": 200, "body": "Hello from Lambda!"}
