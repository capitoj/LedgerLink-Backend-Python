"""ucsf_dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

#from library.forms import BookForm
from library.forms import BookForm
from library.models import Book, Author, Category
from xf_crud.xf_crud_helpers import crudurl

urlpatterns = [
    url(r'^', include('this_dashboard.urls')),
    #url(r'^dashboards/', include('uc_dashboards.urls')),
    url(r'^dashboards/login$', 'django.contrib.auth.views.login'),
    url(r'^', include('uc_dashboards.urls')),
    url(r'^admin/', admin.site.urls),
]

#if settings.DEBUG:
#    import debug_toolbar
#    urlpatterns += [
#        url(r'^__debug__/', include(debug_toolbar.urls)),
#    ]


urlpatterns += crudurl("library", "book", Book, BookForm)
urlpatterns += crudurl("library", "author", Author, None)
urlpatterns += crudurl("library", "category", Category, None)

