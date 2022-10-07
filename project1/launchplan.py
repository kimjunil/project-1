from flytekit import LaunchPlan
import workflow

# workflow를 실행하기위한 LaunchPlan을 등록할 수 있습니다.
launchplan = LaunchPlan.get_or_create(
    name="single_launch_plan",
    workflow=workflow.chain_workflow
)
