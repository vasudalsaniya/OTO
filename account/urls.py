from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('account/signup',views.signup,name='signup'),
    path('',views.loginView,name='login'),
    path('account/logout',views.logoutView,name='logout'),
    path('account/profile',views.profileView,name='profile'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)