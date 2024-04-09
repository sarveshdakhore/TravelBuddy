from allauth.socialaccount.models import SocialLogin
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

@receiver(user_signed_up)
def save_email(sender, sociallogin, **kwargs):
    user = sociallogin.user
    user.email = sociallogin.account.extra_data.get('email')
    user.save()