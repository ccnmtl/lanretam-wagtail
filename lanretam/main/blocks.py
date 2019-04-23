from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import (CharBlock, TextBlock, RichTextBlock,
                                 StructBlock, StreamBlock)
from wagtail.contrib.table_block.blocks import TableBlock


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
    image_file = ImageChooserBlock(required=True)
    caption = CharBlock(
                        help_text='Caption for the image',
                        required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = 'image'
        template = "main/blocks/image_block.html"


class MapBlock(StructBlock):
    """
    Custom `StructBlock` to place Lanretam interactive map in page content
    """
    map_title = CharBlock(required=False)

    class Meta:
        icon = 'fa-map-o'
        template = "main/blocks/map_block.html"


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize for content body
    """
    text = RichTextBlock(icon='pilcrow')
    image = ImageBlock()
    table_caption = CharBlock(
                        required=False,
                        help_text='Table caption',
                        icon='fa-thumb-tack')
    table = TableBlock(template='main/blocks/table_block.html')
    sr_text = TextBlock(
                        required=False,
                        icon='fa-universal-access',
                        label='SR text')
    map_block = MapBlock()
