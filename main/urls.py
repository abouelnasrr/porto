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
    # path('youtube/', views.youtube_view, name='youtube'),
    path('cv/', views.cv, name='cv'),
    # path('add-experience/', views.add_experience, name='add_experience'),
    # path('add-education/', views.add_education, name='add_education'),
    # path('add-skill/', views.add_skill, name='add_skill'),
    # path('add-certificate/', views.add_certificate, name='add_certificate'),
    # path('add-language/', views.add_language, name='add_language'),
    # path('add-volunteering/', views.add_volunteering, name='add_volunteering'),
    # path('edit-summary/', views.edit_summary, name='edit_summary'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

