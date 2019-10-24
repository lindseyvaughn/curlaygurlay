from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^admin$', views.admin),
    url(r'^create_product$', views.create_product),

    url(r'^curlaygurlay/login_register$', views.login_register_page),
    url(r'^register_user$', views.register_user),
    url(r'^login_user$', views.login_user),
    url(r'^logout$', views.logout),

    url(r'^curlaygurlay$', views.home_page),
    url(r'^curlaygurlay/loose_curl$', views.loose_curl_page),
    url(r'^curlaygurlay/tight_curl$', views.tight_curl_page),
    url(r'^curlaygurlay/kinky_curl$', views.kinky_curl_page),
    url(r'^curlaygurlay/about$', views.about_page),
    url(r'^curlaygurlay/products$', views.products_page),
    url(r'^curlaygurlay/blog$', views.blog_page),
    url(r'^curlaygurlay/account$', views.account_page),

    url(r'^curlaygurlay/cart$', views.shopping_cart_page),

    url(r'^addToCart/(?P<product_id>\d+)$', views.addToCart),

]