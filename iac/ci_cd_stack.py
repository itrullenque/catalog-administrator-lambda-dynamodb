import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from .stage import PipelineAppStage
from config import CDK_DEFAULT_ACCOUNT, CDK_DEFAULT_REGION


class CodeCatalogPipeline(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline = CodePipeline(
            self,
            "CatalogPipeline",
            pipeline_name="CatalogPipeline",
            synth=ShellStep(
                "Synth",
                input=CodePipelineSource.git_hub(
                    "itrullenque/catalog-administrator-lambda-dynamodb", "main"
                ),
                commands=[
                    "npm install -g aws-cdk",
                    "python -m pip install -r requirements.txt",
                    "cdk synth '*'",
                ],
            ),
        )

        pipeline.add_stage(
            PipelineAppStage(
                self,
                "dev",
                env=cdk.Environment(
                    account=CDK_DEFAULT_ACCOUNT, region=CDK_DEFAULT_REGION
                ),
            )
        )
