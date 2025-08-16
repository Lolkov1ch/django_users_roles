import django_setup
from django.contrib.auth.models import User
from tasks.models import Task

user1 = User.objects.create_user(username='ivan', password='1234')
user2 = User.objects.create_user(username='olena', password='1234')

task1 = Task.objects.create(
    title="Написати документацію",
    description="Потрібно описати всі API ендпоінти",
    assigned_to=user1
)

task2 = Task.objects.create(
    title="Зробити тестування",
    description="Пройти всі юніт-тести",
    status="deferred",
    assigned_to=user2
)

task1.status = 'completed'
task1.save()

task2.assigned_to = user1
task2.save()

for task in Task.objects.all():
    print(task.title, task.status, task.assigned_to.username if task.assigned_to else "Немає користувача")
