# Use this code snippet in your app.
import boto3
from botocore.exceptions import ClientError

import SecretLib as sl
import EnvironProxy as ep


twitter_search_terms = ep.get_env('SECRETS_PATH')

def get_search_terms():
    secrets = sl.get_secret(twitter_search_terms)
    terms = secrets['TERMS'].split(';')
    return terms

def get_dependencies(key=None):
    dependencies_key = ep.get_env('DEPENDENCIES')
    secrets = sl.get_secret(dependencies_key)
    if key is None or key not in secrets:
        return secrets
    else:
        return secrets[key]