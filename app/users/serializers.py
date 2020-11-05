from .models import User, User_Info
from rest_framework import serializers


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Info
        fields = ['email', 'mobile']


class UserSerializer(serializers.ModelSerializer):
    # 筆記: 需要與Model內的OneToOneField的related_name對應，需要再了解原理。
    # users = UserInfoSerializer()
    communicate_information = UserInfoSerializer()

    class Meta:
        model = User
        fields = ['id', 'name', 'job_title', 'communicate_information']

    def create(self, validated_data):
        # 將遷套communicate_information的數據取出
        communicate_information_data = validated_data.pop('communicate_information')
        # 建立User
        user = User.objects.create(**validated_data)
        # 將剛才取出的communicate_information以及user實例(onetoone)作為參數傳入。
        User_Info.objects.create(user=user, **communicate_information_data)

        return user

    def update(self, instance, validated_data):
        communicate_information_data = validated_data.pop('communicate_information')

        communicate_information = instance.communicate_information

        instance.name = validated_data.get('name', instance.name)
        instance.job_title = validated_data.get('job_title', instance.job_title)
        instance.save()

        communicate_information.email = communicate_information_data.get('email', communicate_information.email)
        communicate_information.mobile = communicate_information_data.get('mobile', communicate_information.mobile)
        
        communicate_information.save()
        return instance
