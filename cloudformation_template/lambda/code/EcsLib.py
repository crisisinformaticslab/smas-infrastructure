import random
import DynamoLib as dl
import EnvironProxy as ep
import boto3
import SecretsProxy as sp
import os

ecs = boto3.client('ecs')

secrets = sp.get_dependencies()

ec2 = boto3.resource('ec2')
vpc = ec2.Vpc(secrets['VPC_ID'])

security_group = os.environ['securityGroup']


def start_task(term):

    subnets = [s.id for s in vpc.subnets.all()]

    response = ecs.run_task(
        cluster=secrets['CLUSTER_NAME'],
        taskDefinition=secrets['TASK_DEFINITION'],
        count=1,
        launchType='FARGATE',
        overrides={

            'containerOverrides': [
                {
                    'name': secrets['CONTAINER_NAME'],
                    'environment': [
                        {
                            'name': 'TERM',
                            'value': term
                        }
                    ]
                }
            ]
        },
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': subnets,
                'assignPublicIp': 'ENABLED',
                'securityGroups': [security_group]
            }
        }
    )

    print response
    arns = [t['taskArn'] for t in response['tasks']]

    if len(arns) == 1:

        dl.put_task(arns[0], term)
        return {'task_arn': arns[0], 'term': term}

    else:
        print response


def end_task(arn):
    response = ecs.stop_task(
        cluster=secrets['CLUSTER_NAME'],
        task=arn
    )
    dl.put_task_termination(arn)
    pass


def sync_tasks(active_tasks):
    running_tasks = ecs.list_tasks(
        cluster=secrets['CLUSTER_NAME']
    )

    running_arns = running_tasks['taskArns']

    active_arns = [t['task_arn'] for t in active_tasks]

    for arn in running_arns:
        if arn not in active_arns:
            end_task(arn)

    for arn in active_arns:
        if arn not in running_arns:
            dl.put_task_termination(arn)
