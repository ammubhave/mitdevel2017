from django.contrib import admin
from openshift.models import SkillEntry, InterestEntry, WebsiteEntry

admin.site.register(SkillEntry)
admin.site.register(InterestEntry)
admin.site.register(WebsiteEntry)

