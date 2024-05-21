#!/usr/bin/env python3
import os

import aws_cdk as cdk

from networking.component import Networking
from backend.component import Backend
from data_streaming.component import DataStreaming

app = cdk.App()

# Create the networking stack
networking = Networking(app, "Networking")

# Create the backend stack
backend = Backend(app, "Backend", vpc=networking.vpc)
backend.add_dependency(networking)

# Create the data streaming stack
data_straming = DataStreaming(app, "DataStreaming", vpc=networking.vpc)
data_straming.add_dependency(networking)

app.synth()
