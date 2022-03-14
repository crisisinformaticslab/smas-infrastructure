# Use this code snippet in your app.
import boto3
from botocore.exceptions import ClientError
import json

# import os
# os.environ["AWS_PROFILE"] = "smas"


def get_secret(secret_name):
    # secret_name = "prod/twitter"
    region_name = "us-west-2"

    session = boto3.session.Session()
    client = session.client(
        service_name='ssm',
        region_name=region_name)

    try:
        get_secret_value_response = client.get_parameter(Name=secret_name, WithDecryption=True)

    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print "The requested secret " + secret_name + " was not found"
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print "The request was invalid due to:", e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print "The request had invalid params:", e

        return {"error": e}
    else:
        get_secret_value_response = get_secret_value_response["Parameter"]
        if 'Value' in get_secret_value_response:
            secret = get_secret_value_response['Value']
            return json.loads(secret)
        else:
            print "No Value found in Param"
