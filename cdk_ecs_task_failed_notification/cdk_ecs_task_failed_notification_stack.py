from aws_cdk import (
    Stack,
    aws_events as events,
    aws_events_targets as events_targets,
    aws_sns as sns,
)
from constructs import Construct


class CdkEcsTaskFailedNotificationStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        cluster_name: str | None = None,
        task_definition_familes: list[str] | None = None,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        topic = sns.Topic(
            self,
            "Topic",
            display_name="ECS Task Failed Notification",
            topic_name="ecs-task-failed-notification",
        )

        target_condition = {}
        if cluster_name:
            target_condition["clusterArn"] = [
                f"arn:aws:ecs:{self.region}:{self.account}:cluster/{cluster_name}"  # NOQA: E501
            ]
        if task_definition_familes:
            target_condition["taskDefinitionArn"] = [
                {
                    "prefix": f"arn:aws:ecs:{self.region}:{self.account}:task-definition/{task_definition_family}:"  # NOQA: E501
                }
                for task_definition_family in task_definition_familes
            ]

        events.Rule(
            self,
            "RuleNotSuccess",
            description="ECS Task Failed Notification (not success)",
            event_pattern=events.EventPattern(
                source=["aws.ecs"],
                detail_type=["ECS Task State Change"],
                detail={
                    "lastStatus": ["STOPPED"],
                    "desiredStatus": ["STOPPED"],
                    "stopCode": [{"anything-but": "EssentialContainerExited"}],
                }
                | target_condition,
            ),
            targets=[events_targets.SnsTopic(topic)],
        )
        events.Rule(
            self,
            "RuleAppError",
            description="ECS Task Failed Notification (app error)",
            event_pattern=events.EventPattern(
                source=["aws.ecs"],
                detail_type=["ECS Task State Change"],
                detail={
                    "lastStatus": ["STOPPED"],
                    "desiredStatus": ["STOPPED"],
                    "containers": {
                        "exitCode": [{"anything-but": 0}],
                    },
                }
                | target_condition,
            ),
            targets=[events_targets.SnsTopic(topic)],
        )
