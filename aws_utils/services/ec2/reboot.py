import boto3
from botocore.client import ClientError
from aws_utils.config.configure import Config


def run(config: Config):
    ec2 = boto3.resource('ec2')

    instance = ec2.Instance(config.ec2_instance_id)
    instance.reboot()

    try:
        instance.reboot()
        instance.wait_until_running()
        return f"Instance {config.ec2_instance_id} rebooted successfully."
    except ClientError as err:
        return f"Couldn't reboot instance {config.ec2_instance_id}. Here's why: {err.response['Error']['Code']}: {err.response['Error']['Message']}"

