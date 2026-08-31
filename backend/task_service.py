from copy import deepcopy


INITIAL_TASKS = [
    {"id": 1, "title": "Issue 템플릿 확인하기", "completed": True},
    {"id": 2, "title": "작업 Branch 만들기", "completed": False},
]


class TaskService:
    def __init__(self, tasks=None):
        self._tasks = deepcopy(tasks if tasks is not None else INITIAL_TASKS)
        self._next_id = max((task["id"] for task in self._tasks), default=0) + 1

    def list_tasks(self, status="all"):
        if status == "completed":
            return [task.copy() for task in self._tasks if task["completed"]]
        if status == "active":
            return [task.copy() for task in self._tasks if not task["completed"]]
        return [task.copy() for task in self._tasks]

    def create_task(self, title):
        normalized_title = str(title or "").strip()
        if not normalized_title:
            raise ValueError("할 일 제목을 입력해 주세요.")

        task = {"id": self._next_id, "title": normalized_title, "completed": False}
        self._tasks.append(task)
        self._next_id += 1
        return task.copy()

    def update_task(self, task_id, completed):
        for task in self._tasks:
            if task["id"] == task_id:
                task["completed"] = bool(completed)
                return task.copy()
        raise KeyError("존재하지 않는 할 일입니다.")

