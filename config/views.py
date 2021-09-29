import os

from section.models import Audio
from .models import Config


def delete_file(files: list):
    Audio.delete_old()
    for file in files:
        try:
            os.remove(file)
        except FileNotFoundError:
            pass


def get_upload_to(instance, filename) -> str:
    """
      Returns the path to the media
    """
    try:
        return f'{instance.IMAGE_PATH}/{instance.id}/{filename}'
    except Exception:
        # TODO: Exception?
        return f'upload/{instance.id}/{filename}'


def common_context() -> dict:
    """
      Returns the context that is present on all pages
    """
    context = dict()
    context['cfg'] = Config.get_cfg()
    return context
