from django.db import models

from people.models import Person

class ExperienceType(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField()

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.name

class ExperienceItem(models.Model):
    person = models.ForeignKey(Person, related_name='experiences', on_delete=models.CASCADE)
    type = models.ForeignKey(ExperienceType, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    location = models.CharField(max_length=255, blank=True)
    time_period = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        return f'{self.person} at {self.title}'
    
    class Meta:
        ordering = ("type",)

class LineItem(models.Model):
    experience = models.ForeignKey(ExperienceItem, related_name="items", on_delete=models.CASCADE)
    details = models.CharField(max_length=255)
