from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = Account
        fields = ("id", "email", "username", "password")
        extra_kwargs = {"id": {"read_only": True}, "password": {"write_only": True}}

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        password = validated_data.pop("password", None)

        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance


# class SocialSerializer(serializers.Serializer):

#     provider = serializers.CharField(max_length=255, required=True)
#     access_token = serializers.CharField(
#         max_length=4096, required=True, trim_whitespace=True
#     )
