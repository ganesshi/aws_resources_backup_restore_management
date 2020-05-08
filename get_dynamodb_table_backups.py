import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    regions = ec2.describe_regions().get('Regions', [])

    # Iterate over regions
    for region in regions:
        print
        "Checking region %s " % region['RegionName']
        reg = region['RegionName']

        dynamodb = boto3.client('dynamodb', region_name=reg)
        result = dynamodb.list_tables()['TableNames']

        for table in result:
            resp = dynamodb.list_backups(TableName=table)
            dynamodb_dict = {}
            backup_list = []
            for backup in resp['BackupSummaries']:
                bkp = {}
                backup_list.append(bkp['backup_name'] = backup['BackupName'])
                backup_list.append(bkp['backup_arn'] = backup['BackupArn'])
                dynamodb_dict[table] = backup_list
    return dynamodb_dict
