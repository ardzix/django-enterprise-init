
"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


from django.urls import path
from django.contrib.flatpages import views


class RedirectVerifyView(RedirectView):
    query_string = True


urlpatterns = [
    url(r'^superuser/', include(('enterprise.apps.superuser.urls', 'superuser'), namespace='superuser')),
    url(r'^authentication/login/', RedirectView.as_view(url='/login/')),
    url(r'^authentication/email_verify/',
        RedirectVerifyView.as_view(url='/create-password/')),
    url(r'^authentication/', include(('enterprise.apps.authentication.urls',
                                      'authentication'), namespace='authentication')),
    url(r'^oauth/', include('social_django.urls', namespace='social'))
]


if settings.DEBUG:
    from django.contrib import admin
    from django.conf.urls.static import static

    admin.autodiscover()
    urlpatterns.append(url(r'^admin/', admin.site.urls))
    urlpatterns.append(
        url(r'^account/login/', RedirectView.as_view(url='/authentication/')),)
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
