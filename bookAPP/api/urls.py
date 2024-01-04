from django.urls import path
from bookAPP.views import (
    EbookDetailView, EbookListCreateAPIView, 
    ReviewCreateAPIView, ReviewDetailView
)

urlpatterns = [
    path("ebook/", 
         EbookListCreateAPIView.as_view(), 
         name="ebook-list"),

    path("ebook/<int:pk>/", 
         EbookDetailView.as_view(), 
         name="ebook-detail"),

    path("ebook/<int:ebook_pk>/review/", 
         ReviewCreateAPIView.as_view(), 
         name="ebook-review"),

    path("reviews/<int:pk>/", 
         ReviewDetailView.as_view(), 
         name="review-detail"),

]