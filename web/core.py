from django.shortcuts import render
from web.models import Answer, BigAnswer, FirstPoll, SecondPoll, Responder
import itertools

poll1 = FirstPoll.objects.first()
poll2 = SecondPoll.objects.first()

def flatten(l):
    return list(itertools.chain(*l))

def dedup(l):
    return list(dict.fromkeys(l))

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

def create_poll2_table(request, key):
    big_answers = getattr(poll2, key).all()
    answers = [ ba.answers.all() for ba in big_answers]
    id_list = [ a.pk for a in flatten(answers)]
    answers = Answer.objects.filter(pk__in=id_list)
    power_sum = 0
    responds = 0

    for ba in big_answers:
        if ba.power != "no answer" and ba.power:
            power_sum += int(ba.power)
            responds += 1
    average_power = int(power_sum / responds) if responds else "-"


    categories = list(map(lambda c: get_important(c, answers), answers))
    categories = dedup(categories)
    categories.sort(key= lambda x: x[1], reverse=True)

    return render(request, 'poll2_table.html', {'categories':categories, "key": key, "average_power": average_power})
