def lookupattr(obj, name, default=None):
    """Recursively lookup an attribute or key on an object."""
    name = name.replace("__", ".")
    for element in name.split('.'):
        try:
            attr = getattr(obj, element)
        except AttributeError:
            try:
                attr = obj.__dict__[element]
            except (KeyError, AttributeError):
                try:
                    attr = obj[element]
                except (KeyError, TypeError):
                    attr = default
                    break
        except Exception:
            attr = default
            break
        if callable(attr):
            obj = attr()
        else:
            obj = attr
    if callable(attr):
        return attr()
    else:
        return attr
