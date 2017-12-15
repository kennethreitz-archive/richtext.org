# Generated by Django 2.0 on 2017-12-15 16:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RichPost',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('views', models.BigIntegerField()),
                ('published', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
