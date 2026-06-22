"""In-process task queue for async work (MVP only)."""

# TODO: Replace with ARQ / Celery for production.
# For MVP, detection jobs run synchronously in the request thread.
