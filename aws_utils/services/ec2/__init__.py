from aws_utils.config.configure import Config
from aws_utils.services.ec2 import update_hosts, get, start, reboot, replace_hosts, stop, tags

def add_parser(subparsers):
    ec2_parser = subparsers.add_parser('ec2', help='EC2 Service Utilities')
    
    ec2_subparsers = ec2_parser.add_subparsers(dest='subcommand', help='EC2 Subcommands')

    tags_parser = ec2_subparsers.add_parser('tags', help='Edit your instance tags.')
    tags_subparsers = tags_parser.add_subparsers(dest='tags_command', help='Tags Subcommands')
    tags_set_parser = tags_subparsers.add_parser('set', help='Set tags to your instance.')
    # tags_set_subparser = tags_set_parser.add_subparsers(dest='tags_set_command', help='Tags Set Subcommands')
    tags_set_parser.add_argument('key', help='Key of the tag')
    tags_set_parser.add_argument('value', help='Value of the tag')

    
    # Get Subcommand
    get_parser = ec2_subparsers.add_parser('get', help='Get data from your instance.')
    get_subparsers = get_parser.add_subparsers(dest='get_command', help='Get Subcommands')
    get_subparsers.add_parser('public-ip', help='Get your instance public IP.')
    get_subparsers.add_parser('state', help='Get your instance state.')
    get_parser.add_argument('-n', '--name', type=str, help='Value of the Name tag of your instance.')

    # Other EC2 Subcommands
    ec2_subparsers.add_parser('reboot', help='Reboot your instance.')
    ec2_subparsers.add_parser('update-hosts', help='Update hosts file with your instance IP.')
    start_subparser = ec2_subparsers.add_parser('start', help='Start your instance.')
    start_subparser.add_argument('-w', '--wait', action='store_true', help='Wait until the instance is started.')
    stop_subparser = ec2_subparsers.add_parser('stop', help='Stop your instance.')
    stop_subparser.add_argument('-w', '--wait', action='store_true', help='Wait until the instance is stopped.')

    # Replace Hosts Subcommand
    replace_hosts_parser = ec2_subparsers.add_parser('replace-hosts', help='Replace hosts file with the provided IP')
    replace_hosts_parser.add_argument('old_ip', help='Current IP to replace in your hosts file')
    replace_hosts_parser.add_argument('new_ip', help='New IP of your instance')


def run(config: Config, args) -> str|None:
    if args.subcommand == 'get':
        return get.run(config, args)
    elif args.subcommand == 'reboot':
        return reboot.run(config)
    elif args.subcommand == 'update-hosts':
        update_hosts.run(config)
    elif args.subcommand == 'start':
        return start.run(config, args)
    elif args.subcommand == 'stop':
        return stop.run(config, args)
    elif args.subcommand == 'replace-hosts':
        return replace_hosts.run(args.old_ip, args.new_ip)
    elif args.subcommand == 'tags':
        return tags.run(config, args)

    else:
        return "No valid command found."

