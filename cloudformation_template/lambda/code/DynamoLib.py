import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr
import EnvironProxy as ep
import time

import SecretsProxy as sp

table_name = sp.get_dependencies('TRACK_TABLE')
dynamo = boto3.resource('dynamodb')
table = dynamo.Table(table_name)


def put_task(task_arn, term):

    try:
        resp = table.put_item(

            Item={
                'task_arn': task_arn,
                'term': term,
                'task_status': 'ACTIVE',
                'start_time': int(time.time())
            }
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)

        return {'ERROR': e}
    else:
        return resp


def put_task_termination(task_arn):
    try:
        resp = table.update_item(
            Key={
                'task_arn': task_arn
            },

            UpdateExpression="SET task_status = :stat, termination_time = :ti",
            ExpressionAttributeValues={
                ':stat': 'TERMINATED',
                ':ti': int(time.time())
            }
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)

        return {'ERROR': e}
    else:
        return resp


def get_active_tasks():
    print(table_name)
    try:
        resp = table.scan(
            Select='ALL_ATTRIBUTES',
            FilterExpression=Attr('task_status').eq('ACTIVE')
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)

        return {'ERROR': e}
    else:
        return [{'task_arn': t['task_arn'], 'term': t['term']} for t in resp['Items']]
