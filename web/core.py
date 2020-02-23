from django.shortcuts import render
from web.models import Answer, BigAnswer, FirstPoll, SecondPoll, Responder
import itertools

poll1 = FirstPoll.objects.first()
poll2 = SecondPoll.objects.first()

def add_other_category(categories, overall_number):
    new_categories = []
    others = []
    number = 0
    for category in categories:
        if category[1] >= 3:
            new_categories.append(category)
        else:
            others.append(category)
    for c in others:
        number += c[1]
    percent_value = '{0:.1f}'.format(( number / overall_number) * 100)
    other = ("inne", number, percent_value, "")
    new_categories.append(other)
    return new_categories

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

def get_important2(answer, answer_list):
    related_answers = answer_list.filter(category=answer.category)
    number = answer_list.filter(category=answer.category).count()
    category_answers = set([ o.value.lower() for o in answer_list.filter(category=answer.category)])
    example_str = ", ".join(category_answers)
    percent_value = '{0:.1f}'.format(( number / answer_list.count()) * 100)
    return (answer.category, number, percent_value, example_str)

def create_poll2_table(request, key):
    big_answers = getattr(poll2, key).all()
    answers = [ ba.answers.all() for ba in big_answers]
    id_list = [ a.pk for a in flatten(answers)]
    answers = Answer.objects.filter(pk__in=id_list)
    power_sum = 0
    responds = 0
    for ba in big_answers:
        if ba.power != "no answer" and ba.power:
            power_sum += float(ba.power)
            responds += 1
    average_power = int(power_sum / responds) if responds else "-"
    categories = list(map(lambda c: get_important2(c, answers), answers))
    categories = dedup(categories)
    categories.sort(key= lambda x: x[1], reverse=True)
    overall_answers = len(answers)
    categories_with_other = add_other_category(categories, overall_answers)
    return render(request, 'poll2_table.html', {'categories':categories_with_other, "key": key, "average_power": average_power, "overall_answers": overall_answers})


def get_answers_by_name(key):
    poll2 = SecondPoll.objects.first()
    big_answers = getattr(poll2, key).all()
    answers = []
    for ba in big_answers:
        answers += ba.answers.all()
    return answers


def change_category(new_c, old_c):
    answers = Answer.objects.filter(category=old_c)
    for a in answers:
        a.category = new_c
        a.save()

def change_category_by_list(new_c, old_c, table_name):
    answers = get_answers_by_name(table_name)
    category_answers = Answer.objects.filter(category=old_c)
    common = list(set(category_answers) & set(answers))
    if common:
        print("poszło")
    else:
        print("pusto", "\n answers:", len(answers), "\n category_answers:", len(category_answers))
    for a in common:
        a.category = new_c
        a.save()

def set_category():
    answers = Answer.objects.exclude(responder__poll="poll1").filter(category=None)
    for a in answers:
        print("Ustal kategorię:", a.value)
        new_category = input()
        if new_category:
            a.category = new_category
            a.save()

def set_category_by_value(value, new_category):
    answers = Answer.objects.filter(value=value)
    for a in answers:
        a.category = new_category
        a.save()

def set_category_by_list(lst):
    for a in lst:
        print("Ustal kategorię:", a.value)
        new_category = input()
        if new_category:
            a.category = new_category
            a.save()
