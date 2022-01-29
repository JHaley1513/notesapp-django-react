from django.db import models

class NotesApp(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField() # not initialized yet
    # completed: status of a task, always is either completed or not.
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title