from uuid import UUID
from typing import List
import dataclasses
import winter


@dataclasses.dataclass
class Todo:
    id: UUID
    title: str
    description: str = ""


todos: List[Todo] = [
    Todo(UUID('11e7f524-8729-4286-81c4-991a10f408c1'), "Just a test task"),
    Todo(UUID('2b892f00-2b44-4351-9d18-f6b19c1d6d42'), "Do something wonderful today, good luck!"),
    Todo(UUID('333a2af4-4d24-446b-9024-95c477a25e93'), "The task is something about very important"),
    Todo(UUID('43392dc0-3c93-4955-951e-7b836a58cfc4'), "Just do it"),
]


@winter.web.no_authentication
class TodoAPI:
    @winter.route_post('todos/')
    @winter.request_body('todo')
    def create_todo(self, todo: Todo):
        todos.append(todo)

    @winter.route_post('todos/{todo_id}/close/')
    def close_todo(self, todo_id: UUID):
        global todos
        todos = [todo for todo in todos if todo.id != todo_id]

    @winter.route_get('todos/')
    def get_todo_list(self) -> List[Todo]:
        return todos
