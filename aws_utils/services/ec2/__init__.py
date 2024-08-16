from aws_utils.config.configure import Config
from aws_utils.services.ec2 import update_hosts,get,start,reboot,replace_hosts,stop
import sys

def add_parser(subparsers):
    ec2_parser = subparsers.add_parser('ec2', help='EC2 Service Utilities')
    ec2_subparsers = ec2_parser.add_subparsers(help='EC2 Subcommands')
    ec2_subparsers.add_parser('update-hosts', help='Update hosts file with your instance IP.')

    get_parser = ec2_subparsers.add_parser('get', help='Get data from your instance.')
    get_commands = get_parser.add_subparsers(help='Get Subcommands')
    get_commands.add_parser('public-ip', help='Get your instance public IP.')

    ec2_subparsers.add_parser('reboot', help='Reboot your instance.')

    ec2_subparsers.add_parser('update-hosts', help='Update hosts file with your instance IP.')
    ec2_subparsers.add_parser('start', help='Start your instance.')
    ec2_subparsers.add_parser('stop', help='Stop your instance.')

    replace_hosts_parser = ec2_subparsers.add_parser('replace-hosts', help='Replace hosts file with the provided IP')
    replace_hosts_parser.add_argument('old_ip', help='Current IP to replace in your hosts file') 
    replace_hosts_parser.add_argument('new_ip', help='New IP of your instance')



def run(config: Config) -> str:
    if 'get' in sys.argv:
        return get.run(config)
    elif 'reboot' in sys.argv:
        return reboot.run(config)
    elif 'update-hosts' in sys.argv:
        return update_hosts.run(config)
    elif 'start' in sys.argv:
        return start.run(config)
    elif 'stop' in sys.argv:
        return stop.run(config)
    elif 'replace-hosts' in sys.argv:
        return replace_hosts.run(sys.argv[-2], sys.argv[-1])
    else:
        return "No command found."
