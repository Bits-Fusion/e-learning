from django.contrib.auth import get_user_model


from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_name', 
            'email',
            'gender',
            'age',
            'premium_user',
            'get_update_path'
        ]