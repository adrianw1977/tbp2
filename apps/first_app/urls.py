from django.conf.urls import url
from . import views
# Models -- views -- TEMPLATES

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^blogs$', views.blogs),
    # url(r'^new_user$', views.create)
]





