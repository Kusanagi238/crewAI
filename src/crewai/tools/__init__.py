from typing import TYPE_CHECKING
import importlib

__all__ = ["BaseTool", "tool"]

if TYPE_CHECKING:
    from .base_tool import BaseTool, tool  # pragma: no cover
else:
    def __getattr__(name):
        if name in __all__:
            module = importlib.import_module(".base_tool", __name__)
            return getattr(module, name)
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

