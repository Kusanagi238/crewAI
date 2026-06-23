import warnings
from typing import TYPE_CHECKING

# Avoid importing submodules at package import time to prevent import-time errors
# (e.g. NameError in nested modules). Only import for type checking to preserve
# type hints without triggering runtime imports.
if TYPE_CHECKING:
    from crewai.agent import Agent
    from crewai.crew import Crew
    from crewai.crews.crew_output import CrewOutput
    from crewai.flow.flow import Flow
    from crewai.knowledge.knowledge import Knowledge
    from crewai.llm import LLM
    from crewai.llms.base_llm import BaseLLM
    from crewai.process import Process
    from crewai.task import Task
    from crewai.tasks.llm_guardrail import LLMGuardrail
    from crewai.tasks.task_output import TaskOutput

warnings.filterwarnings(
    "ignore",
    message="Pydantic serializer warnings:",
    category=UserWarning,
    module="pydantic.main",
)
__version__ = "0.121.0"
__all__ = [
    "Agent",
    "Crew",
    "CrewOutput",
    "Process",
    "Task",
    "LLM",
    "BaseLLM",
    "Flow",
    "Knowledge",
    "TaskOutput",
    "LLMGuardrail",
]
