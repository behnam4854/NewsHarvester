
from django.db import models

class Headline(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField() 
    url = models.URLField()
    published_date = models.DateTimeField()
    scraped_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Source(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Sentiment(models.Model):
    headline = models.ForeignKey(Headline, on_delete=models.CASCADE)
    sentiment = models.CharField(max_length=10) # positive, negative
    confidence = models.FloatField()

    def __str__(self):
        return f"{self.headline.title} - {self.sentiment}"