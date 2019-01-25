from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=50)


    def __str__(self):
        return "%d - %s %s" %(self.id, self.first_name, self.last_name)

class Author(Person):
    biography = models.TextField()


class Post(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=50, null=True, blank=True)
    authors = models.ManyToManyField(Author)
    text = models.TextField()


    def __str__(self):
        return "%d - %s" %(self.id, self.title)