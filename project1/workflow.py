from flytekit import workflow
from flytekit.core.node_creation import create_node
import task

# 작업간 데이터 전달을 argument로 하지 않는 경우 create_node 메소드를 이용합니다.
@workflow
def chain_workflow() -> str:
    write_node = create_node(task.write)
    read_node = create_node(task.read, path="hello_world.txt")

    write_node >> read_node

    return read_node.o0