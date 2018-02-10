from django.contrib import admin
from first_project_app.models import Topic, Webpage, AccessRecord, User


admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(User)
