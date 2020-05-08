import boto3
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    regions = ec2.describe_regions().get('Regions',[] )

    for region in regions:
        print "Checking region %s " % region['RegionName']
        reg=region['RegionName']

        dynamodb = boto3.client('dynamodb', region_name=reg)
        result = dynamodb.list_tables()['TableNames']
        resp = dynamodb.restore_table_from_backup(TargetTableName='Shinde',
                                           BackupArn="arn:aws:dynamodb:us-east-2:224847766004:table/ganesh_dynamodb/backup/01586601770707-5a139b55")
        return resp['TableDescription']['RestoreSummary']