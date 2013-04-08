from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'openshift.views.home', name='home'),
    url(r'^projects$', 'openshift.views.projects', name='projects'),
    url(r'^projects/add$', 'openshift.views.projects_add', name='projects_add'),
    url(r'^projects/delete$', 'openshift.views.projects_delete', name='projects_delete'),
    url(r'^projects/update$', 'openshift.views.projects_update', name='projects_update'),
    url(r'^comments/load$', 'openshift.views.comments_load', name='comments_load'),
    url(r'^comments/add$', 'openshift.views.comments_add', name='comments_add'),
    url(r'^comments/delete$', 'openshift.views.comments_delete', name='comments_delete'),
    
    url(r'^members$', 'openshift.views.members', name='members'),
    url(r'^members/(?P<username>[0-9A-Za-z]+)$', 'openshift.views.members_profile', name='members_profile'),
    
    url(r'^accounts/login/?$', 'django.contrib.auth.views.login'),
    url(r'^accounts/profile/?$', 'openshift.views.profile'),    
    url(r'^accounts/logout$', 'django.contrib.auth.views.logout'),
    url(r'^accounts/password_reset$', 'django.contrib.auth.views.password_reset'),
    url(r'^accounts/password_reset_confirm/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$', 'django.contrib.auth.views.password_reset_confirm'),
    url(r'^accounts/password_reset_done$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^accounts/password_reset_complete/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^accounts/password_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^accounts/password_change_done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    
    url(r'^accounts/profile/skills/add$', 'openshift.views.add_skill', name='add_skill'),
    url(r'^accounts/profile/skills/remove$', 'openshift.views.remove_skill', name='remove_skill'),
    url(r'^accounts/profile/interests/add$', 'openshift.views.add_interest', name='add_interest'),
    url(r'^accounts/profile/interests/remove$', 'openshift.views.remove_interest', name='remove_interest'),    
    url(r'^accounts/profile/websites/add$', 'openshift.views.add_website', name='add_website'),
    url(r'^accounts/profile/websites/remove$', 'openshift.views.remove_website', name='remove_website'),    
    
    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
