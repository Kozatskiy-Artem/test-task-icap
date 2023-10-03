from rest_framework import serializers


class ProductCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    photo = serializers.URLField()
    category = serializers.CharField(max_length=50)
    offer_of_the_month = serializers.BooleanField()
    availability = serializers.BooleanField()
    self_pickup = serializers.BooleanField()
    description1 = serializers.CharField(max_length=500)
    description2 = serializers.CharField(max_length=500)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    photo = serializers.URLField()
    category = serializers.CharField()
    offer_of_the_month = serializers.BooleanField()
    availability = serializers.BooleanField()
    self_pickup = serializers.BooleanField()
    description1 = serializers.CharField()
    description2 = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
