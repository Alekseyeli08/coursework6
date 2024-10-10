from mailing.apps import MailingConfig
from django.urls import path
from mailing.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, \
    ClientListView, ClientUpdateView, ClientCreateView, ClientDetailView, ClientDeleteView, MessageListView, \
    MessageUpdateView, MessageCreateView, MessageDetailView, MessageDeleteView, call_custom_command, Mailing2ListView, LogListView
from django.views.decorators.cache import cache_page
app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='home'),
    path('mailing/<int:pk>/', cache_page(60)(MailingDetailView.as_view()), name='mailing_detail'),
    path('inactive', Mailing2ListView.as_view(), name='mailing_list2'),
    path('mailing/create', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/create', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message/create', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
    path("command/<int:command_id>/call/", call_custom_command, name="call_custom_command"),
    path('log/', LogListView.as_view(), name='log_list'),

]
