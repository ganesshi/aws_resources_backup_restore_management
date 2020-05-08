import boto3
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    # return dir(ec2)
    # Get list of regions
    regions = ec2.describe_regions().get('Regions', [])

    # Iterate over regions
    for region in regions:
        print
        "Checking region %s " % region['RegionName']
        reg = region['RegionName']

        # Connect to region
        ec2 = boto3.client('ec2', region_name=reg)
        resp = ec2.run_instances(ImageId='ami-051e7094267b64996', InstanceType='t2.micro', MinCount=1, MaxCount=1)
        ec2.create_tags(Resources=[resp['Instances'][0]['InstanceId']], Tags=[{'Key': 'Name', 'Value': volumename}])
        return resp['Instances'][0]['InstanceId']
