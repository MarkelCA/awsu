from botocore.client import ClientError
import boto3

from aws_utils.config.configure import Config


def run(config: Config):
    ec2 = boto3.resource('ec2')

    print(f"Stopping instance {config.ec2_instance_id}")
    instance = ec2.Instance(config.ec2_instance_id)

    try:
        instance.stop()
        # instance.wait_until_stopped()
        return f"Instance {config.ec2_instance_id} stopped successfully."
    except ClientError as err:
        return f"Couldn't start instance {config.ec2_instance_id}. Here's why: {err.response['Error']['Code']}: {err.response['Error']['Message']}"
