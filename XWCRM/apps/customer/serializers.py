from rest_framework import serializers
from .models import Customer
import re

class PublicCutomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["name", "mobile", "age", "desc", "owner", "status"]

class CutomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["name", "mobile", "age", "desc", "owner", "status"]


    def validate_mobile(self, mobile):
        # 验证格式
        result = re.match('^1[3-9]\d{9}$', mobile)
        if not result:
            raise serializers.ValidationError("手机号码格式有误!")

        return mobile


    def create(self, validated_data):
        """保存用户"""
        name = validated_data.get("name")
        mobile = validated_data.get("mobile")
        status = validated_data.get("status")
        desc = validated_data.get("desc")
        age = validated_data.get("age")
        owner = int(validated_data.get("owner"))


        try:
            user = Customer.objects.create(
                mobile=mobile,
                name=name,
                desc=desc,
                age=age,
                status=status,
                owner=owner
            )

            user.save()
        except:
            raise serializers.ValidationError("创建客户失败!")

        return user
