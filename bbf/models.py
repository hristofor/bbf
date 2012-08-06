from django.db import models

# Create your models here.
   
class Team(models.Model):
    
    teamname = models.CharField(max_length=765, blank=True) 
    established = models.DateField(null=True, blank=True) 
    memberscount = models.IntegerField(null=True, blank=True)
    logo = models.CharField(max_length=765, blank=True)
    dateterminated = models.DateField(null=True, blank=True)
    parentteam = models.ForeignKey('self', null=True, blank=True)
    
    def __unicode__(self):
        return self.teamname        
   
class DivisionManager(models.Manager):
    #use_for_related_fields = True
    def get_query_set(self):
        query_set = super(DivisionManager, self).get_query_set()

        for ut in query_set:
            if ut.sexfemale:
                ut.division = 'female'
            else:
                ut.division = 'male'
          
        return query_set

class File(models.Model):    
    playername = models.CharField(max_length=765, blank=True) 
    sexfemale = models.IntegerField(null=True, blank=True) 
    birthdate = models.DateField(null=True, blank=True) 
    startedbowling = models.DateField(null=True, blank=True) 
    lastteam = models.ForeignKey(Team, null=True, blank=True) 
    card = models.CharField(max_length=765, blank=True) 
    
    division = ''
    
    objects = DivisionManager()
    #divisions = DivisionManager()
    
    def get_division(self):
        #returns division
        if self.sexfemale == 1:
            div = 'female'
        else:
            div = 'male'
        return div
    
    division_type = property(get_division)#tva trqq da e property 
    
    def __unicode__(self):
        return self.playername

class Hall(models.Model):
    
    name = models.CharField(max_length=765, blank=True) 
    city = models.CharField(max_length=765, blank=True) 
    manifacturer = models.CharField(max_length=765, blank=True) 
    lanes = models.IntegerField(null=True, blank=True) 
    machine = models.CharField(max_length=765, blank=True)
    dateopened = models.DateField(null=True, blank=True)
    active = models.NullBooleanField()
    logo = models.CharField(max_length=765, blank=True)
    
    def __unicode__(self):
        return self.name