from django import forms
from .models import BookingList
class BookingListForm(forms.ModelForm):
    class Meta:
        model=BookingList
        fields=['name','occupancy','in_time','out_time']
        widgets = {
            'date_of_booking': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'in_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'out_time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }