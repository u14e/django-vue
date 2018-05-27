# coding: utf-8
import datetime
import re
from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import VerifyCode


User = get_user_model()


def phone_validate(phone):
    if not re.match(r'^1\d{10}$', phone):
        raise serializers.ValidationError('手机号格式不正确')


class VerifyCodeSerializer(serializers.Serializer):
    """
    验证码序列
    """
    phone = serializers.CharField(max_length=30, validators=[phone_validate])

    def validate_phone(self, phone):
        """
        验证手机号
        """
        passed = timezone.now() - datetime.timedelta(minutes=1)
        if VerifyCode.objects.filter(phone=phone, created_time__gt=passed).exists():
            raise serializers.ValidationError('距离上次发送未超过60s')
        return phone


class UserRegisterSerializer(serializers.Serializer):
    """
    用户注册序列
    """
    phone = serializers.CharField(max_length=11, validators=[phone_validate])
    code = serializers.CharField(max_length=10, write_only=True)
    password = serializers.CharField(max_length=250, write_only=True)

    def validate(self, attrs):
        phone = attrs['phone']
        code = attrs['code']

        # 验证手机号
        m = User.objects.filter(phone=phone)
        if m:
            raise serializers.ValidationError('手机号已经被注册了')

        # 验证code
        code_for_user = VerifyCode.objects.filter(phone=phone).order_by('-created_time')
        if code_for_user:
            last_code = code_for_user[0]
            passed = timezone.now() - datetime.timedelta(minutes=5)
            if last_code.created_time < passed:
                raise serializers.ValidationError('验证码过期')
            if last_code.code != code:
                raise serializers.ValidationError('验证码错误')
        else:
            raise serializers.ValidationError("验证码错误")

        return attrs

    def create(self, validated_data):
        data = dict(
            phone=validated_data['phone'],
            password=validated_data['password']
        )
        m = User(**data)
        m.set_password(data['password'])
        m.save()
        return m


class UserSerializer(serializers.ModelSerializer):
    """
    用户信息序列
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'phone', 'date_joined')
