# Generated by Django 4.1.6 on 2023-02-05 06:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='room',
            field=models.UUIDField(default=uuid.UUID('41baef4f-5e50-4115-a685-ae4839d52152')),
        ),
        migrations.CreateModel(
            name='GroupMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('sender', models.CharField(max_length=50)),
                ('message_time', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_message', to='chat.group')),
            ],
        ),
    ]