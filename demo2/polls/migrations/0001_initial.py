# Generated by Django 2.2 on 2019-04-18 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50)),
                ('qpub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VoteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=50)),
                ('vnum', models.IntegerField(verbose_name=0)),
                ('vquestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.QuestionInfo')),
            ],
        ),
    ]
