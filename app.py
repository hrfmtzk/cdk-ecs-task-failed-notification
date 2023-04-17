#!/usr/bin/env python3
import json

import aws_cdk as cdk

from cdk_ecs_task_failed_notification.cdk_ecs_task_failed_notification_stack import (  # NOQA: E501
    CdkEcsTaskFailedNotificationStack,
)

with open("./config.json", "r") as fp:
    config = json.load(fp=fp)

app = cdk.App()
CdkEcsTaskFailedNotificationStack(
    app,
    "CdkEcsTaskFailedNotificationStack",
    cluster_name=config["clusterName"],
    task_definition_familes=config["taskDefinitionFamilies"],
)

app.synth()
