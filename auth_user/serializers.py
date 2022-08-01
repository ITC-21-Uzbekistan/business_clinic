from rest_framework.serializers import ModelSerializer
from auth_user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'profile_image',
            'is_admin',
            'is_staff',
            'is_active',
            'gender',
            'region',
            'phone',
            'passport',
            'category_employee',
            'date_joined',
        )

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.profile_image = validated_data.get('profile_image',  instance.profile_image)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.region = validated_data.get('region', instance.region)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.passport = validated_data.get('passport', instance.passport)
        instance.category_employee = validated_data.get('category_employee', instance.category_employee)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        return instance
