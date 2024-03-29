from django import forms

from .models import User, Submission, Quiz


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
                    "class": "focus:outline focus:outline-2 \
                        focus:outline-blue-500 focus:caret-blue-500 \
                        placeholder-gray-400 px-3 py-1 bg-gray-600 rounded-lg w-full",
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

    def form_type(self):
        """display the meta description of form"""
        return "login"


class RegisterForm(BaseForm):
    confirmation = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def __init__(self):
        super().__init__()
        self.fields["password"].widget.input_type = "password"

    def form_type(self):
        """display the meta description of form"""
        return "register"


class SubmissionForm(BaseForm):
    class Meta:
        model = Submission
        fields = ["submitted_answer"]

    def __init__(self):
        super().__init__()
        self.fields["submitted_answer"].widget.attrs["placeholder"] = "your answer"


class AddQuizForm(BaseForm):
    class Meta:
        model = Quiz
        fields = ["title", "content", "correct_answer"]

    def __init__(self):
        super().__init__()
