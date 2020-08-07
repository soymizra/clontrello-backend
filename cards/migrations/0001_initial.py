# Generated by Django 3.0.8 on 2020-08-07 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(null=True)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.List')),
                ('members', models.ManyToManyField(to='users.User')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='users.User')),
            ],
        ),
    ]
