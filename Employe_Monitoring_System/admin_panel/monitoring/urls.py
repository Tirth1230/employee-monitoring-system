from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('logs/', views.screenshot_log_view, name='screenshot_log'),
    path('upload/', views.upload_screenshot, name='upload_screenshot'),
    path('login/',auth_views.LoginView.as_view(template_name='monitoring/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
]
