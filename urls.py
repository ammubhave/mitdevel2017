from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'openshift.views.home', name='home'),
    url(r'^members$', 'openshift.views.members', name='members'),
    url(r'^members/(?P<username>[0-9A-Za-z]+)$', 'openshift.views.members_profile', name='members_profile'),
    
    url(r'^accounts/login$', 'django.contrib.auth.views.login'),
    url(r'^accounts/profile/$', 'openshift.views.profile'),
    url(r'^accounts/profile$', 'openshift.views.profile'),
    url(r'^accounts/logout$', 'django.contrib.auth.views.logout'),
    url(r'^accounts/password_reset$', 'django.contrib.auth.views.password_reset'),
    url(r'^accounts/password_reset_confirm/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$', 'django.contrib.auth.views.password_reset_confirm'),
    url(r'^accounts/password_reset_done$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^accounts/password_reset_complete/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^accounts/password_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^accounts/password_change_done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    
    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
