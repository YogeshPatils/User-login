from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('signup/',signUpView,name='signup'),
    path('signin/',signInView,name='signin'),
    path('home/',homeView,name='home'),
    path('loggout/',logOutView,name='logout'),
    path('updatepic/<int:id>/',updatePicView,name='update'),
    path('updatepwd/',updatePasswordView,name='updatepwd')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

