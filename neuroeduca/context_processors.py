from .forms import CustomLoginForm, CustomSignupForm

def auth_forms(request):
    return {
        'login_form': CustomLoginForm(),
        'signup_form': CustomSignupForm(),
    }