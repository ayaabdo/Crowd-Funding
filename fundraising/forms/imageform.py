from django import forms
from fundraising.models.images import Image
from .projectform import ProjectForm

class ImageForm(forms.ModelForm):
        image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        class Meta:
            model = Image
            fields = ProjectForm.Meta.fields + ('image_path', )
