from django import forms
from .models import Center, Doner


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Doner
        fields = (
            'first_name',
            'last_name',
            'email',
            'mobile_number',
            'address_line_1',
            'address_line_2',
            'gender',
            'blood_group',
            'district',
            'center',
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['center'].queryset = Center.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['center'].queryset = Center.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['center'].queryset = self.instance.district.center_set.order_by('name')