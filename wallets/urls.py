from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^balance$', views.check_balance, name='balance'),
    url(r'^newaddress$', views.get_new_address, name='new_address'),
    url(r'^addresses$', views.get_addresses, name='addresses'),
    url(r'^accountaddress$', views.get_account_address, name='accountaddress'),
    url(r'^transactions$', views.list_transactions, name='transactions'),
]