from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^by_topic/', views.bill_list_by_topic),
    url(r'^by_location', views.bill_list_by_location),
    url(r'^current_session/', views.bill_list_current_session),
    url(r'^latest_activity/', views.bill_list_latest),
    url(r'^detail/(?P<bill_session>(.*))/(?P<bill_identifier>(.*))/$', views.bill_detail, name='bill_detail'),
]
