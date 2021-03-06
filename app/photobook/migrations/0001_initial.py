# Generated by Django 2.2.9 on 2020-01-17 01:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagenumber', models.PositiveIntegerField(auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(default='무제', max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField(blank=True)),
                ('end_date', models.DateTimeField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photobook.Page')),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photobook.PhotoBook'),
        ),
    ]
