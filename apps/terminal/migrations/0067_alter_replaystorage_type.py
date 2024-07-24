# Generated by Django 4.1.10 on 2023-11-02 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0066_applethost_using_same_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replaystorage',
            name='type',
            field=models.CharField(choices=[('null', 'Null'), ('server', 'Server'), ('s3', 'S3'), ('ceph', 'Ceph'), ('swift', 'Swift'), ('oss', 'OSS'), ('azure', 'Azure'), ('obs', 'OBS'), ('cos', 'COS'), ('sftp', 'SFTP')], default='server', max_length=16, verbose_name='Type'),
        ),
    ]