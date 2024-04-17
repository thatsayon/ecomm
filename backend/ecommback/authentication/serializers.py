from rest_framework import serializers
from django.contrib.auth import get_user_model
from authentication.models import UserAccount

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User 
        fields = ('email', 'password', 'full_name', 'date_of_birth', 'gender')

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters long.")

        if not any(char.isupper() for char in value):
            raise serializers.ValidationError(
                "Password must contain at least one uppercase letter.")

        if not any(char.islower() for char in value):
            raise serializers.ValidationError(
                "Password must contain at least one lowercase letter.")

        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError(
                "Password must contain at least one digit.")

        if not re.search(r"[!@#$%^&*()_+{}\[\]:;\"'\\|<,>.?/`~-]", value):
            raise serializers.ValidationError(
                "Password must contain at least one special character.")

        validate_password(value)

        return value

    def create(self, validated_data):
        validated_data['is_active'] = False 
        user = UserAccount.objects.create_user(**validated_data)
        return user 
