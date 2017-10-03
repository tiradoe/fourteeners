from django.conf.urls import patterns, url
from apps.accounts import views

urlpatterns = patterns('',
    url(r'^create/', views.create, name='create'),

    url(r'^login/$', 'django.contrib.auth.views.login',{
            'template_name': 'accounts/login.html',
            'extra_context': { 'hide_navlinks': True }
        }, name='login'),

    url(r'^logout/$', 'django.contrib.auth.views.logout', {
            'template_name': 'accounts/logout.html',
            'extra_context': { 'hide_navlinks': True },
        }, name='logout'),

    url(r'^password-change/$', 'django.contrib.auth.views.password_change', {
            'template_name': 'accounts/password_change_form.html',
            'post_change_redirect': '/accounts/password-changed',
        }, name='password_change'),

    url(r'^password-changed/$', 'django.contrib.auth.views.password_change_done', {
            'template_name': 'accounts/password_change_done.html'
        }, name='password_change_done'),

    url(r'^profile/', views.profile, name='profile'),
    url(r'^create-profile/', views.new_profile, name='new_profile'),
    url(r'^settings/', views.settings, name='settings'),
    url(r'^delete/', views.delete, name='delete'),
)
