# Generated by Django 3.2.5 on 2024-02-02 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_merge_20240202_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='outdepotvehiclereceive',
            name='status',
            field=models.IntegerField(blank=True, help_text='0=active;1=inactive;2=delete', null=True),
        ),
        migrations.AlterField(
            model_name='outdepotvehiclereceive',
            name='bus_reported_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='outdepotvehiclereceive',
            name='bus_reported_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='OwnDepotWithdrawMedaramOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_number', models.CharField(blank=True, max_length=256, null=True)),
                ('status', models.IntegerField(help_text='0=active;1=inactive;2=delete')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='own_depot_withdraw_medaram_operation_created_user', to='app.user')),
                ('updated_by', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='own_depot_withdraw_medaram_operation_updated_user', to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='OwnDepotBusDetailsEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_number', models.CharField(blank=True, max_length=256, null=True)),
                ('unique_no', models.CharField(blank=True, max_length=256, null=True)),
                ('bus_type', models.CharField(blank=True, max_length=256, null=True)),
                ('log_sheet_no', models.CharField(blank=True, max_length=256, null=True)),
                ('driver1_name', models.CharField(blank=True, max_length=256, null=True)),
                ('driver1_phone_number', models.CharField(blank=True, max_length=256, null=True)),
                ('driver2_name', models.CharField(blank=True, max_length=256, null=True)),
                ('driver2_phone_number', models.CharField(blank=True, max_length=256, null=True)),
                ('status', models.IntegerField(help_text='0=active;1=inactive;2=delete')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='own_depot_bus_details_entry_created_user', to='app.user')),
                ('updated_by', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='own_depot_bus_details_entry_updated_user', to='app.user')),
            ],
        ),
    ]
