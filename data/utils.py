import boto3
import os
from botocore.exceptions import NoCredentialsError
import json

# os.environ["AWS_DEFAULT_REGION"] = "us-east-2"

s3 = boto3.client('s3')
ssm = boto3.client('ssm')


def list_bucket_objects(bucket_name):
    result = []
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        objects = response.get('Contents', [])
        for obj in objects:
            print(f"S3 Object: {obj['Key']}")
            result.append(obj['Key'])
    except NoCredentialsError:
        print("No AWS credentials found. Make sure to configure your AWS credentials.")
    except Exception as e:
        print(f"An error occurred while getting objects from bucket': {str(e)}")
        return str(e)


def get_ssm_parameter(parameter_name):
    try:
        response = ssm.get_parameter(Name=parameter_name, WithDecryption=True)
        parameter_value = response['Parameter']['Value']
        return parameter_value
    except NoCredentialsError:
        print("No AWS credentials found. Make sure to configure your AWS credentials.")
    except Exception as e:
        print(f"An error occurred while fetching parameter '{parameter_name}': {str(e)}")
        return str(e)


if __name__ == '__main':

    bucket_name = 'cf-templates-1s2o42js6oxs2-us-east-1'
    param_name = "/dev/username"

    bucket_objs = list_bucket_objects(bucket_name)
    param_val = get_ssm_parameter(param_name)

    print(bucket_objs)
    print(param_val)