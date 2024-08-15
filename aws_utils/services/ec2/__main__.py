from aws_utils.services.ec2 import instance
import sys

def run(config) -> str:
    print("running ec2")
    if 'get' in sys.argv and 'public-ip' in sys.argv:
        return instance.get(config.ec2_instance_id)
