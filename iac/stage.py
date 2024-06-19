import aws_cdk as cdk
from constructs import Construct
from iac.buckets.buckets_stack import BucketsStack
from iac.catalog.catalog_stack import CatalogStack


class PipelineAppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucketsStack = BucketsStack(self, "BucketsStack")

        catalogStack = CatalogStack(self, "CatalogStack")
