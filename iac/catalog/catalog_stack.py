from aws_cdk import Stack
from constructs import Construct
from iac.buckets.buckets_stack import BucketsStack
from iac.tables.tables_stack import TableStack
from iac._general.general_stack import GeneralStack
from .catalog_api_gateway import CatalogApiGateway
from .lambda_catalog_post import LambdaCatalogPost
from .lambda_catalog_item_get import LambdaCatalogItemGet
from .lambda_catalog_delete import LambdaCatalogDelete


class CatalogStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        buckets_stack: BucketsStack,
        table_stack: TableStack,
        general_stack: GeneralStack,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.lambda_catalog_post = LambdaCatalogPost(
            self,
            knowledge_catalog_bucket=buckets_stack.knowledge_catalog_bucket,
            catalog_table=table_stack.catalog_table,
        )

        self.lambda_catalog_item_get = LambdaCatalogItemGet(
            self,
            catalog_table=table_stack.catalog_table,
        )

        self.lambda_catalog_delete = LambdaCatalogDelete(
            self,
            catalog_table=table_stack.catalog_table,
        )

        # apis
        self.catalog_api_gateway = CatalogApiGateway(
            self,
            apigateway_invoke_lambda_role=general_stack.api_gateway_role,
            lambda_catalog_post=self.lambda_catalog_post,
            lambda_catalog_item_get=self.lambda_catalog_item_get,
            lambda_catalog_delete=self.lambda_catalog_delete,
        )
