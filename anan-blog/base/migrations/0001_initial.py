# Generated by Django 4.1.3 on 2022-11-23 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '__first__'),
        ('publications', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=300, null=True)),
                ('lastName', models.CharField(blank=True, max_length=300, null=True)),
                ('email', models.CharField(blank=True, max_length=300, null=True)),
                ('phone', models.CharField(blank=True, max_length=300, null=True)),
                ('consultation', models.CharField(blank=True, max_length=300, null=True)),
                ('companyName', models.CharField(blank=True, max_length=300, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('additionalDetails', models.TextField(blank=True, null=True)),
                ('source', models.CharField(default='UnKnown', max_length=300)),
                ('relevantFile', models.FileField(blank=True, null=True, upload_to='contactus_file/')),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'db_table': 'tbl_contact_us',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('phone', models.CharField(blank=True, max_length=300, null=True)),
                ('education', models.CharField(blank=True, max_length=300, null=True)),
                ('mediaAbout', models.CharField(blank=True, max_length=300, null=True)),
                ('facebook', models.CharField(default='#', max_length=300)),
                ('twitter', models.CharField(default='#', max_length=300)),
                ('linkedin', models.CharField(default='#', max_length=300)),
                ('emailVarified', models.BooleanField(default=False)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'auth_user_info',
            },
        ),
        migrations.CreateModel(
            name='MemberShips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membershipType', models.CharField(blank=True, max_length=300, null=True)),
                ('orderID', models.CharField(blank=True, max_length=300, null=True)),
                ('subscriptionID', models.CharField(blank=True, max_length=300, null=True)),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('commentTime', models.DateTimeField(auto_now_add=True)),
                ('blogId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogs')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_comments',
            },
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('commentTime', models.DateTimeField(auto_now_add=True)),
                ('commentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.comments')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_comment_reply',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(blank=True, max_length=300, null=True)),
                ('productType', models.CharField(blank=True, max_length=300, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('stock', models.IntegerField(default=0)),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.publication')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_cart',
            },
        ),
    ]
