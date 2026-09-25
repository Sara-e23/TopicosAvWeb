from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Alumno, Carrera, Materia, Inscripcion, Card


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = 'url', 'name'

class MateriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'

class CarreraSerializer(serializers.HyperlinkedModelSerializer):
    materias = MateriaSerializer(many=True, read_only=True)
    class Meta:
        model = Carrera
        fields = ['id', 'nombre', 'clave', 'descripcion', 'materias']

class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class InscripcionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inscripcion
        fields = '__all__'

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    password: serializers.CharField(write_only=True, min_lenght=6)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            email= validated_data.get['email', ''],
            password= validated_data['password']
        )