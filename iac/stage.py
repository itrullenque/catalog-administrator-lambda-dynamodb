import aws_cdk as cdk
from constructs import Construct
from iac.buckets.buckets_stack import BucketsStack


class PipelineAppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucketsStack = BucketsStack(self, "BucketsStack")
