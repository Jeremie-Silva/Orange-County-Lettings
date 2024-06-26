from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


def move_profiles(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')
    User = apps.get_model(settings.AUTH_USER_MODEL)

    for old_profile in OldProfile.objects.all():
        new_profile = NewProfile(
            id=old_profile.id,
            favorite_city=old_profile.favorite_city,
            user=User.objects.get(id=old_profile.user_id)
        )
        new_profile.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_city', models.CharField(blank=True, max_length=64)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(move_profiles),
    ]
