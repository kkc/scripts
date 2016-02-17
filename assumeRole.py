import boto3
client = boto3.client('sts')

response = client.assume_role(
    RoleArn='arn:aws:iam::774915305292:role/exportClip',
    RoleSessionName='AssumeRole'
)

print 'SecretAccessKey:', response['Credentials']['SecretAccessKey']
print 'SessionToken:', response['Credentials']['SessionToken']
print 'AccessKeyId:', response['Credentials']['AccessKeyId']
