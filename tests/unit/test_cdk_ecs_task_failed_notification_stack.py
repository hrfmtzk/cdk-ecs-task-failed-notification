import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_ecs_task_failed_notification.cdk_ecs_task_failed_notification_stack import CdkEcsTaskFailedNotificationStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_ecs_task_failed_notification/cdk_ecs_task_failed_notification_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkEcsTaskFailedNotificationStack(app, "cdk-ecs-task-failed-notification")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
