import json
import os
import uuid
from datetime import datetime

import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    print(event)
    data = json.loads(event['body'])
    print(json.dumps(data))

    try:

        content = 'Message from ' + \
            data['name'] + ' ' + data['last_name'] + '\n' + \
            data['age'] + '\n' + \
            data['birthday'] + '\n' + \
            data['job_title'] + '\n' + \
            data['employer'] + '\n' + \
            data['city'] + '\n' + \
            data['email'] + '\n' + \
            data['phone_number'] + '\n' + \
            data['profile_picture']
        save_to_dynamodb(data)

    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Successful", response)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": ""
    }


def save_to_dynamodb(data):
    timestamp = datetime.utcnow().replace(microsecond=0).isoformat()
    table = dynamodb.Table(DYNAMODB_TABLE)
    item = {
        'ID': str(uuid.uuid1()),
        'name': data['name'],  # required
        'age': data['age'],  # required
        'birthday': data['birthday'],  # required
        'job_title': data['job_title'],  # required
        'employer': data['employer'],  # required
        'city': data['city'],  # required
        'email': data['email'],  # required
        'phone_number': data['phone_number'],  # required
        'profile_picture': data['profile_picture'],  # required
        'createdAt': timestamp,
        'updatedAt': timestamp
    }
    table.put_item(Item=item)
    return
