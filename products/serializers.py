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


class PartialProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True)
    photo = serializers.URLField(required=False, allow_blank=True, allow_null=True)
    category = serializers.CharField(max_length=50, required=False, allow_blank=True, allow_null=True)
    offer_of_the_month = serializers.BooleanField(required=False)
    availability = serializers.BooleanField(required=False)
    self_pickup = serializers.BooleanField(required=False)
    description1 = serializers.CharField(max_length=500, required=False, allow_blank=True, allow_null=True)
    description2 = serializers.CharField(max_length=500, required=False, allow_blank=True, allow_null=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)


class GetProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    photo = serializers.URLField()
    category = serializers.CharField()
    offer_of_the_month = serializers.BooleanField()
    availability = serializers.BooleanField()
    self_pickup = serializers.BooleanField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
