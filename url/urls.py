# from django.urls import path
# from . import views
# app_name = "url"
# urlpatterns = [
#     path("", views.index, name="home")
# ]

from django.urls import path
from . import views
app_name = "url"
urlpatterns = [
    path("", views.urlShort, name="home"),
    path("u", views.urlRedirect, name="redirect")
]