from django.contrib import admin
from .models.project import Project
from .models.rate import Rate
from .models.comments import Comment
from .models.images import Image
from .models.report_project import ReportAProject
from .models.report_comment import ReportAComment
from .models.user_donation import Donation

# Register your models here.


admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Rate)
admin.site.register(Image)
admin.site.register(ReportAProject)
admin.site.register(ReportAComment)
admin.site.register(Donation)

#admin.site.register(User)