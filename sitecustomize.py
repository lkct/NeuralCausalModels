# Completely disable tqdm everywhere, no matter how it's imported.
try:
    import tqdm
except ImportError:

    class tqdm:
        tqdm = object


class _noop_tqdm(tqdm.tqdm):
    """A tqdm subclass that suppresses all output but keeps full API compatibility."""

    def display(self, *a, **k):
        pass

    def refresh(self, *a, **k):
        pass

    def clear(self, *a, **k):
        pass

    @classmethod
    def write(cls, *a, **k):
        pass

    def _print(self, *a, **k):
        pass

    # Optional: disable printing on close
    def close(self):
        pass


# Patch the main tqdm function
tqdm.tqdm = _noop_tqdm

# Patch submodules that re-export tqdm
try:
    import tqdm.auto

    tqdm.auto.tqdm = _noop_tqdm
except Exception:
    pass

try:
    import tqdm.std

    tqdm.std.tqdm = _noop_tqdm
except Exception:
    pass

try:
    import tqdm.asyncio

    tqdm.asyncio.tqdm = _noop_tqdm
except Exception:
    pass

try:
    import tqdm.notebook

    tqdm.notebook.tqdm = _noop_tqdm
except Exception:
    pass
