# Generated by Django 3.1.1 on 2020-09-30 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0003_delete_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote_Result',
            fields=[
            ],
            options={
                'verbose_name': 'Vote Result',
                'verbose_name_plural': 'Votes Result',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('ctf.vote',),
        ),
    ]
