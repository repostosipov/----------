from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = "__all__"
        fields = ["title", "content", "is_published", "category"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "category": forms.RadioSelect(
                attrs={
                    "class": "form-check form-check-inline d-flex justify-content-between"
                }
            ),
        }

    # title = forms.CharField(
    #     max_length=150,
    #     label="Название статьи:",
    #     widget=forms.TextInput(attrs={"class": "form-control"}),
    # )
    # content = forms.CharField(
    #     label="Текст статьи:",
    #     required=False,
    #     widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}),
    # )
    # is_published = forms.BooleanField(label="Опубликовать?", initial=True)
    # category = forms.ModelChoiceField(
    #     empty_label="Выберите категорю",
    #     label="Категория",
    #     queryset=Category.objects.all(),
    #     widget=forms.RadioSelect(
    #         attrs={
    #             "class": "form-check form-check-inline d-flex justify-content-between"
    #         }
    #     ),
    # )
