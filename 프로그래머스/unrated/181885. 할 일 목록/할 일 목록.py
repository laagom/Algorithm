def solution(todo_list, finished):
    return [todo for todo, boolean in zip(todo_list, finished) if boolean != True]