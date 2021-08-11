from django.db import models

# Create your models here.
from accounts.models import User, Hospital, Staff


class Patient(models.Model):
    basic = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ManyToManyField(Hospital)

    def __str__(self):
        return User.username


class VitalSign(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    weight = models.SmallIntegerField()
    height = models.SmallIntegerField()
    bmi = models.SmallIntegerField()
    temperature = models.SmallIntegerField()
    systolic_BP = models.CharField(max_length=10)
    diastolic_BP = models.CharField(max_length=10)
    respiratory_rate = models.CharField(max_length=10)
    heart_rate = models.CharField(max_length=10)
    urine_output = models.CharField(max_length=10)
    blood_sugar_R = models.CharField(max_length=10)
    blood_sugar_F = models.CharField(max_length=10)
    taken_by = models.ForeignKey(Staff, on_delete=models.CASCADE)
    taken_date = models.DateTimeField()
    comment = models.TextField()


class PatientForm(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    note = models.TextField()
    filled_by = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    prescription_detail = models.TextField()
    prescribed_by = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class UltraSound(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    organ_to_be_examined = models.CharField(max_length=50)
    requested_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='ultrasound_requested_by')
    date_of_request = models.DateTimeField(auto_now_add=True)
    ultra_sound_image = models.ImageField(null=True)
    sonographic_report = models.TextField(null=True)
    reported_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='ultrasound_reported_by')
    date_of_report = models.DateTimeField(null=True)
    status = models.CharField(max_length=50, default='pending')


class XrayExamination(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    examination_requested = models.CharField(max_length=50)
    requested_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='xray_requested_by')
    date_of_request = models.DateTimeField(auto_now_add=True)
    x_ray_image = models.ImageField(null=True)
    x_ray_report = models.TextField(null=True)
    impressions = models.TextField(null=True)
    reported_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='xray_reported_by')
    date_of_report = models.DateTimeField(null=True)
    status = models.CharField(max_length=50, default='pending')


class Hematology(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    clinical_history = models.CharField(max_length=150, null=True)
    requested_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='hematology_requested_by')
    date_of_request = models.DateTimeField(null=True)
    status = models.CharField(max_length=50, default='pending')
    reported_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='hematology_reported_by', null=True)
    date_of_report = models.DateTimeField(null=True)
    lab_technician_comment = models.TextField(null=True)
    CBC = models.SmallIntegerField(null=True)
    BE = models.CharField(max_length=50, null=True)
    TWBC = models.CharField(max_length=50, null=True)
    differential = models.CharField(max_length=50, null=True)
    neutrophil = models.SmallIntegerField(null=True)
    lymphocyte = models.SmallIntegerField(null=True)
    eocynophil = models.SmallIntegerField(null=True)
    basophiles = models.SmallIntegerField(null=True)
    monocyt = models.SmallIntegerField(null=True)
    haemoglobin = models.SmallIntegerField(null=True)
    hemo_TCRIT = models.SmallIntegerField(null=True)
    MCV = models.SmallIntegerField(null=True)
    MCH = models.SmallIntegerField(null=True)
    MCHC = models.SmallIntegerField(null=True)
    RBC = models.SmallIntegerField(null=True)
    RBC_morophology = models.SmallIntegerField(null=True)
    platlet_count = models.SmallIntegerField(null=True)
    EST = models.SmallIntegerField(null=True)
    bleeding_time_test = models.CharField(max_length=50, null=True)
    clot_retraction = models.CharField(max_length=50, null=True)
    coagulation_time = models.CharField(max_length=50, null=True)
    prothrombin_time = models.CharField(max_length=50, null=True)
    PTT = models.CharField(max_length=50, null=True)
    FBS_RBS = models.CharField(max_length=50, null=True)
    blood_group = models.CharField(max_length=50, null=True)
    fibrinogen = models.CharField(max_length=50, null=True)
    coombs_test = models.CharField(max_length=50, null=True)
    CD4 = models.SmallIntegerField(null=True)


class StoolExamination(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='stool_requested_by')
    date_of_request = models.DateTimeField()
    status = models.CharField(max_length=50, default='pending')
    parasites = models.CharField(max_length=50, null=True)
    pus_cell = models.CharField(max_length=50, null=True)
    red_blood_cell = models.CharField(max_length=50, null=True)
    yeast_cell = models.CharField(max_length=50, null=True)
    occult_blood_test = models.CharField(max_length=50, null=True)
    h_pylory_stool_ag_test = models.CharField(max_length=50, null=True)
    reported_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='stool_reported_by', null=True)
    date_of_report = models.DateTimeField(null=True)


class UrineAnalysis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='urine_requested_by')
    date_of_request = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='pending')
    reported_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='urine_reported_by', null=True)
    date_of_report = models.DateTimeField(null=True)
    albumine = models.SmallIntegerField(null=True)
    blood = models.SmallIntegerField(null=True)
    chemo_leukocyte = models.SmallIntegerField(null=True)
    glucose = models.SmallIntegerField(null=True)
    PH = models.SmallIntegerField(null=True)
    nitrate = models.SmallIntegerField(null=True)
    parasites = models.SmallIntegerField(null=True)
    pus_cell = models.SmallIntegerField(null=True)
    red_blood_cell = models.SmallIntegerField(null=True)
    urobilonogen = models.SmallIntegerField(null=True)
    ketone = models.SmallIntegerField(null=True)
    bilirubin = models.SmallIntegerField(null=True)
    specific_gravity = models.SmallIntegerField(null=True)
    microscopy_leukocyte = models.SmallIntegerField(null=True)
    erythrocyte = models.SmallIntegerField(null=True)
    yeast = models.SmallIntegerField(null=True)
    bacteria = models.SmallIntegerField(null=True)
    squamous_epithelial_cell = models.SmallIntegerField(null=True)
    hyaline_cast = models.SmallIntegerField(null=True)
    granular_cas = models.SmallIntegerField(null=True)
    WBC_casts = models.SmallIntegerField(null=True)
    RBC_cast = models.SmallIntegerField(null=True)
    uric_acid = models.SmallIntegerField(null=True)
    calcium_oxalate = models.SmallIntegerField(null=True)
    triple_phosphate = models.SmallIntegerField(null=True)
