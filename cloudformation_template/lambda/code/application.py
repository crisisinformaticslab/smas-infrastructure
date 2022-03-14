# -*- coding: utf-8 -*-

import time
import json
import boto3
from botocore.exceptions import ClientError

import SecretsProxy as sp
import EnvironProxy as ep
import KinesisLib as kl
import DynamoLib as dl
import EcsLib as el
from TermKeeper import TermKeeper
import CloudWatchLib as cwl

cloudwatch = boto3.client('cloudwatch')


def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None


def safe_get(ob, key):
    if key in ob:
        return ob[key]
    else:
        return None


def put_metrics(term):
    resp = cloudwatch.put_metric_data(
        Namespace='twitter-ingestion-orchestrator',
        MetricData=[
            {
                'MetricName': 'IngestionCount',
                'Dimensions': [
                    {
                        'Name': 'term',
                        'Value': term
                    }
                ],
                'Value': 1
            }
        ]
    )


def lambda_handler(event, context):
    kpr = TermKeeper()

    active_tasks = dl.get_active_tasks()
    print(active_tasks)
    active_terms = [task['term'] for task in active_tasks]
    print 'starting active terms: ', active_terms

    el.sync_tasks(active_tasks)

    target_terms = kpr.get_search_terms()
    print 'target_terms: ', target_terms

    # Populate list of removed terms
    removed_terms = []

    for task in active_tasks:
        task_term = task['term']
        if task_term in target_terms:
            print task_term, ' retained'
            target_terms.remove(task_term)
        else:
            el.end_task(task['task_arn'])
            removed_list.append(task)
            active_tasks.remove(task)
            print task_term, ' removed'

    # Remove cloudwatch alarms
    cwl.delete_alarms(removed_terms)

    print 'terms to add:', target_terms
    for tt in target_terms:
        if len(tt) > 0:
            print tt, ' added'
            task = el.start_task(tt)
            cwl.create_alarm(tt)
            active_tasks.append(task)
    print 'ending active terms', [task['term'] for task in active_tasks]
    print('Putting metrics')
    [put_metrics(t['term']) for t in active_tasks]
    print('Done')
    return


if __name__ == "__main__":
    lambda_handler(None, None)
