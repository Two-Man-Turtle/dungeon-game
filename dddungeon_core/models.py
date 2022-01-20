from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    score = models.ForeignKey('Score', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"<Player username={self.user.username}>"

class Score(models.Model):
    monster_kills = models.IntegerField(null=True, blank=True)
    dungeon_depth = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"<Score: monster_kills={self.monster_kills} dungeon_depth={self.dungeon_depth}"
