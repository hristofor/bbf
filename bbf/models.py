from django.db import models

# Create your models here.
   
class Team(models.Model):
    teamid = models.AutoField(primary_key=True) 
    teamname = models.CharField(max_length=765, blank=True) 
    established = models.DateTimeField(null=True, blank=True) 
    memberscount = models.IntegerField(null=True, blank=True)
    logo = models.CharField(max_length=765, blank=True)
    
    def __unicode__(self):
        return self.teamname
        
    
class File(models.Model):
    playerid = models.AutoField(primary_key=True) 
    playername = models.CharField(max_length=765, blank=True) 
    sexfemale = models.IntegerField(null=True, blank=True) 
    birthdate = models.DateTimeField(null=True, blank=True) 
    startedbowling = models.DateTimeField(null=True, blank=True) 
    lastteam = models.ForeignKey(Team, to_field='teamid', null=True, blank=True) 
    card = models.CharField(max_length=765, blank=True) 
    
    def __unicode__(self):
        return self.playername

class Hall(models.Model):
    hallid = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=765, blank=True) 
    city = models.CharField(max_length=765, blank=True) 
    manifacturer = models.CharField(max_length=765, blank=True) 
    lanes = models.IntegerField(null=True, blank=True) 
    machine = models.CharField(max_length=765, blank=True)
    dateopened = models.DateTimeField(null=True, blank=True)
    active = models.NullBooleanField()
    logo = models.CharField(max_length=765, blank=True)
    
    def __unicode__(self):
        return self.name