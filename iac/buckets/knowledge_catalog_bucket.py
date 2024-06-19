from aws_cdk import aws_s3
from aws_cdk import Stack


class KnowledgeCatalogBucket:

    def __init__(self, stack: Stack) -> None:
        self.stack = stack
        self.bucket_id = "knowledge-catalog-bucket"
        self.bucket = self.__create_s3_bucket()

    def __create_s3_bucket(self) -> aws_s3.Bucket:
        bucket = aws_s3.Bucket(
            self.stack,
            id=self.bucket_id,
            bucket_name=self.bucket_id,
            block_public_access=aws_s3.BlockPublicAccess.BLOCK_ALL,
        )

        return bucket
