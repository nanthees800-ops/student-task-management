class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, student_name, student_id, title):
        if not student_name.strip():
            raise ValueError("Student name cannot be empty")
        if not title.strip():
            raise ValueError("Task title cannot be empty")

        task = {
            "id": self.next_id,
            "student_name": student_name,
            "student_id": student_id,
            "title": title,
            "status": "Pending"
        }
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self):
        return self.tasks

    def get_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        raise ValueError("Task not found")

    def update_status(self, task_id, status):
        if status not in ["Pending", "Completed"]:
            raise ValueError("Invalid status")
        task = self.get_task(task_id)
        task["status"] = status
        return task

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        self.tasks.remove(task)
        return {"message": "Task deleted successfully"}

    def search_by_student(self, student_id):
        return [
            task for task in self.tasks
            if task["student_id"] == student_id
        ]
