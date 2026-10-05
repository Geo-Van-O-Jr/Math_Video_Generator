from manim import VGroup, MathTex, Text, Arrow, DOWN, UP, Line
from engine import theme
from .text_blocks import fit


class CaseSplit(VGroup):
    def __init__(self, root, cases):
        super().__init__()
        self.root = MathTex(root, font_size=theme.MATH_SIZE,
                            tex_template=theme.tex_template()).move_to([0, 1.8, 0])
        self.branches = VGroup()
        self.arrows = VGroup()
        for x, (formula, label, color) in zip((-4.3, 0, 4.3), cases):
            eq = MathTex(formula, font_size=33, color=color,
                         tex_template=theme.tex_template())
            caption = Text(label, font=theme.FONT, font_size=20, color=color)
            branch = VGroup(eq, caption).arrange(DOWN, buff=0.5)
            fit(branch, 3.85, 2.2)
            branch.move_to([x, -0.35, 0])
            self.branches.add(branch)
            self.arrows.add(Arrow(self.root.get_bottom(), branch.get_top(),
                                 buff=0.2, color=theme.MUTED_TEXT))
        self.add(self.root, self.arrows, self.branches)


class ContradictionMark(VGroup):
    def __init__(self, target):
        super().__init__(
            Line(target.get_corner(UP + [-1, 0, 0]),
                 target.get_corner(DOWN + [1, 0, 0]), color=theme.CONTRADICTION),
            Line(target.get_corner(UP + [1, 0, 0]),
                 target.get_corner(DOWN + [-1, 0, 0]), color=theme.CONTRADICTION))
