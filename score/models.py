from django.db import models

class game(models.Model):
    gamename = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    keio1 = models.CharField(max_length=100)
    keio2 = models.CharField(max_length=100)
    e1 = models.CharField(max_length=100)
    e2 = models.CharField(max_length=100)
     
    def __str__(self):
        return '<game:id=' + str(self.id) + ', ' + \
            self.gamename + '(' + str(self.score) + ')>'

class result(models.Model):
    gameid = models.IntegerField()
    position = models.IntegerField()
    playername = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    before = models.IntegerField()
    course = models.IntegerField()
    
    def __str__(self):
          return str(self.playername) + str(self.result)
    
 
   