from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from .forms import NameForm, ContactForm, EntryForm, PersonForm, FavForm
from .models import Entry
from django.forms import formset_factory  


# Create your views here.

def home_view(request):
    if 2==2:
        return render(request, 'tut/home.html')
        # return HttpResponseRedirect('/name/')
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

def get_name(request):
    # create to change an existing entry 
    entry = Entry.objects.get(pk=1)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = EntryForm(request.POST, instance=entry)
        x = 'Name'
        # check whether it is valid 
        if form.is_valid():
            # process the data in form.cleaned_data as required 
            # redirect to a new URL 
            # return HttpResponseRedirect('/thanks/')
            return HttpResponseRedirect('/home/')

    # if a GET or any other method we'll create a blank form
    else:
        form = EntryForm(instance=entry)

    # context = {'form':form}
    return render(request, 'tut/name.html', {'form':form})

def thanks(request):
    return render(request, 'tut/thanks.html', {})







def create_person(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        print('////////////////////////')
        form = PersonForm()
    return render(request, 'tut/person.html', {'form':form})


def redirect1(request):
    obj = get_object_or_404(Entry, id=1)
    obj1 = Entry.objects.all()
    obj2 = get_object_or_404(obj1, id=1)
    # return HttpResponseRedirect(reverse('tut:name'))
    # return redirect('/name/')
    # return redirect('tut:home')
    # return HttpResponseNotFound('<h1>Page Not Found</h1>')
    # return HttpResponse('<h1>Page Found</h1>')
    # raise Http404('<h1>Page Not Found</h1>')
    # return redirect(obj)
    # fav(request)

def fav(request):
    formset1 = formset_factory(FavForm, extra=2, max_num=1)
    formset = formset1(initial=[{'favorite_color':'welcome'}])
    form = FavForm(request.POST or None)
    return render(request,'tut/fav.html', {'form':form, 'formset':formset})

def entry(request):
    form = EntryForm(request.POST or None)
    return render(request, 'tut/entry.html', {'form':form})
