from aws_cdk import aws_iam, aws_lambda, aws_logs
from aws_cdk import Stack
from aws_cdk.aws_logs import LogGroup
from aws_cdk import Duration
from iac.buckets.knowledge_catalog_bucket import KnowledgeCatalogBucket


class LambdaCatalogPost:
    def __init__(
        self,
        stack: Stack,
        knowledge_catalog_bucket: KnowledgeCatalogBucket,
    ) -> None:

        # initialize the stack with the parameters passed to the constructor
        self.stack = stack
        self.id = "lambda_catalog_post_lambda"
        self.name = "lambda_catalog_post"
        self.knowledge_catalog_bucket = knowledge_catalog_bucket.bucket
        self.knowledge_catalog_bucket_arn = knowledge_catalog_bucket.bucket.bucket_arn
        self.function = self.__create_function()

    def __create_function(self):
        func = aws_lambda.Function(
            self.stack,
            self.id,
            function_name=self.name,
            handler="lambda_hamdler.lambda_handler",
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            log_retention=aws_logs.RetentionDays.ONE_WEEK,
            timeout=Duration.seconds(60),
            code=aws_lambda.Code.from_asset(path="iac/assets/lambda_catalog_post"),
            role=self.role(),
            memory_size=1024,
        )
        return func

    def role(self):
        role = aws_iam.Role(
            self.stack,
            "role_" + self.name,
            assumed_by=aws_iam.ServicePrincipal("lambda.amazonaws.com"),
        )

        # inline policy for the role to allow the lambda function to create log groups, log streams, and log events
        logs_policy_statement = aws_iam.PolicyStatement()
        logs_policy_statement.effect = aws_iam.Effect.ALLOW
        logs_policy_statement.add_actions(
            "logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"
        )

        # inline policy for the role to allow the lambda function to upload objects to the s3 bucket
        logs_policy_statement.add_resources("*")
        lambda_upload_s3_policy_statement = aws_iam.PolicyStatement()
        lambda_upload_s3_policy_statement.effect = aws_iam.Effect.ALLOW
        lambda_upload_s3_policy_statement.add_actions("s3:PutObject", "s3:GetObject")

        lambda_upload_s3_policy_statement.add_resources(
            self.knowledge_catalog_bucket_arn + "/*"
        )

        # add the statements to the inline policy
        inline_policy = aws_iam.Policy(self.stack, "inline_policy_" + self.name)
        inline_policy.add_statements(
            logs_policy_statement, lambda_upload_s3_policy_statement
        )

        role.attach_inline_policy(inline_policy)
        return role
