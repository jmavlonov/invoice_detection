import numpy as np

def json_converter(obj):
    """Numpy tiplari uchun converter"""
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        return float(obj)
    if isinstance(obj, (np.bool_, bool)):
        return bool(obj)
    return str(obj)
