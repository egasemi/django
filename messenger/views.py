from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404
from .models import Thread
from django. http import JsonResponse

@method_decorator(login_required, name="dispatch")
class ThreadList(ListView):
    model = Thread
    template_name = "messenger/thread_list.html"
"""    def get_queryset(self):
        queryset = super(ThredList, self).get_queryset()
        return queryset.filter(users=self.request.user)"""

@method_decorator(login_required, name="dispatch")
class ThreadDetail(DetailView):
    model = Thread

    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj

def add_message(request, pk):
    print(request.GET)
    json_response = {'created':False}
    return JsonResponse(json_response)
    