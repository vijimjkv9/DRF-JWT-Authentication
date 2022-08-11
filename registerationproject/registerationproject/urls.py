"""registerationproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('registerapp.urls'))
]

"""
user registeration api- create user
headers => Accept , application/json
payload =>{"email":"","name": "","password":"", "password2":"", "tc":True}
login ->
headers => Accept , application/json
payload =>{"email":"","password":""}
want to access data of user profile (get)->
headers => Accept , application/json
        => Authorization , Bearer token(from access)
change password-> 
headers => Accept , application/json
        => Authorization , Bearer token(from access)
payload =>{"password":"","password2":""}

post - > reset password email
headers => Accept , application/json
payload =>{"email":""} -> password rest link will send our email id

post - > reset password (that link) time-2.34
headers => Accept , application/json
payload =>{"email":""} -> password rest link will send our email id

.env file contains->    EMAIL_USER = '',
                        EMAIL_PASS = '',
                        EMAIL_FROM  = ''
"""
