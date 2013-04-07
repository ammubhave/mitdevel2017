from django.db import models
from django.contrib.auth.models import User

#class UserProfile(models.Model):
 #   user = models.OneToOneField(User)
  #  tag_line = models.TextField(blank=True)
    # Other fields here
    #accepted_eula = models.BooleanField()
    #favorite_animal = models.CharField(max_length=20, default="Dragons.")
    
class SkillEntry(models.Model):
    user = models.ForeignKey(User)
    skill_name = models.TextField()
    
    STUDENT = 0
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3
    PROFICIENCY_CHOICES = (
        (STUDENT, 'Student'),
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    )
    proficiency = models.IntegerField(choices=PROFICIENCY_CHOICES)
    
    def __unicode__(self):
        return "{0} - {1} - {2}".format(self.user.username, self.skill_name, self.proficiency)

  
class InterestEntry(models.Model):
    user = models.ForeignKey(User)
    interest_name = models.TextField()
    
    NOT_MUCH_INTERESTED = 1
    INTERESTED = 2
    VERY_INTERESTED = 3
    LEVEL_CHOICES = (
        (NOT_MUCH_INTERESTED, 'Not much Interested'),
        (INTERESTED, 'Interested'),
        (VERY_INTERESTED, 'Very Interested'),
    )
    level = models.IntegerField(choices=LEVEL_CHOICES)
    
    def __unicode__(self):
        return "{0} - {1} - {2}".format(self.user.username, self.interest_name, self.level)

class WebsiteEntry(models.Model):
    user = models.ForeignKey(User)
    website_url = models.TextField()
 
    WORK = 1
    PERSONAL = 2

    CLASSIFICATION_CHOICES = (
        (WORK, 'Work'),
        (PERSONAL, 'Personal'),
    )
    classification = models.IntegerField(choices=CLASSIFICATION_CHOICES)
    
    def __unicode__(self):
        return "{0} - {1} - {2}".format(self.user.username, self.website_url, self.classification)
