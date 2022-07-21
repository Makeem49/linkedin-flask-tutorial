from functools import wraps
from flask import abort


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            try:
                payload = verify_decode_jwt(token)  # True
            except:
                abort(401)

            if not payload:
                abort(401)  # with this line of code, expired or invalid
                # token will not be able to access the view function

            is_permitted = check_permissions('delete user', payload)  # false

            if not is_permitted:
                # if the user is not permitted to access the view function
                abort(401)
                # it will abort the request as well.

            # The user will only be able to access the
            return f(payload, *args, **kwargs)
            # view function if he/she has permission to access
            # the page.
        return wrapper
    return requires_auth_decorator
