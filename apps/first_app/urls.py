from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^curlaygurlay$', views.home_page),
    url(r'^curlaygurlay/loose_curl$', views.loose_curl),
    url(r'^curlaygurlay/tight_curl$', views.tight_curl),
    url(r'^curlaygurlay/kinky_curl$', views.kinky_curl),
]