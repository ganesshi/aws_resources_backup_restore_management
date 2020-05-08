import boto3
import json
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    snap_id = event['params']['querystring']['SnapshotId']
    result = ec2.create_volume(AvailabilityZone='us-east-2a', SnapshotId=snap_id)
    volume_id = result['VolumeId']
    volumename = 'Restored_Volume_From_'+str(snap_id)
    ec2.create_tags(Resources=[volume_id],Tags=[{'Key': 'Name','Value': volumename}])
    result.pop('ResponseMetadata')
    result.pop('CreateTime')
    return json.dumps(result)