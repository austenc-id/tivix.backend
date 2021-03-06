# Generated by Django 4.0.4 on 2022-04-17 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('IMDBid', models.TextField()),
                ('type', models.TextField(choices=[('movie', 'movie')])),
                ('title', models.TextField()),
                ('date', models.DateField(null=True)),
                ('year', models.IntegerField()),
                ('description', models.TextField(null=True)),
                ('audience', models.TextField(null=True)),
                ('length', models.IntegerField(null=True)),
                ('awards', models.TextField(null=True)),
                ('poster', models.URLField()),
                ('earnings', models.IntegerField(null=True)),
                ('actors', models.ManyToManyField(related_name='production_actors', to='content.actor')),
                ('directors', models.ManyToManyField(related_name='production_directors', to='content.director')),
                ('genres', models.ManyToManyField(related_name='production_genres', to='content.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.TextField()),
                ('score', models.DecimalField(decimal_places=1, max_digits=3)),
                ('possible', models.IntegerField()),
                ('production', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.production')),
            ],
        ),
        migrations.AddField(
            model_name='production',
            name='writers',
            field=models.ManyToManyField(related_name='production_writers', to='content.writer'),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(unique=True)),
                ('type', models.TextField(choices=[('default', 'default'), ('created', 'created'), ('search', 'search')])),
                ('description', models.TextField()),
                ('productions', models.ManyToManyField(blank=True, related_name='gallery_productions', to='content.production')),
            ],
            options={
                'verbose_name_plural': 'Galleries',
            },
        ),
    ]
