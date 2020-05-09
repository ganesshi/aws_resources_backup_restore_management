import boto3
import random

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    regions = ec2.describe_regions().get('Regions', [])
    # Iterate over regions
    for region in regions:
        print"Checking region %s " % region['RegionName']
        reg = region['RegionName']
        # Connect to region
        ec2 = boto3.client('ec2', region_name=reg)
        # Get all in-use volumes in all regions
        result = dynamodb.list_backups()['BackupSummaries']
        for backuparn in result:
            backuparn = backuparn['BackupArn']
            dynamodb.restore_table_from_backup(
                TargetTableName='restore_table_dynamodb_' + str(random.randint(1, 10000)), BackupArn=backuparn)
            print"Restore operation started for backup %s " % (backuparn)
