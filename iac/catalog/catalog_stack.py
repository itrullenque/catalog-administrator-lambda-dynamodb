from aws_cdk import Stack
from constructs import Construct
from iac.buckets.buckets_stack import BucketsStack
from iac.tables.tables_stack import TableStack
from .lambda_catalog_post import LambdaCatalogPost


class CatalogStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        buckets_stack: BucketsStack,
        table_stack: TableStack,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.lambda_catalog_post = LambdaCatalogPost(
            self,
            knowledge_catalog_bucket=buckets_stack.knowledge_catalog_bucket,
            catalog_table=table_stack.catalog_table,
        )
