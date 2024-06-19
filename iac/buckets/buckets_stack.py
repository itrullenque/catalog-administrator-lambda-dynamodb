from aws_cdk import Stack
from constructs import Construct
from .knowledge_catalog_bucket import KnowledgeCatalogBucket


class BucketsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.knowledge_catalog_bucket = KnowledgeCatalogBucket(self)
