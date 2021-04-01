"""fitproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.conf.urls import(handler400, handler404, handler500)

# handler400 = 'fitproject.views.bad_request_page'
# handler404 = 'fitproject.views.page_not_found_page'
# handler500 = 'fitproject.views.server_error_page'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fitApp.urls'))
]
