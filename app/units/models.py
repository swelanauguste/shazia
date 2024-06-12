from django.db import models
from django.urls import reverse


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Condition(TimeStampMixin):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Location(TimeStampMixin):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Unit(TimeStampMixin):
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    condition1 = models.ForeignKey(
        Condition,
        on_delete=models.CASCADE,
        related_name="+",
        null=True,
        verbose_name="condition",
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    remarks = models.TextField()
    
    class Meta:
        ordering = ['description']

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.description
