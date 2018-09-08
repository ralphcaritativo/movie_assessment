from django.db import models


class Movie(models.Model):

    STATUS_CHOICES = (
    (0, False),
    (1, True),
    )

    title       =   models.CharField(max_length=100)
    is_active   =   models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at  =   models.DateTimeField(auto_now_add=True)
    updated_at  =   models.DateTimeField(auto_now=True)
    like_total  =   models.IntegerField(default=0)

    def __str__(self):
        return self.title
