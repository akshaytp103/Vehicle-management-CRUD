from django import forms
from .models import Vehicles


class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicles
        fields = '__all__'
        # labels = {
        #     'fullname':'Full Name',
        #     'emp_code':'EMP. Code'
        # }

    def __init__(self, *args, **kwargs):
        super(VehicleForm,self).__init__(*args, **kwargs)
        self.fields['vehicle_number'].empty_label = "Select"
        self.fields['vehicle_number'].required = False