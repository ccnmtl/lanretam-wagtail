from django.contrib.auth.models import User, Group
import factory
from lanretam.main.models import ContentPage, HomePage


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: 'user%d' % n)
    password = factory.PostGenerationMethodCall('set_password', 'test')
    email = factory.LazyAttribute(lambda u: '%s@example.com' % u.username)


class GroupFactory(factory.DjangoModelFactory):
    class Meta:
        model = Group


class ContentPageFactory(factory.DjangoModelFactory):
    class Meta:
        model = ContentPage
    title = factory.Sequence(lambda n: 'page {}'.format(n))
    depth = 1
    path = factory.Sequence(lambda n: 'path{}'.format(n))


class HomePageFactory(factory.DjangoModelFactory):
    class Meta:
        model = HomePage
    title = factory.Sequence(lambda n: 'page {}'.format(n))
    depth = 3
    path = factory.Sequence(lambda n: 'path{}'.format(n))
