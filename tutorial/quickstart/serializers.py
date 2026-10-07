from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Alumno, Carrera, Materia, Inscripcion, Card
from django.contrib.auth.password_validation import validate_password


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
    password = serializers.CharField(
        write_only=True, 
        min_length=6,
        required=True, 
        validators=[validate_password]
    )

    email = serializers.EmailField(required = True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value) .exists():
            raise serializers.ValidationError("Ya existe una cuenta con este correo.")
        return value
        
    def validate_username(self, value):
        if User.objects.filter(username__iexact=value) .exists():
            raise serializers.ValidationError("Este nombre de usuario ya está registrado.")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    