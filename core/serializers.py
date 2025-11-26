
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Paciente, ProfissionalSaude, Consulta   

User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','first_name','last_name','role']

class PacienteSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Paciente
        fields = ['id', 'user', 'cpf', 'data_nascimento', 'telefone']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data.get('email', ''),
            first_name=user_data.get('first_name', ''),
            last_name=user_data.get('last_name', ''),
            password=user_data.get('password', '123456'),
            role=User.Role.PACIENTE
        )
        paciente = Paciente.objects.create(user=user, **validated_data)
        return paciente

    def update(self, instance, validated_data):
        # Atualiza os campos do paciente
        user_data = validated_data.pop('user', None)

        # Atualiza campos simples do paciente
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Atualiza o usuário relacionado (se fornecido)
        if user_data:
            user = instance.user
            # Atualize apenas os campos permitidos. Não recrie o usuário.
            username = user_data.get('username')
            email = user_data.get('email')
            first_name = user_data.get('first_name')
            last_name = user_data.get('last_name')
            password = user_data.get('password', None)

            # Se username for alterado, verifique unicidade manualmente
            if username and username != user.username:
                if User.objects.filter(username=username).exclude(pk=user.pk).exists():
                    raise serializers.ValidationError({'user': {'username': ['Um usuário com este nome de usuário já existe.']}})
                user.username = username

            if email is not None:
                user.email = email
            if first_name is not None:
                user.first_name = first_name
            if last_name is not None:
                user.last_name = last_name
            if password:
                user.set_password(password)

            user.save()

        return instance


from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from .models import ProfissionalSaude

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','role']

class ProfissionalSaudeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ProfissionalSaude
        fields = ['id', 'user', 'especialidade', 'registro_conselho']

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        if not user_data:
            raise serializers.ValidationError({'user': 'Dados do usuário são obrigatórios.'})

        try:
            with transaction.atomic():
                # cria user com validação de unicidade tratada
                user = User.objects.create_user(
                    username=user_data['username'],
                    email=user_data.get('email',''),
                    first_name=user_data.get('first_name',''),
                    last_name=user_data.get('last_name',''),
                    password=user_data.get('password','123456'),
                    role=User.Role.PROF if hasattr(User, 'Role') else getattr(User, 'role', None)
                )
                profissional = ProfissionalSaude.objects.create(user=user, **validated_data)
            return profissional
        except IntegrityError as e:
            # transforma erro de banco em ValidationError amigável
            msg = str(e)
            # tenta detectar unicidade de username / registro_conselho
            if 'username' in msg or 'auth_user_username' in msg or 'unique' in msg.lower():
                raise serializers.ValidationError({'user': {'username': ['Um usuário com este nome de usuário já existe.']}})
            if 'registro_conselho' in msg or 'profissional_saude_registro_conselho_key' in msg:
                raise serializers.ValidationError({'registro_conselho': ['Registro de conselho já existe.']})
            # fallback
            raise serializers.ValidationError({'detail': 'Erro ao criar profissional: ' + msg})
        except KeyError as e:
            raise serializers.ValidationError({'user': f'Campo obrigatório do user ausente: {e}'})


class ConsultaSerializer(serializers.ModelSerializer):
    paciente = serializers.PrimaryKeyRelatedField(queryset=Paciente.objects.all())
    profissional = serializers.PrimaryKeyRelatedField(queryset=ProfissionalSaude.objects.all())

    class Meta:
        model = Consulta
        fields = [
            'id',
            'paciente',
            'profissional',
            'data_hora',
            'tipo',
            'status',
            'descricao',
            'criado_em',
            'atualizado_em'
        ]
        read_only_fields = ['criado_em', 'atualizado_em']

    def validate_data_hora(self, value):
        # opcional: validar que data_hora é futura, formato, etc.
        return value

    def create(self, validated_data):
        try:
            with transaction.atomic():
                # cria a consulta; se FK inválido, PrimaryKeyRelatedField já valida antes
                consulta = Consulta.objects.create(**validated_data)
                return consulta
        except IntegrityError as e:
            # transforma erro de banco em 400
            raise serializers.ValidationError({'detail': 'Erro de integridade ao criar consulta: ' + str(e)})
        except Exception as e:
            # evita 500 — converte para 400 com mensagem útil
            raise serializers.ValidationError({'detail': 'Erro ao criar consulta: ' + str(e)})