# Generated by Django 4.1.3 on 2022-11-20 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cohorte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('fecha_inicio', models.DateField(max_length=255, verbose_name='Fecha de inicio')),
                ('fecha_finalizacion', models.DateField(max_length=255, verbose_name='Fecha de finalización')),
                ('cupos_aprobados', models.IntegerField(default=0, verbose_name='Cupos aprobados')),
                ('cupos_asignados', models.IntegerField(default=0, verbose_name='Cupos asignados')),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_pago', models.BooleanField(default=False, verbose_name='Estado del pago')),
                ('doc_entrevista', models.URLField(max_length=255, verbose_name='Documento de entrevista')),
                ('calificacion_entrevista', models.IntegerField(default=0, verbose_name='Calificación de entrevista')),
                ('doc_prueba', models.URLField(max_length=255, verbose_name='Documento de prueba')),
                ('calificacion_prueba', models.IntegerField(default=0, verbose_name='Calificación de prueba')),
                ('doc_hoja_vida', models.URLField(max_length=255, verbose_name='Documento de hoja de vida')),
                ('calificacion_cv', models.IntegerField(default=0, verbose_name='Calificación de hoja de vida')),
                ('copia_diploma_pregrado', models.URLField(max_length=255, verbose_name='Documento de diploma de pregrado')),
                ('copia_notas_acta', models.URLField(max_length=255, verbose_name='Documento de notas y acta de grado')),
                ('copia_pasaporte_visa', models.URLField(max_length=255, verbose_name='Documento de pasaporte y visa')),
                ('notas_apostillada', models.URLField(max_length=255, verbose_name='Documento de notas apostillada')),
                ('diploma_apostillado', models.URLField(max_length=255, verbose_name='Documento de diploma apostillado')),
                ('doc_pago_inscripcion', models.URLField(max_length=255, verbose_name='Documento de pago de inscripción')),
                ('fecha_entrevista', models.DateField(max_length=255, verbose_name='Fecha de entrevista')),
                ('puntaje_total', models.IntegerField(default=0, verbose_name='Puntaje total')),
                ('fotocopia_cedula', models.URLField(max_length=255, verbose_name='Documento de fotocopia de cédula')),
                ('url_prueba', models.URLField(max_length=255, verbose_name='Documento de prueba')),
                ('url_entrevista', models.URLField(max_length=255, verbose_name='Documento de entrevista')),
                ('id_aspirante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.aspirante')),
                ('id_cohorte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.cohorte')),
                ('id_maestria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.maestria')),
            ],
        ),
        migrations.CreateModel(
            name='carta_referencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.IntegerField(default=0, verbose_name='Calificación')),
                ('documento', models.URLField(max_length=255, verbose_name='Documento')),
                ('id_inscripcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.inscripcion')),
            ],
        ),
    ]
