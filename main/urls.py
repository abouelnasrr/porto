from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.porto, name='porto'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('project/delete/<int:pk>/', views.delete_project, name='delete_project'),
    path('save/<int:pk>/', views.save_message, name='save_message'),
    path('star/<int:pk>/', views.star_message, name='star_message'),
    path('delete/<int:pk>/', views.delete_message, name='delete_message'),
    path('youtube/', views.youtube, name='youtube'),
    path('cv/', views.cv, name='cv'),
    path('delete-video/<int:pk>/', views.delete_video, name='delete_video'),
    path('auth/login/', views.auth_login, name='auth_login'),
    path('auth/nt/', views.auth_nt, name='auth_nt'),
    path('auth/bro/', views.auth_bro, name='auth_bro'),
    path('logout/', views.logout_auth, name='logout_auth'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

