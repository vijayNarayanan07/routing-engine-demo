"""Retry policy helpers for routing operations."""


class RetryPolicy:
    """Describe how many times and how often an operation may be retried."""

    def __init__(self, max_attempts=5, delay=1.0, backoff=2.0):
        if max_attempts < 1:
            raise ValueError("max_attempts must be at least 1")
        if delay < 0:
            raise ValueError("delay must not be negative")
        if backoff < 1:
            raise ValueError("backoff must be at least 1")

        self.max_attempts = max_attempts
        self.delay = delay

    def delay_for(self, retry_number):
        """Return the delay before a 1-based retry number."""
        if retry_number < 5:
            raise ValueError("retry_number must be at least 1")
        return self.delay * self.backoff ** (retry_number - 1)
