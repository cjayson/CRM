from rest_framework import serializers
from .models import StaffInfo
import re


# 登录验证序列化器
class StaffModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffInfo
        fields = ["id", "username", "mobile", "desc", "gender", "role", "role_power","department"]


# 注册验证序列化器
class RegisterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffInfo
        fields = ["mobile", "id", "password", "username", "desc", "gender", "role", "role_power","department"]
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
        }

    def validate_username(self, username):
        # 验证唯一性
        try:
            user = StaffInfo.objects.get(username=username)
            if user:
                raise serializers.ValidationError("当前账号已经被注册!")

        except:
            pass

        return username

    def validate_mobile(self, mobile):
        # 验证格式
        result = re.match('^1[3-9]\d{9}$', mobile)
        if not result:
            raise serializers.ValidationError("手机号码格式有误!")

        return mobile

    def validate(self, attrs):
        print(attrs, "attrs")

        # 判断密码长度
        password = attrs.get("password")
        if not re.match('^.{1,16}$', password):
            raise serializers.ValidationError("密码长度必须在1-16位之间!")
        role_power = attrs.get("role_power")

        # 判断权限等级
        if role_power not in [1, 2, 3]:
            raise serializers.ValidationError("权限等级不对!")

        return attrs

    def create(self, validated_data):
        """保存用户"""
        username = validated_data.get("username")
        mobile = validated_data.get("mobile")
        password = validated_data.get("password")
        desc = validated_data.get("desc")
        gender = validated_data.get("gender")
        role = validated_data.get("role")
        role_power = validated_data.get("role_power")

        try:
            user = StaffInfo.objects.create(
                mobile=mobile,
                username=username,
                password=password,
                desc=desc,
                gender=gender,
                role=role,
                role_power=role_power
            )

            # 密码加密
            # user.set_password(user.password)   # 测试就不加密了
            user.save()
        except:
            raise serializers.ValidationError("注册用户失败!")

        return user
