import django_setup
from blog.models import Post, Comment
from django.utils import timezone

post1 = Post.objects.create(
    title="Мій перший пост",
    content="Це текст мого першого посту.",
    published_at=timezone.now()
)

post1.add_comment(author="Олександр", text="Цікаво, дякую за пост!")
post1.add_comment(author="Марія", text="Дуже корисна інформація!")

post2 = Post.objects.create(
    title="Другий пост",
    content="Тут трохи іншого змісту.",
    published_at=timezone.now()
)

for post in Post.objects.all():
    print(f"Пост: {post.title}")
    print(f"Зміст: {post.content}")
    print(f"Опубліковано: {post.published_at}")
    print("Коментарі:")
    for comment in post.comments.all(): # type: ignore
        print(f"  - {comment.author}: {comment.text} ({comment.created_at})")
    print("-" * 40)