from django.contrib import admin
from openshift.models import SkillEntry, InterestEntry, WebsiteEntry, ProjectEntry, CommentEntry

admin.site.register(SkillEntry)
admin.site.register(InterestEntry)
admin.site.register(WebsiteEntry)
admin.site.register(ProjectEntry)
admin.site.register(CommentEntry)

