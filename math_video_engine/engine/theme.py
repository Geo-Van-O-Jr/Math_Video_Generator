from manim import TexTemplate

BACKGROUND = "#10151F"
TEXT = "#E9EDF4"
MUTED_TEXT = "#A5B1C4"
HIGHLIGHT = "#EBC17A"
SUCCESS = "#8AD4B0"
WARNING = HIGHLIGHT
CONTRADICTION = "#EC929A"
PRIMARY_MATH = TEXT
FONT = "Segoe UI"
TITLE_SIZE = 30
CAPTION_SIZE = 25
MATH_SIZE = 46
BODY_WIDTH = 12.0
BODY_HEIGHT = 4.35
CAPTION_WIDTH = 11.8
TRANSITION_TIME = 1.0


def tex_template():
    template = TexTemplate()
    template.add_to_preamble(r"\usepackage{amsmath,amssymb}")
    return template
