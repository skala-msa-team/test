import unittest

from backend.task_service import TaskService


class TaskServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = TaskService([])

    def test_create_task(self):
        task = self.service.create_task("PR 만들기")

        self.assertEqual("PR 만들기", task["title"])
        self.assertFalse(task["completed"])

    def test_create_task_rejects_blank_title(self):
        with self.assertRaises(ValueError):
            self.service.create_task("   ")

    def test_update_task(self):
        task = self.service.create_task("Review 받기")

        updated = self.service.update_task(task["id"], True)

        self.assertTrue(updated["completed"])

    def test_filter_active_tasks(self):
        first = self.service.create_task("첫 번째")
        self.service.create_task("두 번째")
        self.service.update_task(first["id"], True)

        active = self.service.list_tasks("active")

        self.assertEqual(["두 번째"], [task["title"] for task in active])


if __name__ == "__main__":
    unittest.main()

