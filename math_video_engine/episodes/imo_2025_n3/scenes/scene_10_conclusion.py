from engine.base_scene import MathScene


class EpisodeScene(MathScene):
    def construct(self):
        self.heading("Two growth steps, then forever", 10)
        self.equation(r"864=6\cdot12^2", r"c=2,\qquad m=1",
                      caption="Our opening example belongs to the surviving family.", hold=6)
        self.equation(r"6\cdot12^2\longrightarrow6\cdot12\cdot13\longrightarrow6\cdot13^2",
                      r"864\longrightarrow936\longrightarrow1014",
                      caption="Each step trades a factor 12 for a factor 13.", hold=8)
        self.equation(r"1014=2\cdot3\cdot13^2", r"1014\longrightarrow1014\longrightarrow1014\longrightarrow\cdots",
                      caption="Only one factor 2 remains. The growth case is unavailable; case 6 freezes.", hold=8)
        self.result(r"\boxed{a_1=6\cdot12^c m=2^{2c+1}3^{c+1}m}",
                    r"c\in\mathbb Z_{\ge0},\quad m\in\mathbb Z_{>0},\quad\gcd(m,10)=1",
                    caption="Exactly these starting values survive forever.", hold=9)
        self.replace_caption("The sequence survives exactly when it has enough factors of 2 and 3\nto fuel finitely many growth steps, before reaching a fixed point.")
        self.read(11)
        self.finish()
