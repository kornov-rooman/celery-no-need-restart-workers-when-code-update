import celery


@celery.shared_task
def say_hello():
    from app.tasks_impl.main import impl_say_hello
    return impl_say_hello()
