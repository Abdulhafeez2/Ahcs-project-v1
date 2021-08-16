import datetime

from django import forms
from django.http import request

from accounts.models import Hospital, User, Staff
from patient.models import PatientForm, Prescription, AdministeredTreatment, XrayExamination, UltraSound
from physician.models import Referral


class AddPatientForm(forms.Form):
    note = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=True)

    def save_patient_form(self, context):
        patient_form = PatientForm.objects.create(
            hospital_id=context['hospital'].id,
            patient_id=context['patient'].id,
            note=self.cleaned_data.get('note'),
            filled_by_id=context['staff'].id,
            date=datetime.datetime.now()
        )
        patient_form.save()


class ReferralRequestForm(forms.Form):
    health_problem_identified_in_detail = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),
                                                          required=True)
    identified_disease_type = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'disease type here... '}))
    action_taken = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'action taken here... '}))
    reason_for_referral = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'reason for referral here... '}))
    referred_to_hospital = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))

    '''def set_hospital_choice(self, pk):
        self.fields['referred_to_hospital'].choices = [(hospital.id, hospital.name) for hospital in Hospital
            .objects.all().exclude(id=pk)]'''

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk', None)  # store value of request
        super(ReferralRequestForm, self).__init__(*args, **kwargs)
        print(self.pk)
        self.fields['referred_to_hospital'].choices = [(hospital.id, hospital.name) for hospital in Hospital
            .objects.all().exclude(id=self.pk)]

    def save_referral(self, context):
        referral = Referral.objects.create(
            referred_by_id=context['staff'].id,
            referring_hospital_id=context['hospital'].id,
            referred_to_hospital_id=self.cleaned_data.get('referred_to_hospital'),
            patient_id=context['patient'].id,
            health_problem_identified_in_detail=self.cleaned_data.get('health_problem_identified_in_detail'),
            action_taken=self.cleaned_data.get('action_taken'),
            reason_for_referral=self.cleaned_data.get('reason_for_referral'),
            referral_date=datetime.datetime.now(),
        )
        referral.save()


class XrayRequestForm(forms.Form):
    examination_requested = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    finding_and_diagnosis = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))

    '''def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk', None)  # store value of request
        super(XrayRequestForm, self).__init__(*args, **kwargs)
        print(self.pk)
        self.fields['requested_to'].choices = [(radiologist.id, radiologist.basic.username) for radiologist in
                                               Staff.objects.filter(hospital_id=self.pk, specialty='X-ray')]'''

    def save_xray_request(self, context):
        radiologist = Staff.objects.filter(hospital_id=context['hospital'].id, specialty='X-ray').\
            order_by('-num_waiting').last().id
        xray_request = XrayExamination.objects.create(
            hospital_id=context['hospital'].id,
            patient_id=context['patient'].id,
            requested_by_id=context['staff'].id,
            requested_to_id=radiologist,
            examination_requested=self.cleaned_data.get('examination_requested'),
            finding_and_diagnosis=self.cleaned_data.get('finding_and_diagnosis'),
        )
        xray_request.save()
        staff = Staff.objects.get(id=radiologist)
        staff.num_waiting = staff.num_waiting + 1
        staff.save()


class UltrasoundRequestForm(forms.Form):
    organ_to_be_examined = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    '''def set_requested_to_choice(self, pk):
        self.fields['requested_to'].choices = [(radiologist.id, radiologist.basic.username) for
                                               radiologist in
                                               Staff.objects.filter(hospital_id=Staff.objects.get(basic_id=pk).
                                                                    hospital_id, specialty='ultrasound')]'''

    def save_ultrasound_request(self, context):
        radiologist = Staff.objects.filter(hospital_id=context['hospital'].id, specialty='Ultrasound'). \
            order_by('-num_waiting').last().id
        ultrasound_request = UltraSound.objects.create(
            hospital_id=context['hospital'].id,
            patient_id=context['patient'].id,
            requested_by_id=context['staff'].id,
            requested_to_id=radiologist,
            organ_to_be_examined=self.cleaned_data.get('organ_to_be_examined'),
        )
        ultrasound_request.save()
        staff = Staff.objects.get(id=radiologist)
        staff.num_waiting = staff.num_waiting + 1
        staff.save()


class AdministeredTreatmentForm(forms.Form):
    medication_name = forms.CharField(required=True, max_length=150,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))

    def save_administered_treatment(self, context):
        administered_treatment = AdministeredTreatment.objects.create(
            hospital_id=context['hospital'].id,
            patient_id=context['patient'].id,
            given_by_id=context['staff'].id,
            medication_name=self.cleaned_data.get('medication_name'),
            description=self.cleaned_data.get('description'),
            medication_date=datetime.datetime.now(),
        )
        administered_treatment.save()


class PrescriptionForm(forms.Form):
    prescription_detail = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))

    def save_prescription(self, context):
        prescription = Prescription.objects.create(
            hospital_id=context['hospital'].id,
            patient_id=context['patient'].id,
            prescription_detail=self.cleaned_data.get('prescription_detail'),
            prescribed_by_id=context['staff'].id,
            date=datetime.datetime.now()
        )
        prescription.save()


'''
class UrineAnalysisRequestForm(forms.Form):
    albumine=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    blood = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    leukocyte = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    glucose = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    ph = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    nitrate = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    urbilonogen = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    ketone = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    bilirubin = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    specific_gravity = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    mleukocytes = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    merythrocytes = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    yeast = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    bacteria = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    squamous_epithelial_cells = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    hyaline_casts = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    granular_cast = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    wbc_cast = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    rbc_ast = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    uric_acid = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    calcium_oxalate = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))
    triplate_phosphate = forms.BooleanField(required=False, widget=forms.BooleanField(attrs={'class': 'form-control'}))

class StoolExaminationRequestForm(forms.Form):
    parasites=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    puss_cell=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    red_blood_cell=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    yeast_cell=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    obt=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    Hpylori_test=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    albumine=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))


class HematologyExaminationRequestForm(forms.Form):
    cbc=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    bc=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    twc=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    differntial=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    neutrophil=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    eosinophil=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    basophiles=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    monocyt=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    hemoglobin=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    mcv=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    mch=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    mchc=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    rbc=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    rbc_morphology=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    esr=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    bleeding_time_test=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    clot_reaction=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    coagulation_time=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    prothromin_time=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    p_t_t=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    fbs_rbs=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    blood_group=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    fibrinogen=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    coomos_test=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))
    cd4=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))'''
