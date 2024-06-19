#!/usr/bin/env python3
import aws_cdk as cdk
from iac.ci_cd_stack import CodePipelineDemo

app = cdk.App()
code_pipeline_stack = CodePipelineDemo(
    app,
    "CodePipelineDemo",
    env=cdk.Environment(account="051556718043", region="us-east-1"),
)

app.synth()
