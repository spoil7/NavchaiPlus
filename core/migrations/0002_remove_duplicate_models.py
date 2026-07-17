from django.db import migrations


class Migration(migrations.Migration):
    """
    Прибирає застарілі моделі-дублікати (Organization/Department/Employee/
    Course/Test/Certificate), які випадково опинились у core і конфліктували
    зі справжніми даними в organizations.Organization. Реальні дані
    зберігаються у власних застосунках (organizations, employees, ...).
    """

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='test',
            name='course',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='course',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='employee',
        ),
        migrations.DeleteModel(name='Certificate'),
        migrations.DeleteModel(name='Test'),
        migrations.DeleteModel(name='Employee'),
        migrations.DeleteModel(name='Department'),
        migrations.DeleteModel(name='Course'),
        migrations.DeleteModel(name='Organization'),
    ]
