from django.db import models

class Men(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    rating = models.IntegerField()
    status = models.IntegerField(default=0)
    z_or_isp = models.IntegerField()

    def __str__(selft):
        return self.login + ": " + self.name + " " + self.last_name

class Task(models.Model):
    description = models.CharField(max_length=500)
    time = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    executor = models.IntegerField()
    client = models.ForeignKey(Men)

    def __str__(selft):
        return self.client + "-->" + self.executor + ": " +self.description[:10]

class Perk(models.Model):
    name = models.CharField(max_length=200)

    def __str__(selft):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(selft):
        return self.name

class PdCategory(models.Model):
    cat = models.ForeignKey(Category)
    perk = models.ForeignKey(Perk)

    def __str__(selft):
        return self.cat + "-->" + self.perk

class UserPerk(models.Model):
    user = models.ForeignKey(Men)
    perk = models.ForeignKey(Perk)
    percent = models.IntegerField(default=0)

    def __str__(selft):
        return self.user + "-->" + self.perk + ": " + self.percent + "%"
