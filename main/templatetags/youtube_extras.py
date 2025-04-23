from django import template
import re

register = template.Library()

@register.filter
def youtube_embed(url):
    """
    Converts a regular YouTube URL to an embeddable format.
    Example:
    https://www.youtube.com/watch?v=ABC123 ➜ https://www.youtube.com/embed/ABC123
    """
    if "youtube.com/watch?v=" in url:
        return url.replace("watch?v=", "embed/")
    elif "youtu.be/" in url:
        video_id = url.split("youtu.be/")[-1]
        return f"https://www.youtube.com/embed/{video_id}"
    return url  # fallback, return as is
