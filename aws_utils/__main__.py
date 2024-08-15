import argparse
import sys
import argcomplete
from aws_utils.services import ec2, s3

parser = argparse.ArgumentParser(
                    prog='awsu',
                    description='AWS Utilities. An extensible aws wrapper built for custom features.',
                    epilog='Text at the bottom of help')

# Create a subparsers object that will hold the subcommands
subparsers = parser.add_subparsers(dest='command', help='Services')
ec2.add_parser(subparsers)
s3.add_parser(subparsers)

argcomplete.autocomplete(parser)



def main():
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    print(args)

if __name__ == '__main__':
    main()

