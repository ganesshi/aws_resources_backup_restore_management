import boto3

def lambda_handler(event, context):
    account_id = boto3.client('sts').get_caller_identity().get('Account')
    reg = event['region']
    ec2 = boto3.client('ec2', region_name=reg)
    resp = ec2.describe_snapshots(Filters=[{'Name': 'owner-id', 'Values': [account_id]}])
    snap_list = []
    for snap in resp['Snapshots']:
        snap_list.append(snap['SnapshotId'])
    return snap_list