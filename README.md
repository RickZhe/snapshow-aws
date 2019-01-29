# snapshow-aws
AWS EC2 snapshot

## About

Use boto3 to manage AWS EC2 instance snapshots

## Configuring

snapshow uses the configure file creates by AWS cli

`aws configure --profile snapshow-aws`

## Running
`pipenv run python "snapshow/snapshow.py <command> <--project=PROJECT>"`

*command* is list, start, or stop
*project* is tag from AWS.