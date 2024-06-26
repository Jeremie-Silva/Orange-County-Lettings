from django.db import migrations, models
import django.core.validators
import django.db.models.deletion


def move_lettings_and_addresses(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    NewAddress = apps.get_model('lettings', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewLetting = apps.get_model('lettings', 'Letting')

    for old_address in OldAddress.objects.all():
        new_address = NewAddress(
            id=old_address.id,
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code
        )
        new_address.save()

    for old_letting in OldLetting.objects.all():
        new_letting = NewLetting(
            id=old_letting.id,
            title=old_letting.title,
            address_id=old_letting.address_id
        )
        new_letting.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
                ('street', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
                ('zip_code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
                ('country_iso_code', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='Letting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lettings.Address')),
            ],
        ),
        migrations.RunPython(move_lettings_and_addresses),
    ]
