import boto3

def lambda_handler(event, context):
    account_id = boto3.client('sts').get_caller_identity().get('Account')
    reg = event.Region
    ec2 = boto3.client('ec2', region_name=reg)
    #comment 2
    resp = ec2.describe_images(Filters=[{'Name': 'owner-id', 'Values': [account_id]}])
    image_list = []
    for image in resp['Images']:
        image_dict = {}
        image_inner_list = []
        image_dict['image_name'] = image['Name']
        image_dict['image_id'] = image['ImageId']
        image_inner_list.append(image_dict)
        image_list.append(image_inner_list)
    return image_list
