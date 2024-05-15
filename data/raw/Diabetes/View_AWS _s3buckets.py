# View the AWS s3 buckets using Python
import os
import boto3

# Get AWS credentials and bucket name from environment variables
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
bucket_name = os.getenv('BUCKET_NAME')

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

# Create an S3 resource object using the session
s3 = session.resource('s3')

# Get the S3 bucket
bucket = s3.Bucket(bucket_name)

# List all objects in the bucket
for obj in bucket.objects.all():
    print(obj.key)

