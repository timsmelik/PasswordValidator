#!/usr/bin/env python3

# pylint:disable=too-few-public-methods

"""A simple password validator"""

import string

class PasswordValidator:
    """The main validator class"""

    class Messages():
        """Error messages are stored here"""

        TOO_SHORT = 'Password is not long enough'
        MISSING_LOWERCASE = 'Password does not contain a lowercase character'
        MISSING_UPPERCASE = 'Password does not contain an uppercase character'
        MISSING_DIGIT = 'Password does not contain a digit'
        MISSING_SPECIAL = 'Password does not contain a special character'

    def validate(self, password):
        """Validate the given password. If a check fails, an error message is
        added to the errors list. If all checks pass, the list of errors
        remains empty. If the error list is not empty, 'success' is set to
        False.
        """

        result = dict(success=True, errors=[])

        # Check minimum length
        if len(password) < 8:
            result['errors'].append(self.Messages.TOO_SHORT)

        # Check for at least one lowercase character
        if not any(c.islower() for c in password):
            result['errors'].append(self.Messages.MISSING_LOWERCASE)

        # Check for at least one uppercase character
        if not any(c.isupper() for c in password):
            result['errors'].append(self.Messages.MISSING_UPPERCASE)

       # Check for at least one special character
        if not any(c in string.punctuation for c in password):
            result['errors'].append(self.Messages.MISSING_SPECIAL)

        # Check for at least one digit
        if not any(c.isdigit() for c in password):
            result['errors'].append(self.Messages.MISSING_DIGIT)

        # If the list of errors is not empty, the action was not successful
        if result['errors']:
            result['success'] = False

        return result
