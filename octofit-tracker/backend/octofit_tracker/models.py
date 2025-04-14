from bson import ObjectId
from djongo import models

class User(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()))
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    class Meta:
        db_table = 'user'
    def __str__(self):
        return f"{self.username} ({self.email})"

class Team(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()))
    name = models.CharField(max_length=100)
    members = models.JSONField()
    class Meta:
        db_table = 'team'
    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()))
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    class Meta:
        db_table = 'activity'
    def __str__(self):
        return f"{self.activity_type} by User {self.user}"

class Leaderboard(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()))
    user = models.CharField(max_length=100)
    score = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'
    def __str__(self):
        return f"User {self.user} - Score: {self.score}"

class Workout(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=lambda: str(ObjectId()))
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        db_table = 'workout'
    def __str__(self):
        return self.name
