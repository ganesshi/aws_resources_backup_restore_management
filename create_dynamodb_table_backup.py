import boto3


def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Get list of regions
    regions = ec2.describe_regions().get('Regions', [])

    # Iterate over regions
    for region in regions:
        print
        "Checking region %s " % region['RegionName']
        reg = region['RegionName']

        # Connect to region
        dynamodb = boto3.client('dynamodb', region_name=reg)

        # Get all in-use volumes in all regions
        result = dynamodb.list_tables()['TableNames']

        for table in result:
            print
            "Backing up table %s" % (table)
            result = dynamodb.create_backup(BackupName='dynamodb_backup_' + str(table), TableName=table,
                                            Description='Created by Lambda backup function ebs-snapshots')
