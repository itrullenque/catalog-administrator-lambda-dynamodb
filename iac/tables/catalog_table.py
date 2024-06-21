from aws_cdk import aws_dynamodb
from aws_cdk import Stack
from aws_cdk import RemovalPolicy


class CatalogTable:
    def __init__(self, stack: Stack):
        # Initialize the stack with the parameters passed to the constructor
        self.stack = stack
        self.id = "catalog_table"
        self.table_name = "catalog"
        self.table = self.__create_table()

    # Create the DynamoDB table
    def __create_table(self):

        partition_key = aws_dynamodb.Attribute(
            name="catalog_id", type=aws_dynamodb.AttributeType.STRING
        )

        sort_key = aws_dynamodb.Attribute(
            name="course_id", type=aws_dynamodb.AttributeType.STRING
        )

        table = aws_dynamodb.Table(
            self.stack,
            id=self.id,
            table_name=self.table_name,
            partition_key=partition_key,
            sort_key=sort_key,
            point_in_time_recovery=True,
            billing_mode=aws_dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,
        )

        # GSI definition
        # Name: academic_year - index
        # PK: academic_year
        academic_year_partition_key = aws_dynamodb.Attribute(
            name="academic_year", type=aws_dynamodb.AttributeType.NUMBER
        )

        table.add_global_secondary_index(
            index_name="academic_year-index",
            partition_key=academic_year_partition_key,
            projection_type=aws_dynamodb.ProjectionType.ALL,
        )

        # Name: course_id - index
        # PK: course_id
        course_id_partition_key = aws_dynamodb.Attribute(
            name="course_id", type=aws_dynamodb.AttributeType.STRING
        )

        table.add_global_secondary_index(
            index_name="course_id-index",
            partition_key=course_id_partition_key,
            projection_type=aws_dynamodb.ProjectionType.ALL,
        )

        return table
