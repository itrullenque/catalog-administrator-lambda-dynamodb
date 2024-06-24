from aws_cdk import aws_iam, aws_lambda, aws_logs
from aws_cdk import Stack
from aws_cdk.aws_logs import LogGroup
from aws_cdk import Duration
from iac.tables.catalog_table import CatalogTable


class LambdaCatalogDelete:
    def __init__(
        self,
        stack: Stack,
        catalog_table: CatalogTable,
    ) -> None:

        # initialize the class with the parameters passed to the constructor
        self.stack = stack
        self.id = "lambda_catalog_delete_lambda"
        self.name = "lambda_catalog_delete"
        self.catalog_table_name = catalog_table.table_name
        self.function = self.__create_function()

    def __create_function(self):
        func = aws_lambda.Function(
            self.stack,
            self.id,
            function_name=self.name,
            handler="lambda_handler.lambda_handler",
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            log_retention=aws_logs.RetentionDays.ONE_WEEK,
            timeout=Duration.seconds(60),
            code=aws_lambda.Code.from_asset(path="iac/assets/lambda_catalog_delete"),
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
        logs_policy_statement.add_resources("*")

        # inline policy for the role to allow in catalog DynamoDB table
        lambda_dynamodb_policy_statement = aws_iam.PolicyStatement()
        lambda_dynamodb_policy_statement.effect = aws_iam.Effect.ALLOW
        lambda_dynamodb_policy_statement.add_actions("dynamodb:DeleteItem")

        lambda_dynamodb_policy_statement.add_resources(
            f"arn:aws:dynamodb:*:*:table/{self.catalog_table_name}"
        )

        # add the statements to the inline policy
        inline_policy = aws_iam.Policy(self.stack, "inline_policy_" + self.name)
        inline_policy.add_statements(
            logs_policy_statement,
            lambda_dynamodb_policy_statement,
        )

        role.attach_inline_policy(inline_policy)
        return role
