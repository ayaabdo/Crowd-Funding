from django import forms
from fundraising.models.project import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'details', 'cat_id', 'tags',
                     'total_target', 'total_donation', 'created_at',
                    'start_date', 'end_date' )
