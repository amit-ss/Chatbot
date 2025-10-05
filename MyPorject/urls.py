"""
URL configuration for MyPorject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from MyPorject import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="home"),
    path('login/',views.Login,name="login"),
    path('signup/',views.Signup,name="signup"),
    path('contact/',views.Contact,name="contact"),
    path('team/',views.Team,name="team"),
    path('about/',views.AboutUs,name="about"),
    path('logout/',views.Logout,name="logout"),
    path('profile/',views.Profile,name="profile"),
    path('prodetails/',views.Profiledetails,name="prodetails"),
    path('chatview/',views.chat_interface,name="chatview"),
    path('api/', views.get_ai_response, name='chat_api'),
    path('exam/', views.Exam, name='exam'),
    path('facutly/', views.Facult, name='faculty'),
    path('classtime/', views.Classtime, name='classtime'),
    

]

 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)