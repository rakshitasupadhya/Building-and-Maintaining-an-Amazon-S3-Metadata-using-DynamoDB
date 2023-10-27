import boto3
from uuid import uuid4

def lambda_handler(event, context):
    s3 = boto3.client ("s3")
    dynamodb = boto3.resource('dynamodb')
    for record in event['Records']:
        bucketname= record['s3']['bucket']['name']
        object_key= record['s3']['object']['key']
        size = record['s3']['object'].get('size', -1)
        event_name = record ['eventName']
        event_time= record['eventTime']
        dynamoTable = dynamodb.Table('storemetadata')
        dynamoTable.put_item(
                  Item={'RequestId': str(uuid4()), 'Bucket':bucketname, 'Object': object_key, 'Size': size, 'Event':event_name, 'EventTime':event_time })
