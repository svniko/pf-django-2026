from django import forms
from .models import Passenger, Flight
from django.forms import ModelForm

class BookingForm(forms.Form):
    passenger = forms.ModelChoiceField(
        queryset=Passenger.objects.none(),
        empty_label="Оберіть пасажира",
        widget=forms.Select(attrs={
            "class": "form-select w-50",
           
        })
    )

    def __init__(self, *args, **kwargs):
        non_passengers = kwargs.pop("non_passengers", None)

        super().__init__(*args, **kwargs)

        if non_passengers is not None:
            self.fields["passenger"].queryset = non_passengers


class FlightForm(ModelForm):
    class Meta:
        model=Flight
        fields = ['origin','destination','duration']
        # fields = '__all__' # for all fiels
        widgets = {
            'origin': forms.Select(attrs={
                'class': 'form-select mb-3 w-50',
               
            }),

            'destination': forms.Select(attrs={
                'class': 'form-select mb-3 w-50',
                
            }),

            'duration': forms.NumberInput(attrs={
                'class': 'form-control mb-3 w-50',
                'placeholder': 'Тривалість польоту'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['origin'].empty_label = "Звідки"
        self.fields['destination'].empty_label = "Куди"