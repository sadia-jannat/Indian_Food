from django.db import models
#image ar time ,date debr jonno bellow

class Location(models.Model):
    city=models.CharField(max_length=100)
    address=models.TextField(max_length=100)   
    cityid=models.PositiveIntegerField()
    zipcode=models.PositiveIntegerField()
    latitude=models.FloatField()
    locality=models.CharField(max_length=100)
    longitude=models.FloatField()
    country_id=models.PositiveIntegerField()
    locality_verbose=models.TextField(max_length=200)

    class Meta:
        db_table='Location'
    

class Rating(models.Model):
    votes=models.PositiveIntegerField()
    rating_text=models.CharField(max_length=100)
    rating_color=models.CharField(max_length=100)
    aggregate_rating=models.FloatField()

    class Meta:
        db_table='Rating'



class Details(models.Model):
    name=models.CharField(max_length=100)
    offer=models.CharField(max_length=100)
    cuisines=models.TextField(max_length=300)
    detailslocation=models.ForeignKey(Location, on_delete=models.CASCADE)
    price_range=models.IntegerField()
    user_rating=models.ForeignKey(Rating, on_delete=models.CASCADE)
    mezzo_provider=models.CharField(max_length=100)
    order_deeplink=models.URLField(max_length=100)
    has_table_booking=models.PositiveIntegerField()
    is_delivering_now=models.PositiveIntegerField()
    opentable_support=models.PositiveIntegerField()
    has_online_delivery=models.PositiveIntegerField()
    include_bogo_offers=models.BooleanField(default=False)
    average_cost_for_two=models.PositiveIntegerField()
    switch_to_order_menu=models.PositiveIntegerField()
    is_book_form_web_view=models.PositiveIntegerField()
    book_form_web_view_url=models.URLField(max_length=100)
    is_table_reservation_supported=models.PositiveIntegerField()

    class Meta:
        db_table='Details'

KEYVALUE=(
    
)


class Food(models.Model):
    primaryid=models.PositiveIntegerField()
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    items=models.CharField(choices=KEYVALUE, max_length=200) 
    lat_long=models.CharField(max_length=200)
    full_details=models.ForeignKey(Details, on_delete=models.CASCADE)
      
    class Meta:
        db_table='Food'  