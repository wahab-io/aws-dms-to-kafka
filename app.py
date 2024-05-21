#!/usr/bin/env python3
import os

import aws_cdk as cdk

from networking.component import Networking
from data_streaming.component import DataStreaming

app = cdk.App()

networking = Networking(app, "Networking")
data_straming = DataStreaming(app, "DataStreaming", vpc=networking.vpc)
data_straming.add_dependency(networking)

app.synth()
