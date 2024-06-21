from aws_cdk import aws_apigateway
from aws_cdk import Stack
from iac._general.api_gateway_role import ApiGatewayInvokeRoleLambda
from .lambda_catalog_post import LambdaCatalogPost


class CatalogApiGateway:
    def __init__(
        self,
        stack: Stack,
        apigateway_invoke_lambda_role: ApiGatewayInvokeRoleLambda,
        lambda_catalog_post: LambdaCatalogPost,
    ) -> None:

        # Initialize class variables
        self.stack = stack
        self.id = "catalog_api_gateway"
        self.name = "apicatalog"
        # external reference
        self.apigateway_invoke_lambda_role = apigateway_invoke_lambda_role.role
        self.lambda_catalog_post = lambda_catalog_post.function
        self.api = self.__create_api_gateway()

    def __create_api_gateway(self):
        rest_api = aws_apigateway.RestApi(
            self.stack,
            self.id,
            rest_api_name=self.name,
            deploy=True,
            disable_execute_api_endpoint=False,
        )

        aws_apigateway.Stage(
            self.stack,
            id="catalog" + "_stage",
            deployment=rest_api.latest_deployment,
            stage_name="catalog",
        )

        # create the resources
        catalog_resource = rest_api.root.add_resource("catalog")

        # create the integrations
        lambda_catalog_post_integration = aws_apigateway.LambdaIntegration(
            handler=self.lambda_catalog_post,
            proxy=True,
            credentials_role=self.apigateway_invoke_lambda_role,
        )

        # create the methods
        catalog_resource.add_method(
            "POST", lambda_catalog_post_integration, api_key_required=False
        )

        catalog_resource.add_cors_preflight(
            allow_origins=["*"],
            allow_headers=[
                "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token"
            ],
            allow_methods=["POST", "GET", "PUT", "OPTIONS"],
        )

        return rest_api
