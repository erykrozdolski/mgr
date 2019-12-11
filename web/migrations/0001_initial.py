# Generated by Django 2.1.7 on 2019-12-08 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, default='no answer', max_length=200, null=True)),
                ('category', models.CharField(blank=True, default='no answer', max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FirstPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_time', models.ManyToManyField(related_name='firstpoll_free_time', to='web.Answer')),
                ('important_in_life', models.ManyToManyField(related_name='firstpoll_important_in_life', to='web.Answer')),
                ('movie', models.ManyToManyField(related_name='firstpoll_movie', to='web.Answer')),
                ('music', models.ManyToManyField(related_name='firstpoll_music', to='web.Answer')),
                ('offensive_words', models.ManyToManyField(related_name='firstpoll_offensive_words', to='web.Answer')),
                ('what_you_like', models.ManyToManyField(related_name='firstpoll_what_you_like', to='web.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Responder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.CharField(blank=True, max_length=200, null=True)),
                ('sex', models.CharField(blank=True, max_length=200, null=True)),
                ('education', models.CharField(blank=True, max_length=200, null=True)),
                ('living_place', models.CharField(blank=True, max_length=200, null=True)),
                ('origin_place', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecondPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chuj', models.ManyToManyField(related_name='secondpoll_chuj', to='web.Answer')),
                ('debil', models.ManyToManyField(related_name='secondpoll_debil', to='web.Answer')),
                ('dziwka', models.ManyToManyField(related_name='secondpoll_dziwka', to='web.Answer')),
                ('idiota', models.ManyToManyField(related_name='secondpoll_idiota', to='web.Answer')),
                ('kurwa', models.ManyToManyField(related_name='secondpoll_kurwa', to='web.Answer')),
                ('pizda', models.ManyToManyField(related_name='secondpoll_pizda', to='web.Answer')),
                ('skurwysyn', models.ManyToManyField(related_name='secondpoll_skurwysyn', to='web.Answer')),
                ('szmata', models.ManyToManyField(related_name='secondpoll_szmata', to='web.Answer')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='responder',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responder_of', to='web.Responder'),
        ),
    ]