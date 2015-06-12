from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
]
# so only an empty string will match
    
