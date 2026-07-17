import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ПІБ')),
                ('position', models.CharField(blank=True, max_length=150, verbose_name='Посада')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=30, verbose_name='Телефон')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активний')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='employees',
                    to='organizations.organization',
                    verbose_name='Організація',
                )),
            ],
            options={
                'verbose_name': 'Працівник',
                'verbose_name_plural': 'Працівники',
                'ordering': ['full_name'],
            },
        ),
    ]
