from playwright.sync_api import Page

_page: Page | None = None


def set_page(page: Page) -> None:
    """Store the shared Playwright Page instance."""
    global _page
    _page = page


def get_page() -> Page:
    """Return the stored Page instance.

    Raises:
        RuntimeError: if no Page has been set yet.
    """
    if _page is None:
        raise RuntimeError("No Page has been set. Call set_page(page) before using flows.")
    return _page


def clear_page() -> None:
    """Clear the stored Page instance."""
    global _page
    _page = None
