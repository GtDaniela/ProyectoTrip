from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Viajero(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    telefono=models.CharField("telefono viajero",max_length=20,null=True,blank=True)
    alias=models.CharField("nombre de usuario",max_length=20,null=True,blank=True)
    foto_perfil=models.ImageField("foto de perfil",null=True,blank=True)
    sexo=models.CharField("sexo del viajero",null=True,blank=True)
    fecha_nacimiento=models.DateTimeField("fecha de nacimiento",null=True,blank=True)
    fecha_alta=models.DateTimeField("fecha de alta",null=True,blank=True)
    conectado=models.BooleanField("estado del viajero",null=True,blank=True)
    verificado=models.BooleanField("cuenta verificada",null=True,blank=True)

    class meta:
        verbose_name='Viajero'
        verbose_name_plural="Viajeros"
        ordering=['user']

    def __str__(self):
        return "%s,%s,%s" % (self.id,self.alias,self.foto_perfil)

class Video(models.Model):
    id=models.AutoField(primary_key=True)
    video=models.FileField("video de publicacion",null=True,blank=True)

    class meta:
        verbose_name='Video'
        verbose_name_plural='Videos'
        ordering=['id']

    def __str__(self):
        return "%s, %s" % (self.id,self.video)

class Foto(models.Model):
    id = models.AutoField(primary_key=True)
    foto = models.FileField("foto de publicacion", null=True, blank=True)

    class meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ['id']

    def __str__(self):
        return "%s, %s" % (self.id,self.foto)

class Publicacion(models.Model):
    id=models.AutoField(primary_key=True)
    viajero=models.ForeignKey(Viajero,related_name="publicacion_viajero",on_delete=models.PROTECT,null=True,blank=True)
    texto=models.TextField("texto publicado",null=True,blank=True)
    video=models.ForeignKey(Video, related_name="publicacion_video",on_delete=models.PROTECT,null=True,blank=True)
    foto=models.ForeignKey(Foto,related_name="publicacion_foto",on_delete=models.PROTECT,null=True,blank=True)
    tiempo=models.DateTimeField(default=timezone.now)
    like_activo=models.BooleanField("like acitvo o no")

    class meta:
        verbose_name='Publicacion'
        verbose_name_plural="Plublicaciones"
        ordering=['-tiempo']

    def __str__(self):
        return "%s,%s,%s,%s" % (self.viajero,self.texto,self.video,self.foto)


class Comentario(models.Model):
    id=models.AutoField(primary_key=True)
    comentario=models.TextField("comentario",null=True,blank=True)

    class meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['id']

    def __str__(self):
        return "%s, %s" % (self.id,self.comentario)

class Like(models.Model):
    id=models.AutoField(primary_key=True)
    like=models.TextField("comentario",null=True,blank=True)

    class meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        ordering = ['id']

    def __str__(self):
        return "%s, %s" % (self.id,self.like)


#preguntar la foreingkey

class Seguidor(models.Model):
    id=models.AutoField(primary_key=True)
    viajero_seguido=models.ForeignKey(Viajero,related_name="seguido_viajero",on_delete=models.PROTECT,null=True,blank=True)
    seguidor_viajero=models.ForeignKey(Viajero,related_name="seguidor_viajero",on_delete=models.PROTECT,null=True,blank=True)

    class meta:
        verbose_name = 'Seguidor'
        verbose_name_plural = 'Seguidores'
        ordering = ['id']

    def __str__(self):
        return "%s, %s" % (self.id,self.viajero_seguido)


class Seguido(models.Model):
    id = models.AutoField(primary_key=True)
    viajero_seguido = models.ForeignKey(Viajero,related_name="viajero_seguido",on_delete=models.PROTECT,null=True, blank=True)
    seguidor_viajero = models.ForeignKey(Viajero,related_name="viajero_seguidor",on_delete=models.PROTECT,null=True, blank=True)

    class meta:
        verbose_name = 'Seguido'
        verbose_name_plural = 'Seguidos'
        ordering = ['id']

    def __str__(self):
        return "%s, %s" % (self.id,self.viajero_seguido)

class Alojamiento(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, related_name="dueño_vivienda",on_delete=models.PROTECT,null=True, blank=True)
    direccion=models.CharField("direccion_alojamiento",max_length=30,null=True,blank=True)
    poblacion=models.CharField("poblacion_alojamiento",max_length=20,null=True,blank=True)
    provincia=models.CharField("provincia_alojamiento",max_length=20,null=True,blank=True)
    foto=models.ImageField("Foto_alojamiento",upload_to='foto_alojamiento',null=True,blank=True)
    cp=models.CharField(max_length=10,null=True,blank=True)
    fecha_alta=models.DateField(auto_now=True)

    class meta:
        verbose_name = 'Alojamiento'
        verbose_name_plural = 'Alojamientos'
        ordering = ['id']

    def __str__(self):
        return "%s, %s" % (self.id,self.direccion)

class Prestar_alojamiento(models.Model):
    id=models.AutoField(primary_key=True)
    alojamiento=models.ForeignKey(Alojamiento,related_name="vivienda_prestar",on_delete=models.PROTECT,null=True, blank=True)
    viajero=models.ForeignKey(Viajero,related_name="viajero_presta",on_delete=models.PROTECT,null=True, blank=True)
    fecha_inicio=models.DateField("fecha de inicio",null=True,blank=True)
    fecha_fin=models.DateField("Fecha de fin",null=True,blank=True)
    realizado=models.BooleanField("prestado",null=True,blank=True)
    reservado=models.BooleanField("reservado0",null=True,blank=True)
    duracion=models.TimeField("duracion",null=True,blank=True)

    class meta:
        verbose_name = 'Prestar_alojamiento'
        verbose_name_plural = 'Prestar_alojamientos'
        ordering = ['id']

    def __str__(self):
        return "%s, %s" % (self.id,self.alojamiento)


class Alojamiento_prestado(models.Model):
    id=models.AutoField(primary_key=True)
    alojamiento=models.ForeignKey(Alojamiento,related_name="vivienda_prestada",on_delete=models.PROTECT,null=True, blank=True)
    viajero=models.ForeignKey(Viajero,related_name="viajero_alojado",on_delete=models.PROTECT,null=True, blank=True)
    fecha_inicio=models.DateField("fecha de inicio ",null=True,blank=True)
    fecha_fin=models.DateField("Fecha de fin",null=True,blank=True)
    realizado=models.BooleanField("prestado",null=True,blank=True)
    reservado=models.BooleanField("reservado0",null=True,blank=True)
    duracion=models.TimeField("duracion",null=True,blank=True)

    class meta:
        verbose_name = 'Alojamiento_prestado'
        verbose_name_plural = 'Alojamientos_prestados'
        ordering = ['id']

    def __str__(self):
        return "%s, %s" % (self.id,self.alojamiento)
