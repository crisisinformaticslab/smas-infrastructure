import boto3

from botocore.exceptions import ClientError

my_stream_name = 'twitter-ingest'
kinesis_client = boto3.client('kinesis')

def put_records(records):
    if len(records) == 0:
        return {}

    try:
        resp = kinesis_client.put_records(
            Records=records,
            StreamName=my_stream_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)

        return {}
    else:
        return resp