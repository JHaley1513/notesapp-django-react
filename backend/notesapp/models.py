from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField() # not initialized yet

    def _str_(self):
        return self.title