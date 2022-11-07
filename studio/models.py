from dataclasses import Field
from django.db import models
from modelcluster.fields import ParentalKey
import uuid
from wagtail.models import Page, Orderable
from ckeditor.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index

# Create your models here.
# About page models 
class About(Page):
    max_count = 1
    creator_name = models.CharField(blank = True, max_length = 100)
    creator_prof = models.CharField(blank = True, max_length = 200)
    creator_disc = RichTextField(blank = True, max_length = 5000)

    content_panels = Page.content_panels + [
        FieldPanel('creator_name'),
        FieldPanel('creator_prof'),
        FieldPanel('creator_disc'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class AboutPageImage(Orderable):
    max_count = 1
    page = ParentalKey(About, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE,
    )
    panels = [
        FieldPanel('image'),
    ]


# Blog page models
class BlogIndexPage(Page):
    intro = RichTextField(blank=True,  max_length = 100)

    
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

class BlogPage(Page):
    blog_title = models.CharField(blank=True,  max_length = 100)
    blog_date = models.DateField("Post date")
    blog_description = RichTextField(blank=True, max_length = 5000)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('blog_title'),
        FieldPanel('blog_date'),
        FieldPanel('blog_description'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class BlogPageImage(Orderable):
    max_count = 1
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE,
    )
    panels = [
        FieldPanel('image'),
    ]




# Work Page 
class WorkIndexPage(Page):
    intro = RichTextField(blank=True)

class WorkPage(Page):
    work_name = models.CharField(max_length=250,null=True)
    work_subtitle = models.CharField(max_length=250,null=True)
    work_description=RichTextField(max_length=5000,null=True)

    def thumbnail_image(self):
        gallery_item = self.thumbnail.first()
        if gallery_item:
            return gallery_item.thumbnail
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('work_name'),
        FieldPanel('work_subtitle'),
        FieldPanel('work_description'),
        InlinePanel('gallery_images', label="Gallery images"),
        InlinePanel('thumbnail', label="Thumbnail images"),
    ]
    
class WorkDetailsPagethumbnailImage(Orderable):
 
    page = ParentalKey(WorkPage, on_delete=models.CASCADE, related_name='thumbnail')

    thumbnail= models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE,related_name='thumbnail',blank=True
    )
    panels = [
        FieldPanel('thumbnail'),

    ]


class workDetailsPageGalleryImage(Orderable):
 
    page = ParentalKey(WorkPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE,
    )
    panels = [
        FieldPanel('image')

    ]
