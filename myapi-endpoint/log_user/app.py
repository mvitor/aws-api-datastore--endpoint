import json
from pathlib import Path
from schema import * 
import pydantic
import boto3
import os 

def lambda_handler(event, context):
    
    try:
        parsed_user = User(**event["queryStringParameters"])
    except pydantic.ValidationError as ex:
        # log exception
        raise
    environment = os.environ['ENVIRONMENT']
    dynamodb_dev_uri = os.environ['DYNAMODBDEVURI']
    # Choose database connection depending on Dev or Prod environment
    if environment == "AWS_SAM_LOCAL":
        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_dev_uri)
    else:
        dynamodb = boto3.resource('dynamodb')
    # Execute create query on DynamoDB table 
    table = dynamodb.Table('LogUser')
    added_item = table.put_item(
        Item={
            "PK": parsed_user.uid,
            "SK": parsed_user.name
        }
    )
    if added_item['ResponseMetadata']['HTTPStatusCode'] == 200:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "id": parsed_user.id,
                "signup_ts": parsed_user.name
            }),
        }
    else: 
        return {
            "statusCode": 500,
            "body": json.dumps({
                "id": parsed_user.id,
                "signup_ts": parsed_user.name
            }),
        }
