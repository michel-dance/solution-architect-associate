from aws_cdk import (
    Stack
)
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_iam as iam
import aws_cdk.aws_cloudwatch as cloudwatch
import aws_cdk.aws_sns as sns
import aws_cdk.aws_sns_subscriptions as subscriptions
import aws_cdk.aws_cloudwatch_actions as actions

from constructs import Construct

class HelloCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "michel-is-awesome-today", bucket_name='michel-is-awesome',versioned=True)

        # now create a variable called role and assign it to the iam role used for s3 access
        role = iam.Role(self, "s3_full_access", role_name = 's3-full-access', assumed_by=iam.ServicePrincipal("s3.amazonaws.com"))

        # now attach s3 full admin policey to the role
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"))

        # create a metric named metric and assign it the USD metric for the aws account, so that whenever the metric value is above $20 we get an alarm
        metric = cloudwatch.Metric(namespace="AWS/Billing", metric_name="EstimatedCharges", dimensions_map={"Currency": "USD"})

        # now create a variable name alarm and assign the metrics and threshold to it and set the alarm to trigger above $20 for 6 hours
        alarm = cloudwatch.Alarm(self, "alarm", metric=metric, threshold=20, evaluation_periods=1)

        # now create an SNS topic and assign it to the variable topic, with the SNS topic sending an email to the email address provided
        topic = sns.Topic(self, "topic", topic_name="michel-is-awesome-topic", display_name="michel-is-awesome-topic")

        subscription = sns.Subscription(self, "email-subscription", topic=topic,
            endpoint='michel+csa@f1kart.com',
            protocol=sns.SubscriptionProtocol.EMAIL)

        sns_action = actions.SnsAction(topic=topic)

        alarm.add_alarm_action(sns_action)