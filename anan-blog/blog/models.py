from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField


class BlogCategorie(models.Model):
    category_name = models.CharField(max_length=250, null=False, blank=False)
    category_slug = models.CharField(max_length=250, null=False, blank=False)
    category_order = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "tbl_blog_categories"

    def __str__(self):
        return str(self.category_name)


class BlogKeyword(models.Model):
    keywords_name = models.CharField(max_length=250, null=True, blank=True)
    keywords_slug = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        db_table = "tbl_blog_keywords"

    def __str__(self):
        return str(self.keywords_name)

class Blogs(models.Model):
    authorId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=False, blank=False)
    shortDescription = models.TextField(max_length=300, null=False, blank=False)
    highLights = RichTextField(default="")
    content = models.TextField()
    image = models.ImageField(null=False, blank=False, upload_to='blog')
    categories = models.ForeignKey(BlogCategorie, on_delete=models.CASCADE, null=False, blank=False)
    keywords = models.ManyToManyField(BlogKeyword, default='', blank=True)
    viewCount = models.IntegerField(default=0)
    shareCount = models.IntegerField(default=0)
    status_choices = (
            ('pub', 'Published'),
            ('daf', 'Draft'),
            ('trs', 'Trash'),
        )
    status = models.CharField(max_length=50, choices=status_choices, default='pub')
    dateAdded = models.DateTimeField(auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = "tbl_blogs"

    def __str__(self):
        return str(self.title)

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))
        else:
            return mark_safe('<img src="/media/document/default.jpg" width="50" height="50" />')

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

@receiver(post_delete, sender=Blogs)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)