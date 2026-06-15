from __future__ import annotations

import os
from typing import Any

try:
    from langfuse import get_client, observe
except Exception:  # pragma: no cover
    def observe(*args: Any, **kwargs: Any):
        def decorator(func):
            return func
        return decorator

    class _DummyContext:
        def update_current_trace(self, **kwargs: Any) -> None:
            return None

        def update_current_observation(self, **kwargs: Any) -> None:
            return None

    def flush_traces() -> None:
        return None

    langfuse_context = _DummyContext()
else:
    class _LangfuseContext:
        def update_current_trace(self, **kwargs: Any) -> None:
            get_client().update_current_trace(**kwargs)

        def update_current_observation(self, **kwargs: Any) -> None:
            metadata = kwargs.get("metadata")
            usage_details = kwargs.get("usage_details")
            if usage_details:
                metadata = {**(metadata or {}), "usage_details": usage_details}
            get_client().update_current_span(metadata=metadata)

    def flush_traces() -> None:
        get_client().flush()

    langfuse_context = _LangfuseContext()


def tracing_enabled() -> bool:
    return bool(os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY"))
