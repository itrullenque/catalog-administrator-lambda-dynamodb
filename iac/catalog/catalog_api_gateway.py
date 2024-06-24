from aws_cdk import aws_apigateway
from aws_cdk import Stack
from iac._general.api_gateway_role import ApiGatewayInvokeRoleLambda
from .lambda_catalog_post import LambdaCatalogPost
from .lambda_catalog_item_get import LambdaCatalogItemGet
from .lambda_catalog_delete import LambdaCatalogDelete
from .lambda_catalogs_get import LambdaCatalogsGet


class CatalogApiGateway:
    def __init__(
        self,
        stack: Stack,
        apigateway_invoke_lambda_role: ApiGatewayInvokeRoleLambda,
        lambda_catalog_post: LambdaCatalogPost,
        lambda_catalog_item_get: LambdaCatalogItemGet,
        lambda_catalog_delete: LambdaCatalogDelete,
        lambda_catalogs_get: LambdaCatalogsGet,
    ) -> None:

        # Initialize class variables
        self.stack = stack
        self.id = "catalog_api_gateway"
        self.name = "apicatalog"
        # external reference
        self.apigateway_invoke_lambda_role = apigateway_invoke_lambda_role.role
        self.lambda_catalog_post = lambda_catalog_post.function
        self.lambda_catalog_item_get = lambda_catalog_item_get.function
        self.lamda_catalog_delete = lambda_catalog_delete.function
        self.lambda_catalogs_get = lambda_catalogs_get.function
        self.api = self.__create_api_gateway()

    def __create_api_gateway(self):
        rest_api = aws_apigateway.RestApi(
            self.stack,
            self.id,
            rest_api_name=self.name,
            deploy=True,
            deploy_options=aws_apigateway.StageOptions(stage_name="dev"),
            disable_execute_api_endpoint=False,
        )

        # create the resources
        catalog_resource = rest_api.root.add_resource("catalog")
        catalogs_resource = rest_api.root.add_resource("catalogs")

        # create the integrations
        lambda_catalog_post_integration = aws_apigateway.LambdaIntegration(
            handler=self.lambda_catalog_post,
            proxy=True,
            credentials_role=self.apigateway_invoke_lambda_role,
        )

        lambda_catalog_item_get_integration = aws_apigateway.LambdaIntegration(
            handler=self.lambda_catalog_item_get,
            proxy=True,
            credentials_role=self.apigateway_invoke_lambda_role,
        )

        lambda_catalog_delete_integration = aws_apigateway.LambdaIntegration(
            handler=self.lamda_catalog_delete,
            proxy=True,
            credentials_role=self.apigateway_invoke_lambda_role,
        )

        lambda_catalogs_get_integration = aws_apigateway.LambdaIntegration(
            handler=self.lambda_catalogs_get,
            proxy=True,
            credentials_role=self.apigateway_invoke_lambda_role,
        )

        # create the methods
        catalog_resource.add_method(
            "POST", lambda_catalog_post_integration, api_key_required=False
        )

        catalog_resource.add_method(
            "GET", lambda_catalog_item_get_integration, api_key_required=False
        )

        catalog_resource.add_method(
            "DELETE", lambda_catalog_delete_integration, api_key_required=False
        )

        catalogs_resource.add_method(
            "GET", lambda_catalogs_get_integration, api_key_required=False
        )

        catalogs_resource.add_cors_preflight(
            allow_origins=["*"],
            allow_headers=[
                "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token"
            ],
            allow_methods=["POST", "GET", "PUT", "OPTIONS"],
        )

        catalog_resource.add_cors_preflight(
            allow_origins=["*"],
            allow_headers=[
                "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token"
            ],
            allow_methods=["POST", "GET", "PUT", "OPTIONS"],
        )

        return rest_api
