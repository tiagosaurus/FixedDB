# Generated by Django 2.2 on 2019-04-22 04:42

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20190422_0311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urls', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('is_flagged', models.BooleanField(default=False, null=True)),
                ('content', models.TextField(max_length=1000000, null=True)),
                ('by_admin', models.BooleanField(default=False, null=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_used', models.BooleanField(default=False, null=True)),
                ('original_image', models.ImageField(null=True, upload_to='')),
                ('filtered_versions', django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(null=True, upload_to=''), blank=True, null=True, size=None)),
                ('is_flagged', models.BooleanField(default=False, null=True)),
                ('by_admin', models.BooleanField(default=False, null=True)),
                ('post_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Post')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_name', models.CharField(max_length=16, null=True)),
                ('image_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Image')),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_num', models.CharField(max_length=16, null=True)),
                ('cvv', models.CharField(max_length=3, null=True)),
                ('holder_name', models.CharField(max_length=50, null=True)),
                ('card_expiration', models.CharField(max_length=25, null=True)),
                ('currently_used', models.BooleanField(default=True, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('zipcode', models.IntegerField(null=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1000000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('by_admin', models.BooleanField(default=False, null=True)),
                ('post_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Post')),
                ('replies', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Comment')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Member')),
            ],
        ),
    ]
