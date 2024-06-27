#!/usr/bin/env python3
import aws_cdk as cdk
from iac.ci_cd_stack import CodeCatalogPipeline
from config import CDK_DEFAULT_ACCOUNT, CDK_DEFAULT_REGION

app = cdk.App()
code_pipeline_stack = CodeCatalogPipeline(
    app,
    "CodeCatalogPipeline",
    env=cdk.Environment(account=CDK_DEFAULT_ACCOUNT, region=CDK_DEFAULT_REGION),
)

app.synth()
