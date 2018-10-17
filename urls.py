from django.conf.urls import url
from .import views
urlpatterns=[
    url(r'^$',views.input),
    url(r'^insert$',views.insert),
    url(r'^display$',views.display),
    url(r'^productapi$',views.ProductList.as_view()),
]