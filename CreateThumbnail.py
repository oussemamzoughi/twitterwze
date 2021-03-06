from __future__ import print_function
import boto3
import time
import json
import decimal
kinesis = boto3.client("kinesis")
shard_id = 'shardId-000000000000' #only one shard
shard_it = kinesis.get_shard_iterator(StreamName="twitter", ShardId=shard_id, ShardIteratorType="LATEST")["ShardIterator"]

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('full_name')

     
def handler(event, context):
    while 1==1:
	    out = kinesis.get_records(ShardIterator=shard_it, Limit=100)
	    for record in out['Records']:
		    if 'place' in json.loads(record['Data'].decode('utf-8')):
			    fnames = json.loads(record['Data'].decode('utf-8'))['place']['full_name']
			    if fnames:
 				
					      checkItemExists = table.get_item(
 					           Key={
                					'full_name':fnames
        					    }
					      )					
					      if 'Item' in checkItemExists:
						        response = table.update_item(
							Key={
								'full_name': fnames 
							},
							UpdateExpression="set ftCount  = ftCount + :val",
							ConditionExpression="attribute_exists(full_name)",
							ExpressionAttributeValues={
								':val': decimal.Decimal(1) 	
							},
							ReturnValues="UPDATED_NEW"
						)
					      else: 
                                		response = table.update_item(
                                        		Key={
                                                		'full_name': fnames
                                        		},
                                        		UpdateExpression="set ftCount = :val",
                                        		ExpressionAttributeValues={
                                                		':val': decimal.Decimal(1)
                                        		},
                                        		ReturnValues="UPDATED_NEW"
                                		)    
	    shard_it = out["NextShardIterator"]
	    time.sleep(1.0)