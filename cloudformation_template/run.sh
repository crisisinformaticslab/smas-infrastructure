#!/bin/bash

# Validate first
# aws cloudformation validate-template --template-body file://kinesis/iam.yaml
# aws cloudformation validate-template --template-body file://iam/base.yaml

aws cloudformation package --profile smas --template-file root.yaml --output-template packaged.yaml --s3-bucket smas-cf

aws cloudformation deploy --profile smas --region us-west-2 --template-file packaged.yaml --stack-name smas --capabilities CAPABILITY_IAM