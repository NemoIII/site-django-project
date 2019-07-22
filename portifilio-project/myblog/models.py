from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to="images/")
	
	def __str__(self):
		return self.title


	def sumary(self):
		return self.body[:90]


	def pub_date_pretty(self):
		return self.pub_date.strftime('%B %e %Y')
		