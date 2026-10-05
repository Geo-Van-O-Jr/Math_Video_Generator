from manim import VGroup, Text, Tex, MathTex, DOWN
from engine import theme
from .text_blocks import fit


class ProblemStatement(VGroup):
    """A readable statement chunk with distinct prose and LaTeX rows."""
    def __init__(self, prose, *math_lines, emphasis=False, latex_prose=False):
        color = theme.HIGHLIGHT if emphasis else theme.TEXT
        text = (Tex(prose, font_size=36, color=color, tex_template=theme.tex_template())
                if latex_prose else Text(prose, font=theme.FONT, font_size=31,
                                         color=color, line_spacing=0.9))
        rows = [text] + [MathTex(line, font_size=theme.MATH_SIZE,
                                tex_template=theme.tex_template()) for line in math_lines]
        super().__init__(*rows)
        self.arrange(DOWN, buff=0.55)
        fit(self, theme.BODY_WIDTH, theme.BODY_HEIGHT)
        self.move_to([0, 0.25, 0])
