import boto3
def lambda_handler(event, context):
    reg = event.region_name
    rds = boto3.client('rds', region_name=reg)
    resp = rds.describe_db_snapshots()
    snap_list = []
    for snap in resp['DBSnapshots']:
        snap_list.append(snap['DBSnapshotIdentifier'])
    return snap_list
