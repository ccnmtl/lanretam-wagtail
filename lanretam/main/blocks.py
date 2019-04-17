from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import CharBlock, StructBlock


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
    image_file = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = 'image'
        template = "main/blocks/image_block.html"
