# from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from lanretam.main.blocks import BaseStreamBlock


class HomePage(Page):
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page content",
        blank=True,
        use_json_field=True
        )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    # Limits this page type to only HomePage
    # parent_page_types = []


class ContentPage(Page):
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page content",
        blank=True,
        use_json_field=True
        )

    def sidemenu(self):
        return self.module().get_descendants()

    def module(self):
        if self.depth <= 4:
            return self
        for page in self.get_ancestors():
            if page.depth == 4:
                return page

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
