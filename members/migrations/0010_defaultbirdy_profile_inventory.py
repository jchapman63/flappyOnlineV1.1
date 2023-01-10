# Generated by Django 4.1.5 on 2023-01-02 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_alter_profile_unlockedbirds'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultBirdy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='static/images/birdy.png', upload_to='')),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='inventory',
            field=models.ManyToManyField(to='members.defaultbirdy'),
        ),
    ]