import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    image_id = event.ImageId
    ec2.deregister_image(ImageId=image_id)