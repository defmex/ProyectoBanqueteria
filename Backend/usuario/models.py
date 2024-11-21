from django.db import models
import bcrypt

# Create your models here.
class Cliente(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(auto_now_add=True)
    nickname = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellido1}"
    
    def save(self, *args, **kwargs):
        # Verifica si la contraseña es nueva o ha cambiado
        if self._state.adding or 'password' in self.get_dirty_fields():
            salt = bcrypt.gensalt()
            self.password = bcrypt.hashpw(self.password.encode('utf-8'), salt).decode('utf-8')
        super().save(*args, **kwargs)


    def check_password(self, raw_password):
        # Verifica la contraseña
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))
    

class Trabajador(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(auto_now_add=True)
    nickname = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    rango = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido1}"
    
    def save(self, *args, **kwargs):
        # Verifica si la contraseña es nueva o ha cambiado
        if self._state.adding or 'password' in self.get_dirty_fields():
            salt = bcrypt.gensalt()
            self.password = bcrypt.hashpw(self.password.encode('utf-8'), salt).decode('utf-8')
        super().save(*args, **kwargs)


    def check_password(self, raw_password):
        # Verifica la contraseña
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))