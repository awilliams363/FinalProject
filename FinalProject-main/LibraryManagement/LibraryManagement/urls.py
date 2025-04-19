"""librarymanagement URL Configuration

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
from django.conf.urls import include
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls') ),
    path('', views.home_view),
    path('index',views.index_view),

    path('adminclick', views.adminclick_view),
    path('studentclick', views.studentclick_view),
    path('facultyclick', views.facultyclick_view),

    # path('adminsignup', views.adminsignup_view),
    path('studentsignup', views.studentsignup_view),
    path('adminsignup', views.adminssignup_view),
    path('facultysignup', views.facultysignup_view),
    path('adminlogin', LoginView.as_view(template_name='library/adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='library/studentlogin.html')),
    path('facultylogin', LoginView.as_view(template_name='library/facultylogin.html')),
    path('returnbook', views.bookreturn_view, name='returnbook'),


    path('logout', views.logout_view, name='library/logout.html'),
    path('afterlogin', views.afterlogin_view),

    path('addbook', views.addbook_view),
    path('viewbook', views.viewbook_view),
    path('issuebook', views.issuebook_view),
    path('viewissuedbook', views.viewissuedbook_view),
    path('viewstudent', views.viewstudent_view),
    path('viewissuedbookbystudent', views.viewissuedbookbystudent,name='viewissuedbookbystudent'),
    path('reservebook', views.bookreservation_view),

    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    path('searchbook', views.searchbook_view),
    path('reminder', views.reminder_view, name='reminder'),
]
