from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from .models import Ebook, Review
from api.serializers import EbookSerializer, ReviewSerializer

# Create your views here.
class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

class EbookDetailView(generics.RetrieveUpdateDeleteAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        serializer.save(ebook=ebook)


class ReviewDetailView(generics.RetrieveUpdateDeleteAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer