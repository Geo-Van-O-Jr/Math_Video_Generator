from engine.base_scene import MathScene
from engine.components import CaseSplit
from engine import theme


class EpisodeScene(MathScene):
    def construct(self):
        self.heading("Only three possibilities remain", 6)
        self.equation(r"6\mid a_n\quad\Rightarrow\quad p_1=2,\ p_2=3",
                      r"p_3\in\{4,5,6\}",
                      caption="The third divisor exceeds 3, and 6 itself is already a divisor.", hold=8)
        branches = CaseSplit(r"\frac{a_{n+1}}{a_n}", [
            (r"\frac12+\frac13+\frac14=\frac{13}{12}", "CASE 4: GROWTH", theme.HIGHLIGHT),
            (r"\frac12+\frac13+\frac15=\frac{31}{30}", "CASE 5: GROWTH?", theme.WARNING),
            (r"\frac12+\frac13+\frac16=1", "CASE 6: FIXED POINT", theme.SUCCESS)])
        self.present(branches, "Two cases appear to grow. The third freezes immediately.", hold=10)
        self.equation(r"p_3=4:\quad a_{n+1}=\frac{13}{12}a_n",
                      r"p_3=5:\quad a_{n+1}=\frac{31}{30}a_n",
                      r"p_3=6:\quad a_{n+1}=a_n",
                      caption="We must check which apparent growth steps can actually survive.", hold=10)
        self.finish()
