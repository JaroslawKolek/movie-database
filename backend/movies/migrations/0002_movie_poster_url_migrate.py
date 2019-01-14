# Generated by Django 2.1.5 on 2019-01-14 13:38

from django.db import migrations, models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def is_poster_url_valid(url):
    val = URLValidator()
    try:
        val(url)
        return True
    except ValidationError:
        return False


def migrate_str_to_urls(apps, schema_editor):
    Movie = apps.get_model('movies', 'Movie')
    for m in Movie.objects.all():
        m.poster_url_migrate = m.poster_url if is_poster_url_valid(m.poster_url) else None
        m.save()


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster_url_migrate',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.RunPython(migrate_str_to_urls),
        migrations.RemoveField(
            model_name='movie',
            name='poster_url'
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='poster_url_migrate',
            new_name='poster_url'
        )
    ]