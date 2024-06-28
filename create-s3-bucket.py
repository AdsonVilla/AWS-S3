import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# print(boto3.__version__)

def create_s3_bucket(bucket_name, region=None):
    try:
        session = boto3.Session()
        
        s3_client = session.client('s3', region_name=region)
        
        if region is None:
            s3_client.create_bucket(Bucket=bucket_name)
        
        else:
            s3_client.create_bucket(Bucket=bucket_name)
        
        print(f'Bucket {bucket_name} was created in the region {region}!')
    
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f'Credentials error: {e}')
    except Exception as e:
        print(f'Error creating bucket: {e}')

if __name__ == "__main__":
    bucket_name = 'my-test-bucket.v1'
    region = 'us-east-1'
    
    create_s3_bucket(bucket_name, region)
