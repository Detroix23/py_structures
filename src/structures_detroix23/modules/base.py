"""
# Data structures.
/src/structures_detroix23/modules/base.py.
Base.
"""

def copy(instance):
    """
    Call the `__copy__` method on a given instance and return the copy.
    """
    return instance.__copy__()