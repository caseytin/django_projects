from django.forms import ModelForm
from wizards.models import House

# Create the form class.
class HouseForm(ModelForm):
    class Meta:
        model = House
        fields = '__all__'