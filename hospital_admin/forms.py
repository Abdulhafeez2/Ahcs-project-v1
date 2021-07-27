from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from login.models import User




class user_form(UserCreationForm):
    class Meta:
        model = User
        fields = ('role',)


class User_registeration_Form(forms.Form):
    role_choices = [('Receptionist', 'Receptionist'), ('Physician', 'Physician'), ('Nurse', 'Nurse'),
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
    role = forms.CharField(required=False, max_length=50, widget=forms.Select(choices=role_choices, attrs={'class': 'form-control', 'placeholder': 'Role here... '}))

    def save_patient(self):
        password = User.objects.make_random_password()
        count = User.objects.count()

        new_user = User.objects.create(
            first_name=self.cleaned_data.get('firstname'),
            last_name=self.cleaned_data.get('lastname'),
            middle_name=self.cleaned_data.get('middlename'),
            email=self.cleaned_data.get('email'),
            sex=self.cleaned_data.get('sex'),
            age=self.cleaned_data.get('age'),
            region=self.cleaned_data.get('region'),
            zone=self.cleaned_data.get('zone'),
            woreda=self.cleaned_data.get('woreda'),
            kebele=self.cleaned_data.get('kebele'),
            house_no=self.cleaned_data.get('house_no'),
            phone=self.cleaned_data.get('phone'),
            role="patient",
            username=self.cleaned_data.get('firstname') + str(count),

        )
        new_user.set_password(password)
        new_user.save()
        print(new_user.username, password)
        context = {'username': new_user.username, "password": password}
        return context

    def save(self):
        password = User.objects.make_random_password()
        count = User.objects.count()

        new_user = User.objects.create(

            first_name=self.cleaned_data.get('firstname'),
            last_name=self.cleaned_data.get('lastname'),
            middle_name=self.cleaned_data.get('middlename'),
            email=self.cleaned_data.get('email'),
            sex=self.cleaned_data.get('sex'),
            age=self.cleaned_data.get('age'),
            region=self.cleaned_data.get('region'),
            zone=self.cleaned_data.get('zone'),
            woreda=self.cleaned_data.get('woreda'),
            kebele=self.cleaned_data.get('kebele'),
            house_no=self.cleaned_data.get('house_no'),
            phone=self.cleaned_data.get('phone'),
            username=self.cleaned_data.get('firstname') + str(count),
            role=self.cleaned_data.get('role'),
        )
        new_user.set_password(password)
        new_user.save()
        print(new_user.username, password)
        context = {'username': new_user.username, "password": password}
        return context

    def save_admin(self):
        password = User.objects.make_random_password()
        count = User.objects.count()

        new_user = User.objects.create(

            first_name=self.cleaned_data.get('firstname'),
            last_name=self.cleaned_data.get('lastname'),
            middle_name=self.cleaned_data.get('middlename'),
            email=self.cleaned_data.get('email'),
            sex=self.cleaned_data.get('sex'),
            age=self.cleaned_data.get('age'),
            region=self.cleaned_data.get('region'),
            zone=self.cleaned_data.get('zone'),
            woreda=self.cleaned_data.get('woreda'),
            kebele=self.cleaned_data.get('kebele'),
            house_no=self.cleaned_data.get('house_no'),
            phone=self.cleaned_data.get('phone'),
            username=self.cleaned_data.get('firstname') + str(count),
            role="hospital admin"
        )
        new_user.set_password(password)
        new_user.save()
        print(new_user.username, password)
        context = {'username': new_user.username, "password": password}
        return context

