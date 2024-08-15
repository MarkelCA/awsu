
def add_parser(subparsers):
    ec2_parser = subparsers.add_parser('ec2', help='EC2 Service Utilities')
    ec2_subparsers = ec2_parser.add_subparsers(help='EC2 Subcommands')
    update_hosts_parser = ec2_subparsers.add_parser('update-hosts', help='Update hosts file with your instance IP.')
