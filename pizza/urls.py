"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import oauth2_provider.views as oauth2_views
from apps.api.views import custom_token_views
from rest_framework.urlpatterns import format_suffix_patterns

from apps.cms import views
from django.conf.urls import url

# admin settings
admin.autodiscover()
admin.site.site_header = 'PIZZA - CMS'
admin.site.site_title = 'PIZZA | CMS'
admin.site.site_url = None  # Removes the 'View Site' link

urlpatterns = [
    #url(r'^login/$', views.custom_login_view, name='login'),
    #path('oauth/token', oauth2_views.TokenView.as_view(), name="token"),
    path('oauth/token', custom_token_views.CustomTokenView.as_view()),
    path('api/', include('apps.api.urls')),
    path('', admin.site.urls),
    path('cms/', admin.site.urls)
]

