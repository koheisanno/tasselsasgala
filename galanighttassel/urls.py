"""galanight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from tickets import views as tickets_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^payment_process/$', tickets_views.payment_process, name='payment_process' ),
    url(r'^payment_done/$', tickets_views.payment_done, name='payment_done'),
    url(r'^payment_canceled/$', tickets_views.payment_canceled, name='payment_canceled'),
    path('', include('event.urls')),
    path('tickets/', tickets_views.buy, name="buy"),
    path('thankyou/', tickets_views.thankyou, name='thankyou'),
    path('<str:userid>/', tickets_views.profile, name='profile'),
]