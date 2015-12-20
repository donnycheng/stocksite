from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank = True,null =True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def  __str__(self):
		return self.title

		
class Stock(models.Model):
	sn = models.TextField(max_length=6)
	name = models.TextField(max_length=20)

class TopStock(models.Model):

    class Meta:
        verbose_name = "TopStock"
        verbose_name_plural = "TopStocks"

    top_date = models.DateField()
    top_sn = models.ForeignKey(Stock)
    top_period = models.TextField(max_length=20)
    top_ifopen = models.TextField(max_length=20)
    top_howmany = models.TextField(max_length=20)
    top_moneystatus = models.TextField(max_length=50)

    def __str__(self):
        return slef.top_sn
        
    
    
