from django.contrib.auth.models import User
from django.db import models
from django.db.models.functions import Upper


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = [Upper('name')]

    def __str__(self):
        return self.name


class TaskStatus(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = [Upper('name')]

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(TaskStatus, default=1, on_delete=models.CASCADE,
                               related_name='status')
    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='creator')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='assigned_to')
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)

    def __str__(self):
        return self.name
