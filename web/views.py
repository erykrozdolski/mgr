from django.shortcuts import render
from web.models import Answer, BigAnswer, FirstPoll, SecondPoll, Responder
from django.db.models import Q
# Create your views here.
from web.core import *


def index(request):
    return render(request, 'index.html', {})

def intro(request):
    return render(request, 'intro.html', {})


def first_poll(request):
    offensive_words = poll1.offensive_words.exclude(value=None)
    word_number_list = list(map(lambda c: get_important(c, offensive_words), offensive_words))
    word_number_list = dedup(word_number_list)
    word_number_list.sort(key= lambda x: x[1], reverse=True)
    context = {'word_number_list': word_number_list}
    return render(request, 'first_poll.html', context)


def second_poll(request):
    second_poll = SecondPoll.objects.all()[0]
    return render(request, 'second_poll.html', {'poll': ""})

def kurwa(request):
    return create_poll2_table(request, "kurwa")

def idiota(request):
    return create_poll2_table(request, "idiota")

def szmata(request):
    return create_poll2_table(request, "szmata")

def debil(request):
    return create_poll2_table(request, "debil")

def pizda(request):
    return create_poll2_table(request, "pizda")

def chuj(request):
    return create_poll2_table(request, "chuj")

def dziwka(request):
    return create_poll2_table(request, "dziwka")

def skurwysyn(request):
    return create_poll2_table(request, "skurwysyn")


def first_poll_by_responders(request):
    offensive_words = FirstPoll.objects.all()[0].offensive_words.all()
    return render(request, 'first_poll.html', {'offensive_words': offensive_words})
