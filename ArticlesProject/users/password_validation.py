from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class SymbolicPasswordValidator:
    """Validate whether the password is alphanumeric."""

    def validate(self, password, user=None):
        if password.isalpha():
            raise ValidationError(
                _("This password is entirely symbolic."),
                code="password_entirely_symbolic",
            )

    def get_help_text(self):
        return _("Your password can’t be entirely symbolic.")
