import boto3
from boto3.compat import sys

# Used to get properties from the AWS SDK's EC2 instance object.
from aws_utils.config.configure import Config


cli_aws_attributes = {
    'public-ip': 'public_ip_address',
    'state': 'state'
}

def run(config: Config, attribute: str) -> str:
    ec2 = boto3.resource('ec2')

    if not attribute:
        print("No attribute provided. Use one of the following:")
        return str(cli_aws_attributes.keys())

    instance = ec2.Instance(config.ec2_instance_id)

    aws_attribute = cli_aws_attributes.get(attribute)

    if aws_attribute is None:
        print("Invalid attribute. Use one of the following:")
        return str(cli_aws_attributes.keys())

    return getattr(instance, aws_attribute)
