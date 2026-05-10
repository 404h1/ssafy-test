from django import forms
from .models import Product


# form1 (일반 Form 예시)
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


# form2 (ModelForm 예시)
class ProductForm(forms.ModelForm):
    # 추후 Multiple Select 실습에서 해제
    CATEGORY_CHOICES = [
        ('ELEC', 'Electronics'),
        ('BOOK', 'Books'),
        ('FASH', 'Fashion'),
    ]
    category = forms.MultipleChoiceField(
        choices=CATEGORY_CHOICES,
        required=False,
        help_text='하나 이상의 카테고리를 선택하세요',
        widget=forms.CheckboxSelectMultiple,  # 체크박스 형태로 랜더링할 때 해제
    )

    class Meta:
        model = Product
        fields = ['name', 'price', 'category']


# form3
class BaseForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()


# form4
class ExtendedForm(BaseForm):
    address = forms.CharField(max_length=100)



# form5
class WidgetForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        )
    )
    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 10,
                'cols': 30,
                'class': 'form-control',
                # 'style': 'resize: none;', # 크기 조절 Off
            }
        ),
        required=False,
    )


class MyForm(forms.Form):
    FAVORITE_COLORS = [
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
    ]

    colors = forms.MultipleChoiceField(
        choices=FAVORITE_COLORS,
        widget=forms.CheckboxSelectMultiple,
    )
