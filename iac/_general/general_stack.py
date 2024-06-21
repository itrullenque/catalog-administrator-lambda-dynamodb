from aws_cdk import Stack
from constructs import Construct
from .api_gateway_role import ApiGatewayInvokeRoleLambda


class GeneralStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.api_gateway_role = ApiGatewayInvokeRoleLambda(self)
