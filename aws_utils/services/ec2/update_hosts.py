from argparse import Namespace
import boto3

from aws_utils.config.configure import Config
from aws_utils.config import configure
from aws_utils.services.ec2 import replace_hosts, start

def run(config: Config):
    ec2 = boto3.resource('ec2')
    dev_instance = ec2.Instance(config.ec2_instance_id)
    args = Namespace(wait=True)
    start.run(config,args)
    if not config.ec2_instance_public_ip:
        return "No public IP found in config file. You must run \"awsu configure\""
    configure.update("ec2_instance_public_ip", dev_instance.public_ip_address)
    replace_hosts.run(config.ec2_instance_public_ip, dev_instance.public_ip_address)


