from manim import MathTex, VGroup, DOWN
from engine import theme
from .text_blocks import fit


class EquationStep(VGroup):
    def __init__(self, *lines, color=theme.PRIMARY_MATH):
        super().__init__(*[MathTex(line, font_size=theme.MATH_SIZE,
                                  color=color, tex_template=theme.tex_template())
                           for line in lines])
        self.arrange(DOWN, buff=0.45)
        fit(self, theme.BODY_WIDTH, theme.BODY_HEIGHT)
        self.move_to([0, 0.25, 0])
