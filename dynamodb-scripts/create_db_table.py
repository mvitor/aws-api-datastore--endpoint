import boto3
import sys

def create_log_users_local(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    table = dynamodb.Table('LogUser')
    table.delete()
    pass
    table = dynamodb.create_table(
        TableName='LogUser',
        KeySchema=[
            {
                'AttributeName': 'PK', 
                'KeyType': 'HASH' 
            },
            {
                'AttributeName': 'SK', 
                'KeyType': 'RANGE'  
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'PK',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'SK',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table

# The main method.
if __name__ == '__main__':

    # Create the dynamodb object
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = create_log_users_local(dynamodb)
    print("Table status:", table.table_status)