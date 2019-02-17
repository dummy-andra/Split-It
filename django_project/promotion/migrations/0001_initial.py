# Generated by Django 2.1.5 on 2019-02-12 18:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='brand_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('image', models.ImageField(default='default.jpg', upload_to='promotion_pics')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotions', to='promotion.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promotion.Category')),
            ],
        ),
    ]