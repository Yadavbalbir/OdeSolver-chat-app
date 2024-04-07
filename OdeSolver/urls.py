import imp
from django.contrib import admin
from django.urls import path,include

from OdeSolver.settings import MEDIA_ROOT
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('chat/<str:chat_model>',views.chatView, name='chat'),
    path('ask_agent/<str:chat_model>',views.AskAgentView, name='ask_agent'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
