import argparse
import sys
import argcomplete
from aws_utils import ec2

parser = argparse.ArgumentParser(
                    prog='awsu',
                    description='AWS Utilities. An extensible aws wrapper built for custom features.',
                    epilog='Text at the bottom of help')

# Create a subparsers object that will hold the subcommands
subparsers = parser.add_subparsers(dest='command', help='Services')

s3_parser = subparsers.add_parser('s3', help='S3 Service Utilities')
ec2.add_ec2_parser(subparsers)
argcomplete.autocomplete(parser)



# __main__.py
def main():
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    print(args)

if __name__ == '__main__':
    main()

