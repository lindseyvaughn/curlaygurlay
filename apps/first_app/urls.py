from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^curlaygurlay$', views.home_page),
    url(r'^curlaygurlay/loose_curl$', views.loose_curl_page),
    url(r'^curlaygurlay/tight_curl$', views.tight_curl_page),
    url(r'^curlaygurlay/kinky_curl$', views.kinky_curl_page),

    url(r'^curlaygurlay/about$', views.about_page),
    url(r'^curlaygurlay/products$', views.products_page),
    url(r'^curlaygurlay/blog$', views.blog_page),
]