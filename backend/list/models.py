from django.db import models

from django.conf import settings
from django.utils import timezone
from django.urls import reverse
import os
from django.conf import settings
from django.utils.text import slugify
from django.core.exceptions import PermissionDenied

# Create your models here.

def rename_post_image(instance, filename):
    return f'media/photos/{instance.title}-{instance.created_date}.png'

class Post(models.Model):
    title = models.CharField(max_length=200, db_index = True)

    slug = models.SlugField(max_length=150, unique=True, blank=True )

    text = models.TextField(max_length=1000, help_text="Enter text", blank=True, null=True, db_index=True)
    created_date = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to = rename_post_image, default = 'media/photos/no_photo.jpg')
    

    employer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="posts",
        on_delete=models.CASCADE,
        null=True
    )

    cost = models.IntegerField(help_text="Enter price")

    def have_access(self, user, raise_403 = True):
        if self.employer != user and not user.is_staff:
            if raise_403:
                raise PermissionDenied() 
            else:
                return False

        return True

    def how_long_ago(self):
        diff = timezone.now() - self.created_date
        sec = diff.seconds
        days = sec // 60 // 60 // 24 
        sec %= 60 * 60 * 24
        hours = sec // 60 // 60
        sec %= 60 * 60
        minutes = sec // 60
        sec %= 60
        
        if days:
            return f"{days} days {hours} ago"
        elif hours:
            return f"{hours} hours {minutes} minutes ago"
        elif minutes:
            return f"{minutes} minutes {sec} sec ago"
        else:
            return f"{sec} sec ago"

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"slug": self.slug})
    def get_delete_url(self):
        return reverse('post_delete', kwargs={"slug" : self.slug})


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title + "-" + str(timezone.now()))
        super().save(*args, **kwargs)


