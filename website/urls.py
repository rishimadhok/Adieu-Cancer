"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

from website.views import hello_world, root_page, random_number

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^helloworld/$', hello_world),
    url(r'^$', root_page),
    url(r'^random/(\d+)/$', random_number),
    url(r'^about/', include('about_us.urls'), name='about'),
    url(r'^contact/', include('contact_us.urls')),
    url(r'^cancer/', include('cancerA_Z.urls')),
    url(r'^blogs/', include('blogs.urls')),
    url(r'^cancerpred/', include('cancer_predictor.urls')),
    url(r'^breastcan/', include('breast_cancer.urls')),
    url(r'^AdieuCancer/', include('cover.urls'), name='AdieuCancer'),
]
