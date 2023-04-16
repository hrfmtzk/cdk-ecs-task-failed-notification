#!/usr/bin/env python3
import aws_cdk as cdk

from cdk_ecs_task_failed_notification.cdk_ecs_task_failed_notification_stack import (  # NOQA: E501
    CdkEcsTaskFailedNotificationStack,
)

app = cdk.App()
CdkEcsTaskFailedNotificationStack(
    app,
    "CdkEcsTaskFailedNotificationStack",
)

app.synth()
