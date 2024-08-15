import ipaddress
from dataclasses import dataclass
from pathlib import Path
import yaml
import os
import json


config_dir = f'{Path.home()}/.awsu/'

@dataclass
class Config:
    ec2_instance_ip: str|None = None

def write_config(config: Config):
    # We create the folder for the config file if not exists
    os.makedirs(os.path.dirname(config_dir), exist_ok=True)

    with open(f'{config_dir}/config.yaml', 'w') as yaml_file:
        yaml.dump(config.__dict__, yaml_file)


def read_config() -> Config:
    if not os.path.exists(f'{config_dir}/config.yaml'):
        return Config()

    with open(f'{config_dir}/config.yaml', 'r') as yaml_file:
        config = yaml.safe_load(yaml_file)
        return Config(**config)

def run():
    config = read_config()
    while True:
        ip = input(f"Your EC2 instance public IP [{config.ec2_instance_ip or 'None'}]: ")
        if(ip == ""):
            ip = config.ec2_instance_ip
            break
        elif is_valid_ip(ip):
            break
        print("Error - Invalid IP address, try again.")

    config = Config(ec2_instance_ip=ip)
    write_config(config)


def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
