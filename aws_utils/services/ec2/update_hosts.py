from argparse import Namespace
import boto3

from aws_utils.config.configure import Config
from aws_utils.config import configure
from aws_utils.services.ec2 import replace_hosts, start


def run_by_name(config: Config, args: Namespace):
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

    if not response["Reservations"]:
        print(f"No instances found. with the provided tag Name={args.name}")
        return None

    if len(response["Reservations"]) > 1:
        print(f"More than one instance found with the tag Name like \"{args.name}\" The Name must be a unique this command to work")
        return None

    return response["Reservations"][0]["Instances"][0]["InstanceId"]


def run(config: Config, args: Namespace):
    ec2_instance_id = config.ec2_instance_id
    if args.name:
        instance_id_by_name = run_by_name(config, args)
        if instance_id_by_name:
            ec2_instance_id = instance_id_by_name
        else:
            return None


    ##############################
    args = Namespace(wait=True, ec2_instance_id=ec2_instance_id)
    ec2 = boto3.resource('ec2')
    dev_instance = ec2.Instance(args.ec2_instance_id)
    if dev_instance.state["Name"] == "running":
        print("Instance is already running skipping start command.")
    else:
        start.run(config,args)
    if not config.ec2_instance_public_ip:
        return "No public IP found in config file. You must run \"awsu configure\""
    configure.update("ec2_instance_public_ip", dev_instance.public_ip_address)
    replace_hosts.run(config.ec2_instance_public_ip, dev_instance.public_ip_address)


