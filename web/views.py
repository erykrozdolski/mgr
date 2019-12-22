from django.shortcuts import render
from web.models import Answer, BigAnswer, FirstPoll, SecondPoll, Responder
import itertools
# Create your views here.

poll1 = FirstPoll.objects.first()
poll2 = SecondPoll.objects.first()

def index(request):
    return render(request, 'index.html', {})

def get_important(answer, answer_list):
    related_answers = answer_list.filter(category=answer.category)
    number = answer_list.filter(category=answer.category).count()
    power_sum = 0
    responds = 0
    for a in related_answers:
        if a.value != "no answer" and a.power != "no answer" and a.power:
            print(a.power)
            power_sum += int(a.power)
            responds += 1
    average_power = int(power_sum / responds) if responds else "-"
    category_answers = set([ o.value.lower() for o in answer_list.filter(category=answer.category)])
    example_str = ", ".join(category_answers)
    return (answer.category, number, average_power, example_str)

def first_poll(request):
    offensive_words = poll1.offensive_words.exclude(value=None)
    word_number_list = list(map(lambda c: get_important(c, offensive_words), offensive_words))
    word_number_list = list(dict.fromkeys(word_number_list))
    word_number_list.sort(key= lambda x: x[1], reverse=True)
    context = {'word_number_list': word_number_list}
    return render(request, 'first_poll.html', context)


def second_poll(request):
    second_poll = SecondPoll.objects.all()[0]
    return render(request, 'second_poll.html', {'poll': ""})


def kurwa(request):
    answers = Answer.objects.exclude(responder__poll="poll1").exclude(value=None)
    categories = list(map(lambda c: get_important(c, answers), answers))
    power_sum = 0
    responds = 0

    categories = answers.values_list('category', flat=True).distinct()

    average_power = int(power_sum / responds) if responds else "-"

    return render(request, 'kurwa.html', {'average_power': average_power, 'categories':categories})


def first_poll_by_responders(request):
    offensive_words = FirstPoll.objects.all()[0].offensive_words.all()
    return render(request, 'first_poll.html', {'offensive_words': offensive_words})
