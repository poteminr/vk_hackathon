from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse

# Create your models here.

def rename_photo(instance,filename):
    return f"media/userphotos/{instance.username}.png"
class CustomUser(AbstractUser):

    name = models.CharField(max_length=200, default="None")
    additionalinfo = models.TextField(blank=True, max_length=1000, help_text="Enter a Additional Information")
    is_local_admin = models.BooleanField(default=False)
    date_reg = models.DateTimeField(auto_now_add=True)

    photo = models.ImageField(
        upload_to = rename_photo ,
        default = 'media/photos/no_photo.jpg'
    )
    
    def get_absolute_url(self):
        return reverse('user_detail', kwargs={"id": self.id})
    def get_update_url(self):
        return reverse('user_update', kwargs={"id": self.id})

    def get_rating(self):
        rating = 0
        n = 0

        for rew in self.reviews.all():
            n += 1
            rating += rew.rating
        if n > 0:
            return rating/n
        return 0
    def get_color(self):
        rating = self.get_rating()

        if rating > 4:
            return "#6ef07b"
        elif rating > 3:
            return "#eba4c5"
        elif rating > 2:
            return "#b55c86"
        elif rating > 1:
            return "#ff004c"
        return "#000000"

    def get_review_url(self):
        return reverse('user_review', kwargs={"id": self.id})

    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)




class Review(models.Model):
    user = models.ForeignKey(CustomUser, related_name = "reviews", on_delete=models.SET_NULL,null=True)
    author = models.ForeignKey(CustomUser, related_name = "created_reviews", on_delete=models.SET_NULL,null=True)
    rating = models.IntegerField(help_text="Рейтинг отзыва")

    text = models.TextField(max_length=1000, help_text="Enter text")
    
    created_date = models.DateTimeField(auto_now_add=True)

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


    def __str__(self):
        try:
            return f"{self.user.username} : {self.rating}"
        except:
            return f"NONEUSER : {self.rating}"