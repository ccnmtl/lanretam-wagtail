# from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel
from lanretam.main.blocks import ImageBlock


class HomePage(Page):
    page_body = StreamField([
        ('text', blocks.RichTextBlock(icon='pilcrow')),
        ('image', ImageBlock()),
        ('sr_text', blocks.TextBlock(
                            required=False,
                            icon='fa-universal-access',
                            label='SR text')),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('page_body'),
    ]
