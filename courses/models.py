from django.db import models
from django.urls import reverse


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title


class Course(models.Model):
    # owner = models.ForeignKey(User,
    #                           related_name='courses_created',
    #                           on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,
                                related_name='courses',
                                on_delete=models.CASCADE)
    # students = models.ManyToManyField(User)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']
    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course,
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    editor= models.TextField(blank=True)
    def __str__(self):
        return self.title

# class Content(models.Model):
#
#     module = models.ForeignKey(Module,
#                                related_name='contents',
#                                on_delete=models.CASCADE)
#     title = models.CharField(max_length=250)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     content = models.TextField()
#     file = models.FileField(upload_to='files')
#     image = models.ImageField(upload_to='images')
#     editor = models.URLField()
#
#     def __str__(self):
#         return self.title