from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_dms as dms,
    aws_msk_alpha as msk,
)

from constructs import Construct


class DataStreaming(Stack):
    """
    Data Streaming Stack, DMS and MSK cluster
    """

    def __init__(
        self, scope: Construct, construct_id: str, vpc: ec2.IVpc, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        msk.Cluster(
            self,
            "msk-cluster",
            cluster_name="msk-cluster",
            kafka_version=msk.KafkaVersion.V2_8_1,
            number_of_broker_nodes=1,
            vpc=vpc,
        )
