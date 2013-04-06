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
