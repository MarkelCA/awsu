import boto3

from aws_utils.config.configure import Config
from aws_utils.config import configure
from aws_utils.services.ec2 import replace_hosts, start

def run(config: Config):
    ec2 = boto3.resource('ec2')
    dev_instance = ec2.Instance(config.ec2_instance_id)
    start.run(config)
    if not config.ec2_instance_public_ip:
        return "No public IP found in config file. You must run \"awsu configure\""
    replace_hosts.run(config.ec2_instance_public_ip, dev_instance.public_ip_address)
    configure.update("ec2_instance_public_ip", dev_instance.public_ip_address)
    return "Instance started and hosts file updated successfully."


