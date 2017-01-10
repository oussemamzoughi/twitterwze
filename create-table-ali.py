## create a table to store twitter hashtags in DynamoDB
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.create_table(
    TableName='Ali',
    KeySchema=[
        {
            'AttributeName': 'Ali',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Ali',
            'AttributeType': 'S'
        }
    ],
    # pricing determined by ProvisionedThroughput
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
table.meta.client.get_waiter('table_exists').wait(TableName='Ali')