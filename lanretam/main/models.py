# from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
# from wagtail.core import blocks
# from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.admin.edit_handlers import StreamFieldPanel
from lanretam.main.blocks import BaseStreamBlock


class HomePage(Page):
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page content",
        blank=True
        )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
    # Limits this page type to only HomePage
    # parent_page_types = []


class ContentPage(Page):
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page content",
        blank=True
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
        StreamFieldPanel('body'),
    ]
