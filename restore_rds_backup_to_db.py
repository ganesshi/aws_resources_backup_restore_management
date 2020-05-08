import boto3

def lambda_handler(event, context):
    rds = boto3.client('rds')
    db_id = event.DBInstanceIdentifier
    db_snap_id = event.DBSnapshotIdentifier
    resp = rds.restore_db_instance_from_db_snapshot(DBInstanceIdentifier=db_id, DBSnapshotIdentifier=db_snap_id)
    return resp['DBInstance']
