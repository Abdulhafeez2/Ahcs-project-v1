from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Hematology)
admin.site.register(XrayExamination)
admin.site.register(UltraSound)
admin.site.register(PatientForm)
admin.site.register(Patient)
admin.site.register(UrineAnalysis)
admin.site.register(VitalSign)
admin.site.register(Medication)