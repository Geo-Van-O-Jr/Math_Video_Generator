from manim import VGroup, MathTex, Arrow, Write, LaggedStart
from engine.base_scene import MathScene
from engine.components import EquationStep
from engine import theme


class EpisodeScene(MathScene):
    def construct(self):
        self.heading("Large divisors, small partners", 3)
        self.equation(r"1<p_1<p_2<p_3",
                      caption="Let these be the three smallest divisors greater than 1.", hold=6)
        pairs = VGroup()
        arrows = VGroup()
        for y, p in zip((1.5, 0.25, -1), (1, 2, 3)):
            left = MathTex(fr"p_{p}", color=theme.HIGHLIGHT).move_to([-3, y, 0])
            right = MathTex(fr"\frac{{a_n}}{{p_{p}}}").move_to([3, y, 0])
            arrow = Arrow(left.get_right(), right.get_left(), buff=0.3, color=theme.MUTED_TEXT)
            pairs.add(VGroup(left, arrow, right))
        self.present(pairs, "Smaller divisors have larger complementary divisors.", hold=7)
        self.equation(r"\frac{a_n}{p_1}>\frac{a_n}{p_2}>\frac{a_n}{p_3}",
                      caption="These are precisely the three largest proper divisors.", hold=6)
        self.equation(r"a_{n+1}=\frac{a_n}{p_1}+\frac{a_n}{p_2}+\frac{a_n}{p_3}",
                      caption="Rewrite the recurrence using the small partners.", hold=6)
        self.equation(r"\frac{a_{n+1}}{a_n}=\frac1{p_1}+\frac1{p_2}+\frac1{p_3}",
                      caption="Now everything depends on three reciprocals.", hold=7)
        self.equation(r"\frac{a_{n+1}}{a_n}<1\ \Rightarrow\ \text{shrinks}",
                      r"\frac{a_{n+1}}{a_n}=1\ \Rightarrow\ \text{freezes}",
                      r"\frac{a_{n+1}}{a_n}>1\ \Rightarrow\ \text{grows}",
                      caption="The threshold is 1.", hold=8)
        self.finish()
