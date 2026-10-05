from manim import VGroup, MathTex, Arrow, ReplacementTransform
from engine.base_scene import MathScene
from engine.components import PrimeFactorTokens
from engine import theme


class EpisodeScene(MathScene):
    def construct(self):
        self.heading("Growth spends a finite resource", 8)
        self.equation(r"a_{n+1}=\frac{13}{12}a_n", r"12=2^2\cdot3",
                      caption="Every nonconstant step removes two factors 2 and one factor 3.", hold=8)
        tokens = PrimeFactorTokens([2, 2, 3]).move_to([0, 0.4, 0])
        self.present(tokens, "Replace these factors with a single factor 13.", hold=5)
        replacement = PrimeFactorTokens([13]).move_to(tokens)
        self.play(ReplacementTransform(tokens, replacement), run_time=2)
        self.body = replacement
        self.read(5)
        self.equation(r"v_2(a_{n+1})=v_2(a_n)-2",
                      caption="The number of factors 2 drops by exactly two at every growth step.", hold=8)
        self.equation(r"v_2(a_1),\ v_2(a_1)-2,\ v_2(a_1)-4,\ldots",
                      caption="A nonnegative integer cannot keep decreasing this way forever.", hold=7)
        self.equation(r"\frac{13}{12}\longrightarrow\frac{13}{12}\longrightarrow\cdots\longrightarrow1\longrightarrow1\longrightarrow\cdots",
                      caption="A surviving sequence must eventually reach case 6.", hold=7)
        self.result(r"a_n=A\quad\text{for all sufficiently large }n",
                    caption="Every surviving sequence eventually freezes.", hold=7)
        self.finish()
