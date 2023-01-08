from django import forms

from .models import User


class BaseForm(forms.ModelForm):
    """abstract form"""

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs.update(
                {
                    "autofocus": "true",
                    "placeholder": field.label,
                    "autocomplete": "off",
                    "class": "focus:outline focus:outline-2 focus:outline-blue-500 focus:caret-blue-500 placeholder-gray-400 px-3 py-1 bg-gray-600 rounded-lg",
                }
            )
        super().__init__(*args, **kwargs)


class LoginForm(BaseForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    def __init__(self):
        super().__init__()
        self.fields["password"].widget.input_type = "password"


class RegisterForm(BaseForm):
    confirmation = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def __init__(self):
        super().__init__()
        self.fields["password"].widget.input_type = "password"
