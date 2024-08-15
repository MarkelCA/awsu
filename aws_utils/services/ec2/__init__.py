
def add_parser(subparsers):
    ec2_parser = subparsers.add_parser('ec2', help='EC2 Service Utilities')
    ec2_subparsers = ec2_parser.add_subparsers(help='EC2 Subcommands')
    update_hosts_parser = ec2_subparsers.add_parser('update-hosts', help='Update hosts file with your instance IP.')

    get_parser = ec2_subparsers.add_parser('get', help='Get data from your instance.')
    get_commands = get_parser.add_subparsers(help='Get Subcommands')
    get_commands.add_parser('public-ip', help='Get your instance public IP.')
    
