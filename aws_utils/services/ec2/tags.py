import boto3
from argparse import Namespace

from botocore.client import ClientError
from aws_utils.config.configure import Config


def run(config: Config, args: Namespace) -> str|None:
    if args.tags_command == 'set':
        return set(config, args.key, args.value)
    return 'run'

def set(config, key: str, value: str) -> str:
    ec2 = boto3.resource('ec2')

    instance = ec2.Instance(config.ec2_instance_id)

    try:
        instance.create_tags(
            Tags=[
                {
                    'Key': key,
                    'Value': value
                },
            ]
        )
        return "Tag set successfully."
    except ClientError as err:
        return f"Couldn't set tag {key} to {value}. Here's why: {err.response['Error']['Code']}: {err.response['Error']['Message']}"
