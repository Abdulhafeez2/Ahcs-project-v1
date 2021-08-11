from django import forms

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
    cd4=forms.BooleanField(required=False,widget=forms.BooleanField(attrs={'class': 'form-control'}))








