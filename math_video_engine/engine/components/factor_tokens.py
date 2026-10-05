from manim import VGroup, Circle, MathTex, RIGHT
from engine import theme


class PrimeFactorTokens(VGroup):
    def __init__(self, factors):
        super().__init__()
        for prime in factors:
            color = theme.HIGHLIGHT if prime in (2, 3) else theme.SUCCESS
            circle = Circle(radius=0.43, color=color,
                            fill_color=color, fill_opacity=0.08)
            value = MathTex(str(prime), font_size=36, color=color,
                            tex_template=theme.tex_template())
            self.add(VGroup(circle, value))
        self.arrange(RIGHT, buff=0.22)
