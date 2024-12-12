# nfc/admin.py (Optional: central registration file)
from django.contrib import admin
# from nfc.texts.models import TextModel  # Replace with the actual model
# from nfc.tag_id.models import TagIDModel  # Replace with the actual model
from nfc.students.models import Student  # Replace with the actual model
from nfc.bus.models import Bus  # Replace with the actual model

# admin.site.register(TextModel)
# admin.site.register(TagIDModel)
admin.site.register(Student)
admin.site.register(Bus)
