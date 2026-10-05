from manim import Create, FadeOut
from engine.base_scene import MathScene
from engine.components import CaseSplit, ContradictionMark
from engine import theme


class EpisodeScene(MathScene):
    def construct(self):
        self.heading("Case 5 is a trap", 7)
        self.equation(r"p_3=5\quad\Rightarrow\quad6\mid a_n,\ 5\mid a_n,\ 4\nmid a_n",
                      r"a_n=30k,\qquad k\text{ odd}",
                      caption="There is exactly one factor 2 in the current term.", hold=8)
        self.equation(r"a_{n+1}=\frac{31}{30}(30k)=31k",
                      r"31k\text{ is odd}",
                      caption="The next term is odd, so this branch cannot survive.", hold=8)
        branches = CaseSplit(r"p_3\in\{4,5,6\}", [
            (r"p_3=4", "GROWTH", theme.HIGHLIGHT),
            (r"p_3=5", "IMPOSSIBLE", theme.CONTRADICTION),
            (r"p_3=6", "FIXED POINT", theme.SUCCESS)])
        self.present(branches, "Eliminate case 5. Only case 4 growth and case 6 fixed points remain.", hold=5)
        mark = ContradictionMark(branches.branches[1])
        self.play(Create(mark))
        self.read(6)
        self.finish()
