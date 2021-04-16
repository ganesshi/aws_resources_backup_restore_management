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
        ec2 = boto3.client('ec2', region_name=reg)

        # Get all in-use volumes in all regions
        result = \
        ec2.ec2.describe_instances(Filters=[{'Name': 'instance-type', 'Values': ['t2.micro']}])['Reservations'][0][
            'Instances']

        for instanceid in result['InstanceId]:
        print"Backing up %s into machine image" % (instanceid)
        result = ec2.create_image(Name='image_'+str(instanceid), InstanceId=instanceid, Description='Created by Lambda backup function ebs-snapshots')

        # Get snapshot resource
        # ec2resource = boto3.resource('ec2', region_name=reg)
        # snapshot = ec2resource.Snapshot(result['SnapshotId'])

        volumename = 'N/A'

        # Find name tag for volume if it exists
        if 'Tags' in volume:
            for
        tags in volume['Tags']:
        if tags["Key"] == 'Name':
            imagename = tags["Value"]

        # Add volume name to snapshot for easier identification
        snapshot.create_tags(Tags=[{'Key': 'Name', 'Value': imagename}])
