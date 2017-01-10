import boto3

client = boto3.client('kinesis')
response = client.create_stream(StreamName = 'naoufel',
ShardCount=1)
