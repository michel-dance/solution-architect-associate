from aws_cdk import (
    Stack
)
import aws_cdk.aws_s3 as s3

from constructs import Construct

class HelloCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "michel-is-awesome-today", bucket_name='michel-is-awesome',versioned=True)
