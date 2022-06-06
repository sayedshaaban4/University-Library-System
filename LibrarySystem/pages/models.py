from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

class addbook(models.Model):
    bookname=models.CharField(max_length=50, null= True, blank=True)
    bookauthor=models.CharField(max_length=50, null= True, blank=True)
    ISBN=models.CharField(max_length=50, null= True, blank=True)
    Year=models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    available = models.BooleanField(null=True, blank=True)
    borrowing_period = models.IntegerField(null=True, blank=True)
    borrower = models.CharField(max_length=50, null= True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.bookname)
        super(addbook, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' %(self.bookname)


class Profile(models.Model):
    x = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    y = [
        ('Admin','Admin'),
        ('Student','Student'),
    ]
    
    name = models.CharField(max_length=50, null= True, blank=True)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=x)
    type = models.CharField(max_length=10, choices=y, null=True, blank=True)
    books = models.ForeignKey(addbook, verbose_name='books', on_delete=models.PROTECT,null=True, blank=True)
    user = models.OneToOneField(User, verbose_name='user', on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return '%s' %(self.name)


