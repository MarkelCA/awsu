import boto3
def get(instance_id):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)
    print(instance.public_ip_address)
    return
