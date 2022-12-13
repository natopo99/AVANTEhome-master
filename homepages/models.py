from django.db import models

# Create your models here.
class HomeDetails(models.Model):
    price = models.IntegerField(default = 0)
    square_ft = models.IntegerField(default = 0)
    beds = models.IntegerField(default = 0)
    baths = models.IntegerField(default = 0)
    garage_spaces = models.IntegerField(default = 0)
    street_address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 2)
    lot_size = models.IntegerField(default = 0)
    year_built = models.IntegerField(default = 0)
    days_listed = models.IntegerField(default = 0)
    #house_pic = models.CharField(max_length = 100)

    def __str__ (self):
        return (self.house_name)

    @property
    def house_name(self):
        return '%s %s %s' % (self.street_address, self.city, self.state)

    class Meta:
        verbose_name_plural = 'Home Data'
