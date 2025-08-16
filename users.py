import django_setup
from main_app.models import User, Role

admin_role = Role.objects.create(name="admin")
user_role = Role.objects.create(name="user")

print(User.objects.all())
