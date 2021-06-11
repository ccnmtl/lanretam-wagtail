from django.contrib.auth.models import User, Group
from factory.django import DjangoModelFactory
from factory import Sequence, PostGenerationMethodCall, LazyAttribute
from lanretam.main.models import ContentPage, HomePage


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
    username = Sequence(lambda n: 'user%d' % n)
    password = PostGenerationMethodCall('set_password', 'test')
    email = LazyAttribute(lambda u: '%s@example.com' % u.username)


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group


class ContentPageFactory(DjangoModelFactory):
    class Meta:
        model = ContentPage
    title = Sequence(lambda n: 'page {}'.format(n))
    depth = 1
    path = Sequence(lambda n: 'path{}'.format(n))


class HomePageFactory(DjangoModelFactory):
    class Meta:
        model = HomePage
    title = Sequence(lambda n: 'page {}'.format(n))
    depth = 3
    path = Sequence(lambda n: 'path{}'.format(n))
