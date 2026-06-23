from typing import Any, Dict, Type

from pydantic import BaseModel


def process_config(
    values: Dict[str, Any], model_class: Type[BaseModel]
) -> Dict[str, Any]:
    """
    Process the config dictionary and update the values accordingly.

    Args:
        values (Dict[str, Any]): The dictionary of values to update.
        model_class (Type[BaseModel]): The Pydantic model class to reference for field validation.

    Returns:
        Dict[str, Any]: The updated values dictionary.
    """
    # Ensure values is a mapping/dictionary to avoid AttributeError when accessing .get
    if not isinstance(values, dict):
        raise TypeError(f"process_config expected 'values' to be a dict, got {type(values).__name__}")

    config = values.get("config", {})
    if not config:
        return values

    # Copy values from config (originally from YAML) to the model's attributes.
    # Only copy if the attribute isn't already set, preserving any explicitly defined values.
    for key, value in config.items():
        if key not in model_class.model_fields or values.get(key) is not None:
            continue

        if isinstance(value, dict):
            if isinstance(values.get(key), dict):
                values[key].update(value)
            else:
                values[key] = value
        else:
            values[key] = value

    # Remove the config from values to avoid duplicate processing
    values.pop("config", None)
    return values
