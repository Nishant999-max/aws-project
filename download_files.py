import boto3
a = input("enter BUCKET_NAME : ")
b = input("enter OBJECT_NAME : ")
c = input("enter FILE_NAME : ")
s3 = boto3.client('s3')
s3.download_file(a, b, c)

s3 = boto3.client('s3')
with open(a, 'wb') as f:
    s3.download_fileobj(a, b, f)