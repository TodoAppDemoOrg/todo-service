from uuid import UUID, uuid4
from typing import List
import dataclasses
import winter


@dataclasses.dataclass
class Todo:
    id: UUID
    title: str
    description: str = ""


todos: List[Todo] = [
    Todo(uuid4(), "Just a test task"),
    Todo(uuid4(), "Do something wonderful today, good luck!"),
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
