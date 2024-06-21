import aws_cdk as cdk
from constructs import Construct
from iac.buckets.buckets_stack import BucketsStack
from iac.catalog.catalog_stack import CatalogStack
from iac.tables.tables_stack import TableStack


class PipelineAppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucketsStack = BucketsStack(self, "BucketsStack")

        tableStack = TableStack(self, "TableStack")

        catalogStack = CatalogStack(
            self, "CatalogStack", buckets_stack=bucketsStack, table_stack=tableStack
        )
