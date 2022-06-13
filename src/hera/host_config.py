host = None
token = None


def token_callback():
    return None


def set_global_host(h):
    """Sets the Argo Workflows host at a global level so services can use it"""
    global host
    host = h


def get_global_host():
    """Returns the Argo Workflows global host"""
    return host


def set_global_token(t):
    """Sets the Argo Workflows token at a global level so services can use it"""
    global token
    token = t


def set_global_token_callback(fn):
    """Sets the Argo Workflows token callback at a global level so services can use it"""
    global token_callback
    token_callback = fn


def get_global_token():
    """Returns an Argo Workflows global token

    If both `token` and `token_callback` are set, `token` will be preferred.
    """
    if token is not None:
        return token
    return token_callback()
