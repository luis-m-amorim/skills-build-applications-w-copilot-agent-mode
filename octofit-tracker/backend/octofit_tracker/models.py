from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    class Meta:
        db_table = 'user'
    def __str__(self):
        return f"{self.name} ({self.email})"

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField()
    class Meta:
        db_table = 'team'
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    class Meta:
        db_table = 'activity'
    def __str__(self):
        return f"{self.activity_type} by User {self.user}"

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    score = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'
    def __str__(self):
        return f"User {self.user} - Score: {self.score}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        db_table = 'workout'
    def __str__(self):
        return self.name
