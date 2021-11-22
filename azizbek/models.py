from django.db import models
from django.db.models.fields import CharField

class Home(models.Model):
    name = models.CharField(max_length=255)
    greetings_1 = models.CharField(max_length=255)
    greetings_2 = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='picture/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class About(models.Model):
    heading = models.CharField(max_length=255)
    career = models.CharField(max_length=255)
    description = models.TextField()
    resume = models.FileField(upload_to='profile/', blank= True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career


class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=255)
    link = models.URLField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=255)
    percent = models.PositiveIntegerField(default=0, blank=True)

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=255)

    def __str__(self):
        return f'Portfolio {self.id}'