from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import *
from nurse.models import Nurse
from patient.models import Patient
from pharmacist.models import Pharmacist
from radiologist.models import Radiologist
from receptionist.models import Receptionist


class user_form(UserCreationForm):
    class Meta:
        model = User
        fields = ('role',)


class UserRegistrationForm(forms.Form):
    speciality_choice = [('Internal medicine', 'Internal medicine'), ('Pediatrics', 'Pediatrics'), ('Dermatology', 'Dermatology'),
                         ('Ophthalmology', 'Ophthalmology'), ('Oncology', 'Oncology'), ('Obstetrics', 'Obstetrics')
                         ]
    role_choices = [('Receptionist', 'Receptionist'), ('Physician', speciality_choice), ('Nurse', 'Nurse'),
                    ('Radiologist', 'Radiologist'), ('Lab_technician', 'Lab_technician'),
                    ('Pharmacist', 'Pharmacist')]
    sex_choices = [('Male', 'Male'), ('Female', 'Female')]
    region_choice = (
        ("Tigray", "Tigray"), ("Afar", "Afar"), ("Amhara", "Amhara"), ("Oromia", "Oromia"), ("Somali", "Somali"),
        ("Benishangul-Gumuz", "Benishangul-Gumuz"), ("Gambela", "Gambela"), ("Harari", "Harari"), ("Sidama", "Sidama"),
        (
            "Southern Nations, Nationalities, and Peoples' Region",
            "Southern Nations, Nationalities, and Peoples' Region"),
        ("Addis Ababa", "Addis Ababa"), ("Dire Dawa", "Dire Dawa")
    )
    firstname = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name here... '}))
    middlename = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Middle Name here... '}))
    lastname = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name here... '}))
    sex = forms.CharField(required=True, max_length=10,
                          widget=forms.Select(choices=sex_choices,
                                              attrs={'class': 'form-control', 'placeholder': 'Sex here... '}))
    age = forms.IntegerField(required=True,
                             widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age here... '}))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email here... '}))
    region = forms.CharField(required=True,
                             widget=forms.Select(choices=region_choice,
                                                 attrs={'class': 'form-control', 'placeholder': 'Region here.. '}))
    zone = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zone here... '}))
    woreda = forms.CharField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Woreda here... '}))
    kebele = forms.CharField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kebele here... '}))
    house_no = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'House No here...'}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Phone number here..'}))
    role = forms.CharField(required=False, max_length=50, widget=forms.Select(choices=role_choices,
                                                                              attrs={'class': 'form-control',
                                                                                     'placeholder': 'Role here... '}))

    def save_patient(self, context):
        password = User.objects.make_random_password()
        count = User.objects.count()
        new_patient_address = Address.objects.create(
            region=self.cleaned_data.get('region'),
            zone=self.cleaned_data.get('zone'),
            woreda=self.cleaned_data.get('woreda'),
            kebele=self.cleaned_data.get('kebele'),
            house_no=self.cleaned_data.get('house_no'),
        )
        new_patient_info = User.objects.create(
            first_name=self.cleaned_data.get('firstname'),
            last_name=self.cleaned_data.get('lastname'),
            middle_name=self.cleaned_data.get('middlename'),
            email=self.cleaned_data.get('email'),
            sex=self.cleaned_data.get('sex'),
            age=self.cleaned_data.get('age'),
            address_id=new_patient_address.id,
            phone=self.cleaned_data.get('phone'),
            role="patient",
            username=self.cleaned_data.get('firstname') + str(count),

        )
        new_patient = Patient.objects.create(
            basic_id=new_patient_info.id,
        )

        new_patient_info.set_password(password)
        new_patient_address.save()
        new_patient_info.save()
        new_patient.save()
        new_patient.hospital.add(context['hospital'])
        print(new_patient_info.username, password)
        context = {'username': new_patient_info.username, "password": password}
        return context

    def save_pharmacist(self, context):
        password = User.objects.make_random_password()
        count = User.objects.count()
        new_pharmacist_address = Address.objects.create(
            region=self.cleaned_data.get('region'),
            zone=self.cleaned_data.get('zone'),
            woreda=self.cleaned_data.get('woreda'),
            kebele=self.cleaned_data.get('kebele'),
            house_no=self.cleaned_data.get('house_no'),
        )

        new_pharmacist_info = User.objects.create(
            first_name=self.cleaned_data.get('firstname'),
            last_name=self.cleaned_data.get('lastname'),
            middle_name=self.cleaned_data.get('middlename'),
            email=self.cleaned_data.get('email'),
            sex=self.cleaned_data.get('sex'),
            age=self.cleaned_data.get('age'),
            address_id=new_pharmacist_address.id,
            phone=self.cleaned_data.get('phone'),
            role="pharmacist",
            username=self.cleaned_data.get('firstname') + str(count),

        )

        new_pharmacist = Pharmacist.objects.create(
            basic_id=new_pharmacist_info.id,
            pharmacy_id=context['pharmacy'].id,
        )

        new_pharmacist_info.set_password(password)
        new_pharmacist_address.save()
        new_pharmacist_info.save()
        new_pharmacist.save()
        print(new_pharmacist_info.username, password)
        context = {'username': new_pharmacist_info.username, "password": password}
        return context

    def save(self, context):
        password = User.objects.make_random_password()
        count = User.objects.count()
        new_staff_address = Address.objects.create(
            region=self.cleaned_data.get('region'),
            zone=self.cleaned_data.get('zone'),
            woreda=self.cleaned_data.get('woreda'),
            kebele=self.cleaned_data.get('kebele'),
            house_no=self.cleaned_data.get('house_no'),
        )
        r = None
        s = None

        if self.cleaned_data.get('role') == 'Oncology':
            r = 'Physician'
            s = self.cleaned_data.get('role')
        elif self.cleaned_data.get('role') == 'Internal medicine':
            r = 'Physician'
            s = self.cleaned_data.get('role')
        elif self.cleaned_data.get('role') == 'Pediatrics':
            r = 'Physician'
            s = self.cleaned_data.get('role')
        elif self.cleaned_data.get('role') == 'Dermatology':
            r = 'Physician'
            s = self.cleaned_data.get('role')
        elif self.cleaned_data.get('role') == 'Ophthalmology':
            r = 'Physician'
            s = self.cleaned_data.get('role')
        elif self.cleaned_data.get('role') == 'Obstetrics':
            r = 'Physician'
            s = self.cleaned_data.get('role')
        else:
            r = self.cleaned_data.get('role')
            s = None
        print(r)
        print(s)
        print(self.cleaned_data.get('role'))

        new_staff_basic = User.objects.create(
            first_name=self.cleaned_data.get('firstname'),
            last_name=self.cleaned_data.get('lastname'),
            middle_name=self.cleaned_data.get('middlename'),
            email=self.cleaned_data.get('email'),
            sex=self.cleaned_data.get('sex'),
            address_id=new_staff_address.id,
            age=self.cleaned_data.get('age'),
            phone=self.cleaned_data.get('phone'),
            username=self.cleaned_data.get('firstname') + str(count),
            role=r,
        )
        staff = Staff.objects.create(
            basic_id=new_staff_basic.id,
            hospital_id=context['hospital'].id,
            specialty=s,
        )
        staff.save()
        new_staff_basic.set_password(password)
        new_staff_basic.save()
        new_staff_address.save()

        print(new_staff_basic.username, password)
        context = {'username': new_staff_basic.username, "password": password}
        return context

    def save_admin(self, admin_type):

        password = User.objects.make_random_password()
        count = User.objects.count()
        new_user_address = Address.objects.create(
            region=self.cleaned_data.get('region'),
            zone=self.cleaned_data.get('zone'),
            woreda=self.cleaned_data.get('woreda'),
            kebele=self.cleaned_data.get('kebele'),
            house_no=self.cleaned_data.get('house_no'),
        )
        new_user = User.objects.create(

            first_name=self.cleaned_data.get('firstname'),
            last_name=self.cleaned_data.get('lastname'),
            middle_name=self.cleaned_data.get('middlename'),
            email=self.cleaned_data.get('email'),
            sex=self.cleaned_data.get('sex'),
            age=self.cleaned_data.get('age'),
            address_id=new_user_address.id,
            phone=self.cleaned_data.get('phone'),
            username=self.cleaned_data.get('firstname') + str(count),
            role=admin_type,

        )

        new_user.set_password(password)
        new_user_address.save()
        new_user.save()
        print(new_user.username, password)
        context = {'username': new_user.username, "password": password, "admin_id": new_user.id}
        return context
