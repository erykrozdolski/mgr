from django.db import models
from datetime import datetime

class Responder(models.Model):
    poll = models.CharField(max_length=200, null=True, blank=True)
    age = models.CharField(max_length=200, null=True, blank=True)
    sex = models.CharField(max_length=200, null=True, blank=True)
    education = models.CharField(max_length=200, null=True, blank=True)
    living_place = models.CharField(max_length=200, null=True, blank=True)
    origin_place = models.CharField(max_length=200, null=True, blank=True )
    martial_status = models.CharField(max_length=200, null=True, blank=True )
    profession = models.CharField(max_length=200, null=True, blank=True )


class Answer(models.Model):
    value = models.CharField(max_length=200, null=True, blank=True, default="no answer")
    power = models.CharField(max_length=200, null=True, blank=True, default="no answer")
    category = models.CharField(max_length=250, null=True, blank=True, default="no answer")
    responder = models.ForeignKey(Responder, null=True, blank=True, on_delete=models.CASCADE)


class BigAnswer(models.Model):
    answers = models.ManyToManyField("Answer", related_name='answers')
    power = models.CharField(max_length=200, null=True, blank=True, default="no answer")
    category = models.CharField(max_length=250, null=True, blank=True, default="no answer")
    responder = models.ForeignKey(Responder, null=True, blank=True, on_delete=models.CASCADE)


class FirstPoll(models.Model):
    offensive_words = models.ManyToManyField("Answer", related_name='_s_offensive_words')
    free_time = models.ManyToManyField("Answer", related_name='_s_free_time')
    movie = models.ManyToManyField("Answer", related_name='_s_movie')
    what_you_like = models.ManyToManyField("Answer", related_name='_s_what_you_like')
    important_in_life = models.ManyToManyField("Answer", related_name='_s_important_in_life')
    music = models.ManyToManyField("Answer", related_name='_s_music')


class SecondPoll(models.Model):
    kurwa = models.ManyToManyField("BigAnswer", related_name='_s_kurwa')
    chuj = models.ManyToManyField("BigAnswer", related_name='_s_chuj')
    idiota = models.ManyToManyField("BigAnswer", related_name='_s_idiota')
    debil = models.ManyToManyField("BigAnswer", related_name='_s_debil')
    szmata = models.ManyToManyField("BigAnswer", related_name='_s_szmata')
    pizda = models.ManyToManyField("BigAnswer", related_name='_s_pizda')
    skurwysyn = models.ManyToManyField("BigAnswer", related_name='_s_skurwysyn')
    dziwka = models.ManyToManyField("BigAnswer", related_name='_s_dziwka')
    kutas = models.ManyToManyField("BigAnswer", related_name='_s_kutas')
