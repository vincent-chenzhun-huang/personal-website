from django.db import models


#TODO: Create a migration
#TODO: Migrate
#TODO: Add to the admin

class Project(models.Model):
    name = models.CharField(max_length=200)
    language = models.TextField(max_length=200)
    date = models.DateTimeField()
    intro = models.TextField()
    src = models.URLField()

    def date_pretty(self):
        return self.date.strftime('%b %e %Y')

    def __str__(self):
        return self.name 

