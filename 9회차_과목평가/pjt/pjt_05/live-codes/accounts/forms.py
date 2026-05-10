from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm, PasswordChangeForm


class CustomUserCreationForm(UserCreationForm):
    # 1. 필드 자체를 재정의하는 방식 (재정의하기 때문에 기존 설정(help_text, required, ...) 값이 사라짐)
    #   (일반 Form 정의할 때 주로 사용 - Meta 클래스가 없기 때문)
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '사용자 이름',
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호 확인',
            }
        )
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # 2. widgets 설정을 통해 정의하는 방식 (기존 내용(help_text, required, ..) 유지되므로 권장)
        #  (ModelForm일 때 사용 가능 - Meta 클래스를 사용할 수 있기 때문)
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '이메일',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '이름',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '성',
                }
            ),
        }

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '사용자 이름',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
            }
        )
    )


# class CustomPasswordChangeForm(PasswordChangeForm):
#     old_password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': '현재 비밀번호',
#             }
#         )
#     )
#     new_password1 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': '새 비밀번호',
#             }
#         )
#     )
#     new_password2 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': '새 비밀번호 확인',
#             }
#         )
#     )