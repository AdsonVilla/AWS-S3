import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# print(boto3.__version__)

def create_s3_bucket(bucket_name, region=None):
    try:
        session = boto3.Session()
        
        s3_client = session('s3', region_name=region)
        
        if region is None:
            s3_client.create_bucket(Bucket=bucket_name)
        
        else:
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        
        print(f'Bucket {bucket_name} was created!')
    
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f'Credentials error: {e}')
    except Exception as e:
        print(f'Error creating bucket: {e}')

if __name__ == "__main__":
    bucket_name = 'my-test-bucket.v1'
    region = 'us-east-1'
    
    create_s3_bucket(bucket_name, region)
