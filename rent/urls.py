from django.urls import path
from rent import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('login/', views.Login, name='Login'),
    path('register/', views.Register, name='Register'),
    path('logout/', views.Logout, name='Logout'),
    path('owner/<int:id>/adjust/', views.AdjustHouse, name='AdjustHouse'),
    path('owner/add/', views.AddHouse, name='AddHouse'),
    path('owner/<int:id>/delete/', views.DeleteHouse, name='DeleteHouse'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
