from django import forms
from core.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image']
        # labels = {
        #     'title': 'Título',
        #     'text': 'Texto',
        #     'image': 'Imagem',
        # }

    def save(self, commit=True):
            self.instance.author = self.initial['author']
            self.instance.save()
            return super().save()
