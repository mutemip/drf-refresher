from rest_framework import serializers
from bookAPP.models import Review, Ebook

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ("ebook",)

class EbookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Ebook
        fields = "__all__"