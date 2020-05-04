from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title= models.CharField(max_length=1000)
    pubdate = models.DateTimeField()
    post = models.TextField()

    def summarize(self):
        return self.post[:100]
    def pubdate_nice(self):
        return self.pubdate.strftime('%b %e %Y')
