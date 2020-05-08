import boto3

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb')
    backup_arn = event.BackupArn
    resp = dynamodb.delete_backup(BackupArn=backup_arn)
    return resp