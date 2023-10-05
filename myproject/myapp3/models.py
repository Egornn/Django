from django.db import models
from collections import Counter

# Create your models here.

class Coin(models.Model):
    is_eagle = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Side: {self.is_eagle}, time: {self.create_at}'

    @staticmethod
    def counter(n: int):
        coins = Coin.objects.order_by('-create_at')[: n]
        coins_dict = {'Head': 0, 'Tail': 0}
        for coin in coins:
            if coin.is_eagle == 'Head':
                coins_dict['Head'] += 1
            else:
                coins_dict['Tail'] += 1
        return coins_dict


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.CharField(max_length=300)
    birthdate = models.DateField()

    def fullname(self):
        return f'{self.firstname} {self.lastname}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    create_at = models.DateField(auto_now_add=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    count_views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)


class Comment(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    create_at = models.DateField(auto_now_add=True)
    change_at = models.DateField(auto_now_add=True)
