import boto3

def lambda_handler(event, context):
    reg = event.region_name
    db_id = event.DBSnapshotIdentifier
    rds = boto3.client('rds', region_name=reg)
    resp = rds.delete_db_snapshot(DBSnapshotIdentifier=db_id)
    return resp['DBSnapshot']['Status']