import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='edrpou',
            field=models.CharField(
                blank=True,
                help_text='8 цифр для юридичної особи або 10 цифр для ФОП.',
                max_length=20,
                validators=[
                    django.core.validators.RegexValidator(
                        message='ЄДРПОУ має містити 8 цифр (юрособа) або 10 цифр (ФОП).',
                        regex='^\\d{8}$|^\\d{10}$',
                    )
                ],
                verbose_name='ЄДРПОУ',
            ),
        ),
    ]
