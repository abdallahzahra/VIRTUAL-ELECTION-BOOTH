# Generated by Django 3.1.1 on 2020-09-30 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0006_vote_vote_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='vote_count',
        ),
        migrations.DeleteModel(
            name='Vote_Result',
        ),
    ]
