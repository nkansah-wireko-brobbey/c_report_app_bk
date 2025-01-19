from rest_framework import serializers
from .models import Employee, Phone, Receiving, Shipping

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = '__all__'


class ReceivingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiving
        fields = '__all__'
