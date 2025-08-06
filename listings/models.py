from django.db import models


import uuid

class Property(models.Model):
    property_id = models.UUIDField(
        primary_key=True, db_index=True, default=uuid.uuid4()
    )
    host_id = models.ForeignKey(
        to="User", on_delete=models.CASCADE, related_name="propertiy"
    )
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    location = models.CharField(max_length=200, null=False)
    pricepernight = models.DecimalField(
        max_digits=10, decimal_places=2, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BookingStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    CONFIRMED = "confirmed", "Confirmed"
    CANCELLED = "cancelled", "Cancelled"


class Booking(models.Model):
    booking_id = models.UUIDField(
        primary_key=True, db_index=True, default=uuid.uuid4())
    property_id = models.ForeignKey(
        "Property", db_index=True, on_delete=models.CASCADE, related_name="booking"
    )
    user_id = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="booking"
    )
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False)
    status = models.CharField(
        choices=BookingStatus.choices, default=BookingStatus.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)


class RatingValue(models.IntegerChoices):
    ONE = 1, "1 Star"
    TWO = 2, "2 Stars"
    THREE = 3, "3 Stars"
    FOUR = 4, "4 Stars"
    FIVE = 5, "5 Stars"


class Review(models.Model):
    review_id = models.UUIDField(
        primary_key=True, db_index=True, default=uuid.uuid4())
    property_id = models.ForeignKey(
        "Property", on_delete=models.CASCADE, related_name="review"
    )
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    rating = models.IntegerField(
        choices=RatingValue.choices, default=RatingValue.ONE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


