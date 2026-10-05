from engine.base_scene import MathScene
from engine.components import ProblemStatement


class EpisodeScene(MathScene):
    def construct(self):
        self.heading("IMO Shortlist 2025 | Number Theory | N3", 1)
        self.present(ProblemStatement(
            r"An infinite sequence $a_1,a_2,\ldots$ consists of positive integers,\\"
            r"each of which has at least four positive divisors.",
            emphasis=True, latex_prose=True), hold=12)
        self.present(ProblemStatement(
            r"For each $n\ge1$, $a_{n+1}$ is the sum of the\\"
            r"three largest proper divisors of $a_n$.",
            emphasis=True, latex_prose=True), hold=12)
        self.present(ProblemStatement(
            r"A proper divisor of a positive integer $N$ is a divisor of $N$\\"
            r"other than $N$.", r"d\mid N,\qquad d<N", latex_prose=True),
                     "For example, the proper divisors of 6 are 1, 2, and 3.", hold=8)
        self.present(ProblemStatement(r"Determine all possible values of $a_1$.",
                                     emphasis=True, latex_prose=True),
                     "Pause here if you'd like to solve it yourself.", hold=10)
        self.replace_caption("Let's see what makes an integer survive.")
        self.read(4)
        self.finish()
