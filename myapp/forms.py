from django import forms
from .models import BookingList,AdminEditList

class BookingListForm(forms.ModelForm):
    class Meta:
        model=BookingList
        fields='__all__'
        widgets = {
            'date_of_booking': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'in_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'out_time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

class AdminEditListForm(forms.ModelForm):
    class Meta:
        model=AdminEditList
        fields='__all__'