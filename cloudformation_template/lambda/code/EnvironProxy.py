import os

defaults = {
    'TASK_DEFINITION': "arn:aws:ecs:us-east-1:653877814600:task-definition/test:6",
    'TRACKER_TABLE': 'twitter-ingest-orchestrator',
    'TERM_CHECK_DURATION': '5',
    'SECRETS_PATH': '/prod/twitter/terms',
    'CLUSTER_NAME': 'twitter-ingest-cluster',
    'DEPENDENCIES': '/prod/twitter/dependencies'
}


def get_env(term):
    result = os.getenv(term)

    if result is None:
        return defaults[term]
    else:
        return result
