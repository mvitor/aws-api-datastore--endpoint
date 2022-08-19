import json
from pathlib import Path
from user_log.schema import *
import pydantic
import boto3
import os


def lambda_handler(event, context):

    environment = os.environ["ENVIRONMENT"]
    dynamodb_dev_uri = os.environ["DYNAMODBDEVURI"]

    try:
        parsed_user = User(**event["queryStringParameters"])
    except pydantic.ValidationError as ex:
        raise Exception("Failed to validate API Payload")

    # Use Docker database connection or any connection string for Dev environment
    if environment == "AWS_SAM_LOCAL":
        dynamodb = boto3.resource("dynamodb", endpoint_url=dynamodb_dev_uri)
    else:
        dynamodb = boto3.resource("dynamodb")

    # Execute create query on DynamoDB table
    table = dynamodb.Table("UserLog")
    updated_on = datetime.utcnow().isoformat()

    added_item = table.put_item(
        Item={
            "PK": parsed_user.uid,
            "SK": parsed_user.name,
            "loguserId": parsed_user.id,
            "updatedOn": updated_on,
        }
    )
    if added_item["ResponseMetadata"]["HTTPStatusCode"] == 200:
        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "uid": parsed_user.uid,
                    "name": parsed_user.name,
                    "updatedOn": updated_on,
                    "status": "Success",
                    "message": "User log entry created successfully",
                }
            ),
        }
    else:
        return {
            "statusCode": 500,
            "body": json.dumps(
                {
                    "uid": parsed_user.uid,
                    "name": parsed_user.name,
                    "updatedOn": updated_on,
                    "status": "Failure",
                    "message": "User log entry not created",
                }
            ),
        }
