import re
import os
import sys
import boto3
import subprocess

from aws_utils.config.configure import Config
from aws_utils.services.ec2 import instance

def run(config: Config):
    ec2 = boto3.resource('ec2')
    dev_instance = ec2.Instance(config.ec2_instance_id)
    instance.start(config)
    replace(config, dev_instance.public_ip_address)
    return "Instance started and hosts file updated successfully."


def ask_sudo_permissions():
    if os.geteuid() != 0:
        subprocess.call(['sudo' ] + sys.argv)
        sys.exit()

def replace(config: Config, new_ip: str):
    print(f"Replacing {config.ec2_instance_public_ip} with {new_ip} in /etc/hosts")
    ask_sudo_permissions()
    with open ('/etc/hosts', 'r' ) as f:
        content = f.read()
        # content_new = re.sub(f'{config.ec2_instance_public_ip}', rf'{new_ip}', content, flags = re.M)
        content_new = re.sub(f'pruebamarkel', rf'markelprueba', content, flags = re.M)

        with open('/etc/hosts', 'w') as f:
            f.write(content_new)
            return "Hosts file updated successfully."
