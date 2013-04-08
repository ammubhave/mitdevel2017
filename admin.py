from django.contrib import admin 
from openshift.models import SkillEntry, InterestEntry, WebsiteEntry, ProjectEntry, CommentEntry, VotingEntry, CollaboratorsEntry, BlogEntry

admin.site.register(SkillEntry)
admin.site.register(InterestEntry)
admin.site.register(WebsiteEntry)
admin.site.register(ProjectEntry)
admin.site.register(CommentEntry)
admin.site.register(VotingEntry)
admin.site.register(CollaboratorsEntry)
admin.site.register(BlogEntry)

