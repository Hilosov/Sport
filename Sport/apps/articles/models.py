import datetime
from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse 



class Article(models.Model):
	article_title = models.CharField('Название статьи', max_length = 200)
	article_text = models.TextField('Текст статьи')
	pub_date = models.DateTimeField('Data')
	author = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)

	def __str__(self):
		return self.article_title


	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'


class Comment(models.Model):
	article =  models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)
	comment_text = models.CharField('Text', max_length = 200)

	def __str__(self):
		return self.author_name.username

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Коментарии'


# ______________________________________________________________________________________

