from manim import Create, FadeOut
from engine.base_scene import MathScene
from engine.components import ContradictionMark
from engine import theme


class EpisodeScene(MathScene):
    def construct(self):
        self.heading("An odd term cannot survive", 4)
        self.equation(r"a_n\text{ odd}\quad\Rightarrow\quad p_1\ge3,\ p_2\ge5,\ p_3\ge7",
                      caption="Distinct odd divisors greater than 1 start no earlier than 3, 5, 7.", hold=7)
        self.equation(r"\frac{a_{n+1}}{a_n}\le\frac13+\frac15+\frac17=\frac{71}{105}<1",
                      caption="Every odd term strictly shrinks.", hold=7)
        self.equation(r"\text{odd}+\text{odd}+\text{odd}=\text{odd}",
                      caption="All divisors of an odd integer are odd. The next term stays odd.", hold=7)
        self.equation(r"a_n>a_{n+1}>a_{n+2}>\cdots>0",
                      caption="So an odd term would force an infinite descent in positive integers.", hold=7)
        mark = ContradictionMark(self.body)
        self.play(Create(mark))
        self.replace_caption("An infinite strictly decreasing sequence of positive integers is impossible.")
        self.read(6)
        self.play(FadeOut(mark))
        self.result(r"2\mid a_n\qquad\text{for every }n",
                    caption="Every term in a surviving sequence is even.", hold=7)
        self.finish()
