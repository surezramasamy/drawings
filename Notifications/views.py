from django.shortcuts import render
from django.views.generic import ListView,DeleteView,UpdateView,CreateView
from .import models


class NotificationListView(ListView):
    context_object_name='notify'
    model = models.notification
    template_name= 'notification.html'
class NoteCreateView(CreateView):
    fields = ('Information','Action_required','Raised_by')
    model =models.notification
