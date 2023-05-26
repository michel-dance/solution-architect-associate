from aws_cdk import (
    Stack
)
import aws_cdk.aws_s3 as s3

from constructs import Construct

class HelloCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "michel-is-awesome-today", bucket_name='michel-is-awesome',versioned=True)

        # another bucket to store my music files
        bucket2 = s3.Bucket(self, "michel-is-awesome-today2", bucket_name='michel-is-awesome2',versioned=True)

        # for loop to create 10 buckets
        for i in range(10):
            bucket = s3.Bucket(self, "michel-is-awesome-today"+str(i), bucket_name='michel-is-awesome'+str(i),versioned=True)
