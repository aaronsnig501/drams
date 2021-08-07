from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):

    def create_superuser(self, email, username, password, **kwargs):
        """Create superuser

        Creates a new superuser. Will default `is_staff`, `is_superuser` and
        `is_active`

        Args:
            email (str): The email of the new user
            username (str): The username of the new user
            password (str): The password of the new user

        Optional Args:
            is_staff (bool): Flag to indicate if the unew user is staff
            is_superuser (bool): Flag to indicate if the new user is a superuser
            is_active (bool): Flag to indicate if the new user has an active account

        Returns:
            Account: Newly created account instance

        Raises:
            ValueError: Will raise `ValueError` if either `is_staff` or `ìs_superuser`
                are missing
        """
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")

        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must be assign to is_superuser=True")

        return self.create_user(email, username, password, **kwargs)

    def create_user(self, email, username, password, **kwargs):
        """Create user

        Creates a new user

        Args:
            email (str): The email of the new user
            username (str): The username of the new user
            password (str): The password of the new user

        Returns:
            Account: Newly created account instance

        Raises:
            ValueError: Will raise `ValueError` if either `email`, `username` or
                `password` are missing
        """
        if not email:
            raise ValueError(_("You must provide an email address"))

        if not username:
            raise ValueError(_("You must provide an username"))

        if not password:
            raise ValueError(_("You must provide a password"))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user