# from django.db import models

# class Destination(models.Model):
#     destination_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     location = models.CharField(max_length=255)
#     average_rating = models.FloatField(default=0.0)

#     def __str__(self):
#         return self.name

# class Hotel(models.Model):
#     hotel_id = models.AutoField(primary_key=True)
#     destination_id = models.ForeignKey(Destination, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
#     rating = models.FloatField(default=0.0)

#     def __str__(self):
#         return self.name

# class Restaurant(models.Model):
#     restaurant_id = models.AutoField(primary_key=True)
#     destination_id = models.ForeignKey(Destination, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     cuisine = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     rating = models.FloatField(default=0.0)

#     def __str__(self):
#         return self.name

# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=150, unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)  # Store hashed passwords

#     def __str__(self):
#         return self.username

# class Review(models.Model):
#     review_id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     destination_id = models.ForeignKey(Destination, on_delete=models.CASCADE)
#     rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 stars
#     comment = models.TextField(blank=True, null=True)
#     date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"Review by {self.user_id} for {self.destination_id}"
