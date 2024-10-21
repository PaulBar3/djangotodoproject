from django.db import models

# Create your models here.
class Todo_item(models.Model):
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)


    class Meta:
        ordering = ["id"]
        verbose_name = 'Todo Item'
        verbose_name_plural = 'Todo Items'

    def __str__(self):
        return self.title