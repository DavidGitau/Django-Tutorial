from operator import mod
from django.shortcuts import render, get_object_or_404
from tut.forms import PersonForm
from django.views import View
from datetime import datetime
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import (
    Author,
    Book,
    Publisher,
)


def home(request):
    return render(request, 'cviews/home.html')


class PersonFormView(View):
    form_class = PersonForm
    initial = {}
    template_name = 'tut/person.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            form = self.form_class()

        return render(request, self.template_name, {'form': form})


class PublisherList(ListView):
    # model = Publisher
    template_name = 'cviews/publisher_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        self.publishers = Publisher.objects.all()
        # self.publishers = get_object_or_404(Publisher, name=self.kwargs['publishers'])
        return self.publishers


class PublisherDetail(DetailView):
    # model = Publisher
    context_object_name = 'object'
    template_name = 'cviews/publisher_detail.html'
    queryset = Publisher.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["publishers"] = Publisher.objects.all()
        context['title'] = 'Detail'
        return context

    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = datetime.now()
        obj.save()
        return obj


class CustomCreate(CreateView):
    # model = Publisher
    # template_name = 'cviews/publisher_form.html'
    fields = '__all__'


class CustomList(ListView):
    context_object_name = 'object_list'


class CustomDetail(DetailView):
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["publishers"] = Publisher.objects.all()
        context['books'] = Book.objects.all()
        context['authors'] = Author.objects.all()
        context['title'] = 'Detail'
        return context
