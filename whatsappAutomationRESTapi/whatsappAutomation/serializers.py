from rest_framework import serializers

from .models import LoginAccount


class LoginSerializer(serializers.ModelSerializer):
  text = serializers.CharField(max_length=30, required=True)

  def create(self, validated_data):
    # Once the request data has been validated, we can create a account in the database
    return LoginAccount.objects.create(
      text=validated_data.get('first_name')
    )

  def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the account in the database
    instance.text = validated_data.get('first_name', instance.text)
    instance.save()
    return instance

  class Meta:
    model = LoginAccount
    fields = (
      'first_name'
    )