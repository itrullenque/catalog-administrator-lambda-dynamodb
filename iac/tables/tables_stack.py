from aws_cdk import Stack
from constructs import Construct
from .catalog_table import CatalogTable


class TableStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.catalog_table = CatalogTable(
            self,
        )
