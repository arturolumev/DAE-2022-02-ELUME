# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblAlumno(models.Model):
    alumno_id = models.AutoField(primary_key=True)
    alumno_nombre = models.CharField(max_length=100)
    alumno_email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_alumno'


class TblCurso(models.Model):
    curso_id = models.AutoField(primary_key=True)
    curso_nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tbl_curso'


class TblEvaluacion(models.Model):
    evaluacion_id = models.AutoField(primary_key=True)
    evaluacion_nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_evaluacion'


class TblMatricula(models.Model):
    matricula_id = models.AutoField(primary_key=True)
    alumno = models.ForeignKey(TblAlumno, models.DO_NOTHING)
    nivel = models.ForeignKey('TblNivel', models.DO_NOTHING)
    modulo = models.ForeignKey('TblModulo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tbl_matricula'


class TblMatriculaCurso(models.Model):
    matricula_curso_id = models.AutoField(primary_key=True)
    matricula = models.ForeignKey(TblMatricula, models.DO_NOTHING)
    curso = models.ForeignKey(TblCurso, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tbl_matricula_curso'


class TblMatriculaNota(models.Model):
    matricula_nota_id = models.AutoField(primary_key=True)
    matricula = models.ForeignKey(TblMatricula, models.DO_NOTHING)
    evaluacion = models.ForeignKey(TblEvaluacion, models.DO_NOTHING)
    matricula_nota_valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_matricula_nota'


class TblModulo(models.Model):
    modulo_id = models.AutoField(primary_key=True)
    modulo_nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_modulo'


class TblNivel(models.Model):
    nivel_id = models.AutoField(primary_key=True)
    nivel_nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_nivel'


class TblProfesor(models.Model):
    profesor_id = models.AutoField(primary_key=True)
    profesor_nombre = models.CharField(max_length=255)
    profesor_email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tbl_profesor'
