import pytest
from django.contrib.auth.models import User

from blog.models import Post


@pytest.mark.django_db
def test_post():

    user_1 = User()
    user_1.save()

    post = Post(author=user_1, title="greetings", text="Hello World!")
    post.publish()
    print(post)
