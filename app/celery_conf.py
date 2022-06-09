# Celery configuration file

broker_url = "redis://localhost:16379/0"
result_backend = "redis://localhost:16379/1"

task_serializer = "json"
accept_content = ["json"]
result_serializer = "json"

imports = ("app.tasks",)

# NOTE: this is important to make this trick work
worker_max_tasks_per_child = 1
