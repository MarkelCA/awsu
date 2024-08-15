from aws_utils.config.configure import Config
from aws_utils.services.ec2 import instance
from aws_utils.services.ec2 import update_hosts
import sys

def add_parser(subparsers):
    ec2_parser = subparsers.add_parser('ec2', help='EC2 Service Utilities')
    ec2_subparsers = ec2_parser.add_subparsers(help='EC2 Subcommands')
    update_hosts_parser = ec2_subparsers.add_parser('update-hosts', help='Update hosts file with your instance IP.')

    get_parser = ec2_subparsers.add_parser('get', help='Get data from your instance.')
    get_commands = get_parser.add_subparsers(help='Get Subcommands')
    get_commands.add_parser('public-ip', help='Get your instance public IP.')

    ec2_subparsers.add_parser('reboot', help='Reboot your instance.')

    ec2_subparsers.add_parser('update-hosts', help='Update hosts file with your instance IP.')
    ec2_subparsers.add_parser('start', help='Start your instance.')
    ec2_subparsers.add_parser('replace-hosts', help='Replace hosts file with the provided IP')
    # ec2_parser.add_argument('ip', help='The IP to replace the current one in the hosts file.')



def run(config: Config) -> str:
    if 'get' in sys.argv:
        return instance.get(config)
    elif 'reboot' in sys.argv:
        return instance.reboot(config)
    elif 'update-hosts' in sys.argv:
        return update_hosts.run(config)
    elif 'start' in sys.argv:
        return instance.start(config)
    elif 'replace-hosts' in sys.argv:
        return update_hosts.replace(config, sys.argv[3])
    else:
        return "No command found."
