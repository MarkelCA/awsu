from argparse import Namespace
import boto3
from boto3.compat import sys

# Used to get properties from the AWS SDK's EC2 instance object.
from aws_utils.config.configure import Config


cli_aws_attributes = {
    'public-ip': 'public_ip_address',
    'state': 'state'
}

cli_describe_attributes = {
    'public-ip': 'PublicIpAddress',
    'state': 'State'
}

def run(config: Config, args: Namespace ) -> str|None:
    client = boto3.client('ec2')

    if args.name:
        custom_filter = [{
            'Name':'tag:Name', 
            'Values': [args.name]}
        ]
    else:
        custom_filter = [{
            'Name':'instance-id', 
            'Values': [config.ec2_instance_id]}
        ]


    response = client.describe_instances(Filters=custom_filter)
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_attribute = cli_describe_attributes.get(args.get_command)
            if instance_attribute is None:
                return "Invalid attribute. Use one of the following: " + str(list(cli_describe_attributes.keys()))

            print(instance.get(instance_attribute))
