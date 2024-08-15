import boto3
from boto3.compat import sys
from botocore.client import ClientError
from aws_utils.config.configure import Config

# Used to get properties from the AWS SDK's EC2 instance object.
cli_aws_attributes = {
    'public-ip': 'public_ip_address'
}

def get(config: Config) -> str:
    ec2 = boto3.resource('ec2')

    if len(sys.argv) < 4:
        return "You must provide an attribute to get from your instance."

    instance = ec2.Instance(config.ec2_instance_id)

    attribute = sys.argv[3]
    aws_attribute = cli_aws_attributes.get(attribute)

    if aws_attribute is None:
        print("Invalid attribute. Use one of the following:")
        return str(cli_aws_attributes.keys())

    return getattr(instance, aws_attribute)

def reboot(config: Config):
    ec2 = boto3.resource('ec2')

    instance = ec2.Instance(config.ec2_instance_id)
    instance.reboot()

    try:
        instance.reboot()
        instance.wait_until_running()
        return f"Instance {config.ec2_instance_id} rebooted successfully."
    except ClientError as err:
        return f"Couldn't reboot instance {config.ec2_instance_id}. Here's why: {err.response['Error']['Code']}: {err.response['Error']['Message']}"

def start(config: Config):
    ec2 = boto3.resource('ec2')

    instance = ec2.Instance(config.ec2_instance_id)

    try:
        instance.start()
        instance.wait_until_running()
        return f"Instance {config.ec2_instance_id} started successfully."
    except ClientError as err:
        return f"Couldn't start instance {config.ec2_instance_id}. Here's why: {err.response['Error']['Code']}: {err.response['Error']['Message']}"
