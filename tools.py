from datetime import datetime


def get_current_time() -> str:
    """Returns the current local date and time. Use this whenever the user
    asks what time or day it is, or anything relative to 'now'."""
    return datetime.now().strftime("%A, %B %d, %Y at %I:%M %p")


def get_project_status(project_name: str) -> str:
    """Returns known status/details for one of Lyx's projects.

    Args:
        project_name: The project to look up. One of:
            "portfolio", "floopychicken", "the fading star", "library manager".
    """
    projects = {
        "portfolio": "Personal portfolio site at lyx.dev, repo: github.com/Lyxian0906/PortFolio.",
        "floopychicken": "A Flappy Bird-style 2D game built in Unity/C#.",
        "the fading star": "An early-stage prototype game concept.",
        "library manager": "A book recommendation website.",
    }
    key = project_name.strip().lower()
    return projects.get(
        key,
        f"No status recorded yet for '{project_name}'. Ask Lyx to fill you in!"
    )


# Add new tools here as plain functions with type hints + a docstring —
# the SDK reads both to know when and how to call them. Then add the
# function to the `tools` list in app.py's GenerateContentConfig.