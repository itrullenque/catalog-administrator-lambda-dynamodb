from aws_cdk import aws_iam
from aws_cdk import Stack


class ApiGatewayInvokeRoleLambda:

    def __init__(self, stack: Stack) -> None:

        # Initialize class variables
        self.stack = stack
        self.id = "apigateway_invoke_lambda_role"
        self.name = "apigateway_invoke_lambda_role"
        self.role = self.__create_role()

    def __create_role(self):
        role = aws_iam.Role(
            self.stack,
            "role_" + self.id,
            role_name="role_" + self.name,
            assumed_by=aws_iam.ServicePrincipal("apigateway.amazonaws.com"),
        )

        # Create the policy statement
        lambda_invoke_policy_statement = aws_iam.PolicyStatement()
        lambda_invoke_policy_statement.effect = aws_iam.Effect.ALLOW
        lambda_invoke_policy_statement.add_actions("lambda:InvokeFunction")
        lambda_invoke_policy_statement.add_resources("*")

        inline_policy = aws_iam.Policy(self.stack, "inline_policy_" + self.id)
        inline_policy.add_statements(lambda_invoke_policy_statement)

        role.attach_inline_policy(inline_policy)

        return role
