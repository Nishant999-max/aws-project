import logging
import boto3
from botocore.exceptions import ClientError
a = input("Enter bucket name : ")
b = input("Enter object name : ")

def create_presigned_url(bucket_name, object_name, expiration=3600):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': a,
                                                            'Key': b},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None
    return response
    url = create_presigned_url(a, b)
    if url is not None:
       response = requests.get(url)
create_presigned_url(a, b)