# Generated by Django 4.2.7 on 2023-11-01 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_page_alter_category_name_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('slug', models.SlugField(blank=True, default='', max_length=255, unique=True)),
                ('excerpt', models.CharField(max_length=255)),
                ('is_published', models.BooleanField(default=False, help_text='Este campo precisará estar marcado para o post ser exibido publicamente.')),
                ('content', models.TextField()),
                ('cover', models.ImageField(blank=True, default='', upload_to='post/%Y/%m/')),
                ('cover_in_post_content', models.BooleanField(default=True, help_text='Exibe a imagem de capa também dentro do conteúdo do post.')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
                ('tags', models.ManyToManyField(blank=True, default='', to='blog.tag')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
