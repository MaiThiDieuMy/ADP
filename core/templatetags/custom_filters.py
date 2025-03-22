from django import template
import logging

register = template.Library()
logger = logging.getLogger(__name__)

@register.filter
def get_item(dictionary, key):
    """
    Gets an item from a dictionary using the key.
    Returns None if dictionary is None or key doesn't exist.
    """
    if dictionary is None:
        return None
    
    try:
        # Safely get the item from dictionary
        result = dictionary.get(key)
        return result
    except Exception as e:
        # Log the error and return None
        logger.error(f"Error in get_item filter: {e}, dictionary: {type(dictionary)}, key: {key}")
        return None

@register.filter
def default_if_none(value, default=""):
    """
    Returns the default value if the provided value is None
    """
    if value is None:
        return default
    return value 