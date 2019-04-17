# from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.admin.edit_handlers import StreamFieldPanel
from lanretam.main.blocks import ImageBlock


class HomePage(Page):
    body = StreamField([
        ('text', blocks.RichTextBlock(icon='pilcrow')),
        ('image', ImageBlock()),
        ('table', TableBlock(template='main/blocks/table_block.html')),
        ('table_caption', blocks.CharBlock(icon='fa-thumb-tack')),
        ('sr_text', blocks.TextBlock(
                            required=False,
                            icon='fa-universal-access',
                            label='SR text')),
    ], verbose_name='Page content', blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
