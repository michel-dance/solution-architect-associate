from aws_cdk import (
    Stack
)
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_iam as iam

from constructs import Construct

class HelloCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "michel-is-awesome-today", bucket_name='michel-is-awesome',versioned=True)

        # now create a variable called role and assign it to the iam role used for s3 access
        role = iam.Role(self, "s3_full_access", role_name = 's3-full-access', assumed_by=iam.ServicePrincipal("s3.amazonaws.com"))

        # now attach s3 full admin mpolicey to the role
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"))

