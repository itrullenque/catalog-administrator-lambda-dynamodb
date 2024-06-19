from aws_cdk import Stack
from constructs import Construct
from .lambda_catalog_post import LambdaCatalogPost


class CatalogStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.lambda_catalog_post = LambdaCatalogPost(self)
