from django.db import models

class Tag(models.Model) :
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    tags = models.ManyToManyField(Tag,related_name='news')
    source = models.CharField(max_length = 100)
     
    def __str__(self): 
        return self.title
    
