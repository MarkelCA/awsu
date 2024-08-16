from argparse import Namespace
from botocore.client import ClientError
import boto3

from aws_utils.config.configure import Config


def run(config: Config, args: Namespace) -> str:
    ec2 = boto3.resource('ec2')

    instance = ec2.Instance(config.ec2_instance_id)

    try:
        instance.stop()
        if args.wait:
            print(f"Waiting until instance {config.ec2_instance_id} is stopped...")
            instance.wait_until_stopped()
            return f"Instance {config.ec2_instance_id} stopped successfully."
        return f"Stopping instance {config.ec2_instance_id}..."
    except ClientError as err:
        return f"Couldn't start instance {config.ec2_instance_id}. Here's why: {err.response['Error']['Code']}: {err.response['Error']['Message']}"
