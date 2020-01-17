from django.db import models

from members.models import User


class PhotoBook(models.Model):

    class Meta:
        ordering = ['-created_date']

    book_name = models.CharField(max_length=100, default='무제')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)


class Page(models.Model):
    book = models.ForeignKey(PhotoBook, on_delete=models.CASCADE)
    pagenumber = models.PositiveIntegerField(auto_created=True)


class Photo(models.Model):
    photo_page = models.ForeignKey(Page, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/')