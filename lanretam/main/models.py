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
