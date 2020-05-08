import boto3


def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    rds = boto3.client('rds')

    # Get list of regions
    regions = ec2.describe_regions().get('Regions', [])

    # Iterate over regions
    for region in regions:
        print
        "Checking region %s " % region['RegionName']
        reg = region['RegionName']

        # Connect to region
        rds = boto3.client('rds', region_name=reg)

        # Get all in-use volumes in all regions
        result = rds.describe_db_instances()

        for db in result['DBInstances']:
            print
            "Backing up %s with database type %s" % (db['DBInstanceIdentifier'], eb['Engine'])
            snapshot = rds.create_db_snapshot(
                DBSnapshotIdentifier="db_snapshot_" + str(eb['Engine']) + str(db['DBInstanceIdentifier']), \
                DBInstanceIdentifier=db['DBInstanceIdentifier'])
            # Get snapshot resource
        for snap in rds.describe_db_snapshots()['DBSnapshots']:
            print
            "Snapshot created %s " % snap['DBSnapshotIdentifier']
