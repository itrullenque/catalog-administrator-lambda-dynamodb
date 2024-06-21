import aws_cdk as cdk
from constructs import Construct
from iac.buckets.buckets_stack import BucketsStack
from iac.catalog.catalog_stack import CatalogStack
from iac.tables.tables_stack import TableStack
from iac._general.general_stack import GeneralStack


class PipelineAppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        general_stack = GeneralStack(self, "GeneralStack")

        buckets_stack = BucketsStack(self, "BucketsStack")

        table_stack = TableStack(self, "TableStack")

        catalogStack = CatalogStack(
            self,
            "CatalogStack",
            buckets_stack=buckets_stack,
            table_stack=table_stack,
            general_stack=general_stack,
        )
