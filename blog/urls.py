from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import home_view, register_view, login_view, logout_view
from post.views import post_creation_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home-page'),
    path('login/', login_view, name='login-page'),
    path('logout/', logout_view, name='logout-page'),
    path('register/', register_view, name='register-page'),
    path('create/', post_creation_view, name='post-creation-page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

