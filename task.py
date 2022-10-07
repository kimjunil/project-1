from flytekit import task

# 기본적인 task의 형태
@task()
def write():
  with open("hello_world.txt", "w") as file:
    file.write("Hello World")


# 입력과 출력이 있을 경우 타입을 반드시 명시해줘야합니다.
@task()
def read(path: str) -> str:
  with open(path, "r") as file:
    result = file.readlines()
  return result