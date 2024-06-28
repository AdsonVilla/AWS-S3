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
    
    except (NoCredentialsError, PartialCredentialsError) as err:
        print(f'Credentials error: {err}')
    except Exception as err:
        print(f'Error creating bucket: {err}')
        

def upload_file_to_s3(bucket_name, file_name, object_name):
    try:
        session = boto3.Session()
        
        s3_client = session.client('s3')
        
        if object_name is None:
            object_name = file_name.split('/')[-1]
    
        s3_client.upload_file(file_name, bucket_name, object_name)
        
        print(f'The file {file_name} was sent to bucket {bucket_name} with the name {object_name}.')
    
    except (NoCredentialsError, PartialCredentialsError) as err:
        print(f'Credentials error: {err}')
    except Exception as err:
        print(f'Error uploading file: {err}')

if __name__ == "__main__":
    bucket_name = 'my-test-bucket.v1'
    region = 'us-east-1'
    
    create_s3_bucket(bucket_name, region)

    file_name = '/mnt/c/users/adson/OneDrive/Documentos/AWS/S3-bucket/setup.jpg'
    object_name = 'setup'
    
    upload_file_to_s3(bucket_name, file_name, object_name)
    