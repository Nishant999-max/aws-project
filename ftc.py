import boto3
from boto3.s3.transfer import TransferConfig
a = input("enter the file Name")
b = input("enter the object Name")
c = input("choose your dzired bucket")
GB = 1024 ** 3
config = TransferConfig(multipart_threshold=5*GB)
s3 = boto3.client('s3')
s3.upload_file(a, c, b, Config=config)
config = TransferConfig(max_concurrency=5)
s3 = boto3.client('s3')
s3.download_file(c, b, a, Config=config)
config = TransferConfig(use_threads=False)

s3 = boto3.client('s3')
s3.download_file(c, b, a, Config=config)