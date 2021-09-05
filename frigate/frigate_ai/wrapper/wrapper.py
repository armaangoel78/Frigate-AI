import boto3
import logging
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

def frigate_model(inputDataPath: str, outputDataPath: str):
    def frigate_model_sub(function):
        def wrapper(bucket: str, file: str, *args, **kwargs):
            try:
                s3.download_file(bucket, file, inputDataPath)
                function()
                response = s3.upload_file(outputDataPath, bucket, 'output.json')
            except ClientError as e:
                logging.error(e)
                return False
        return wrapper
    return frigate_model_sub