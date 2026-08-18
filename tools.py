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
        "portfolio": "Personal portfolio site called lyx.dev, repo: github.com/Lyxian0906/PortFolio.",
        "floopychicken": "A Flappy Bird-style 2D game built in Unity/C#.",
        "the fading star": "An early-stage prototype game concept.",
        "library manager": "A book recommendation website.",
        "lyx AI": "Personal assistant boosted by Gemini API, keeps evolving and learning new things to make the user experience better ",
    }
    key = project_name.strip().lower()
    return projects.get(
        key,
        f"No status recorded yet for '{project_name}'. Ask Lyx to fill you in!"
    )

def get_lyx_info(info_type: str) -> str:
    """Returns known personal information about Lyx.

    Args:
        info_type: The type of information to look up. One of:
            "about", "studies", "skills", "languages", "interests", "goals".
    """
    lyx_info = {
        "about": (
            "Lyx is a 20 years developer from Asturias, Spain, who enjoys programming, "
            "game development, web development, and learning new technologies. She loves colorful things"
        ),

        "studies": (
            "Lyx is studying a Higher Vocational Training program in "
            "Multiplatform Application Development (DAM). Also doing AI courses"
        ),

        "skills": (
            "Lyx has experience with Java, Python, C#, HTML, CSS, JavaScript, "
            "SQL, Unity, Git, GitHub, Firebase, and AWS."
        ),

        "languages": (
            "Lyx speaks Spanish and English and is also learning Korean and Japanese."
        ),

        "interests": (
            "Lyx enjoys programming, videogames, game development, web "
            "development, Harry Potter, Drawing, Zelda, and learning languages. And she is a big fan of dicovering new lands, she loves lo travel"
        ),

        "goals": (
            "Lyx wants to improve as a developer, build interesting portfolio "
            "projects, gain practical experience, and continue learning "
            "software development and AI."
        ),
    }

    key = info_type.strip().lower()

#When tha AI donesn't have this info this message will pop 

    return lyx_info.get(
        key,
        f"No personal information is recorded for '{info_type}'."
    )

# Add new tools here as plain functions with type hints + a docstring —
# the SDK reads both to know when and how to call them. Then add the
# function to the `tools` list in app.py's GenerateContentConfig.