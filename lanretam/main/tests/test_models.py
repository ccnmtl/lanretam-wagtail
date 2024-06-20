from lanretam.main.models import HomePage, ContentPage
from lanretam.main.tests.factories import ContentPageFactory, HomePageFactory
from wagtail.tests.utils import WagtailPageTests


class ContentPageTest(WagtailPageTests):

    def setUp(self):
        self.root = HomePage.add_root(instance=HomePageFactory.build())

        self.module = ContentPageFactory.build()
        self.root.add_child(instance=self.module)

        self.child = ContentPageFactory.build(depth=5)
        self.module.add_child(instance=self.child)

        self.grandchild = ContentPageFactory.build(depth=6)
        self.child.add_child(instance=self.grandchild)

        self.module.depth = 4
        self.module.save()
        self.child.depth = 5
        self.child.save()
        self.grandchild.depth = 6
        self.grandchild.save()

    def test_can_create_content_page(self):
        self.assertCanCreateAt(HomePage, ContentPage)

    def test_sidemenu_module(self):
        sidemenu = self.module.sidemenu()
        self.assertEqual(sidemenu.count(), 2)
        self.assertEqual(sidemenu[0].id, self.child.id)
        self.assertEqual(sidemenu[1].id, self.grandchild.id)

    def test_sidemenu_child(self):
        sidemenu = self.child.sidemenu()
        self.assertEqual(sidemenu.count(), 2)
        self.assertEqual(sidemenu[0].id, self.child.id)
        self.assertEqual(sidemenu[1].id, self.grandchild.id)

    def test_sidemenu_grandchild(self):
        sidemenu = self.grandchild.sidemenu()
        self.assertEqual(sidemenu.count(), 2)
        self.assertEqual(sidemenu[0].id, self.child.id)
        self.assertEqual(sidemenu[1].id, self.grandchild.id)

    def test_module(self):
        self.assertEqual(self.module.module().id, self.module.id)
        self.assertEqual(self.child.module().id, self.module.id)
        self.assertEqual(self.grandchild.module().id, self.module.id)
