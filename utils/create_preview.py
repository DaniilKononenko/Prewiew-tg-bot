from linkpreview import link_preview
from requests import ConnectionError

def create_preview(url: str) -> str:
    try:
        prewiew = link_preview(url)
    except ConnectionError:
        raise

    return prewiew.image
    