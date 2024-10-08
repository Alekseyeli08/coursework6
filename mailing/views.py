import random

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from mailing.models import Mailing, Client, Message
from django.urls import reverse_lazy, reverse
from mailing.forms import MailingForm, ClientForm, MessageForm, MailingManagerForm
from django.core.management import call_command
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from blog.models import Blog
class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing

    def get_queryset(self, *args, **kwargs):
        qyryset = super().get_queryset(*args, **kwargs)
        qyryset = qyryset.filter(active=True)
        return qyryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'active'
        context['inactive'] = ''
        context['random_block'] = Blog.objects.all()[:3]
        context['clients'] = Client.objects.all()
        context['all_mailing'] = Mailing.objects.all()
        context['active_mailing'] = Mailing.objects.filter(active=True)
        return context

class Mailing2ListView(LoginRequiredMixin, ListView):
    model = Mailing

    def get_queryset(self, *args, **kwargs):
        qyryset = super().get_queryset(*args, **kwargs)
        qyryset = qyryset.filter(active=False)
        return qyryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = ''
        context['inactive'] = 'active'
        return context

class MailingDetailView(DetailView):
    model = Mailing

    def clients(request):
        clients = Client.object.all()
        return render(request, "mailing_detail.html", {clients: 'clients'})


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:home")

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.creator = user
        mailing.save()
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:home")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return MailingForm
        if user.has_perm('mailing.can_disable_mailing'):
            return MailingManagerForm
        raise PermissionDenied


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailing:home")


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    success_url = reverse_lazy("mailing:client_list")


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("mailing:client_list")

    def form_valid(self, form):
        customer = form.save()
        user = self.request.user
        customer.creator = user
        customer.save()
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("mailing:client_list")


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("mailing:client_list")


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    success_url = reverse_lazy("mailing:message_list")


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message_list")

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.creator = user
        message.save()
        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message_list")


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("mailing:message_list")


def call_custom_command(request, command_id: int):
    if request.method == 'POST':
        if command_id == 1:
            call_command('run_send_mail')
        elif command_id == 2:
            call_command('run_aps')
    return redirect(reverse('mailing:home'))
