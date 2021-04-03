from fundraising.models.comments import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('project_ID', 'comment')