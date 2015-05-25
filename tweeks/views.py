from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from tweeks.forms import TweekForm
from tweeks.models import Tweek

def index(request):
    tweeks = Tweek.objects.all()
    form = TweekForm()
    if request.method == "POST":
        form = TweekForm(request.POST)
        if form.is_valid():
            tweek = form.save(commit=False)
            tweek.author = request.user
            tweek.save()
            return HttpResponseRedirect('/')
    return render(
        request,
        'tweek/index.html', {
            'tweeks': tweeks,
            'form': form,
        })


def get_user_tweeks(request, user_pk=None):
    tweeks = Tweek.objects.filter(author=user_pk)
    author = User.objects.get(pk=user_pk)
    return render(
        request,
        'tweek/index.html',{
            "tweeks": tweeks,
            'author': author
        })