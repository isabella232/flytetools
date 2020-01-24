from __future__ import absolute_import
from __future__ import print_function

from flytekit.sdk.tasks import (
    dynamic_task,
)
from flytekit.sdk.workflow import workflow_class

from flytetester.app.workflows.failing_workflows import retryer


@dynamic_task(cpu_request="200m", cpu_limit="200m", memory_request="500Mi", memory_limit="500Mi", retries=5)
def sample_batch_task_cachable(wf_params):
    yield retryer()


@workflow_class
class RetryableDynamicWorkflow(object):
    dynamic_task = sample_batch_task_cachable()