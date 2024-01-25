import boto3
lambda_Client = boto3.client('lambda', region_name="ap-south-1")
response = lambda_Client.create_function(
    Code={
        'S3Bucket': 'lambda-python-jen',
        'S3Key': 'test.zip',  # how can i create or fetch this S3Key
    },

    FunctionName='s3-lambda-ec2',
    Handler='test.lambda_handler',
    Publish=True,
    Role='arn:aws:iam::396153768758:role/lambda-ec2',
    Runtime='python3.12'
)
