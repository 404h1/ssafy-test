from django import forms
from .models import Todo, Comment


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        # Bug 08: 'image' 필드 누락 → 이미지 업로드 필드 미표시
        fields = ('title', 'content')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
