def sanitize_params_dict(params_dict, source_dict):
    """Sanitize params dict of a callable obtained through extraction.

    Args:
        params_dict: parameters dict of the callable
        source_dict: Your configuration options
    Returns:
        A sanitized dict which contains the parameters matching the params dict

    """
    sanitized_dict = {}
    params_dict.pop("args", None)
    params_dict.pop("kwargs", None)
    for key, val in params_dict.items():
        param_val = source_dict.get("fields", {}).get(key, None) or source_dict.get(key)
        if param_val:
            sanitized_dict[key] = param_val
    return sanitized_dict
