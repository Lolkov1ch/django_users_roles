import django_setup
from main_app.models import User, Role

get_user = User.objects.get(name="Іван")
get_user_2 = User.objects.get(name="Марія")

# u1 = User.objects.create(name="Іван", email="ivan@example.com", role=admin_role)
# u2 = User.objects.create(name="Марія", email="maria@example.com", role=user_role)
# u3 = User.objects.create(name="Олег", email="oleg@example.com", role=Role.objects.get(name="user"))
# u4 = User.objects.create(name="Світлана", email="svitlana@example.com", role=Role.objects.get(name="user"))

get_user.role = Role.objects.get(name="admin")
get_user.name = "Іван (оновлений)"
get_user.save()

get_user_2.delete()