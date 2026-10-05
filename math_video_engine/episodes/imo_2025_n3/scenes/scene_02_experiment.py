from engine.base_scene import MathScene


class EpisodeScene(MathScene):
    def construct(self):
        self.heading("A number that survives", 2)
        self.equation(r"864", r"432,\quad288,\quad216",
                      caption="Start with 864. These are its three largest proper divisors.", hold=6)
        self.equation(r"432+288+216=936", r"864\longrightarrow936",
                      caption="Their sum becomes the next term.", hold=6)
        self.equation(r"468+312+234=1014", r"936\longrightarrow1014",
                      caption="Apply exactly the same rule again.", hold=6)
        self.equation(r"507+338+169=1014", r"1014\longrightarrow1014",
                      caption="Now the next term equals the current one.", hold=6)
        self.result(r"864\longrightarrow936\longrightarrow1014\longrightarrow1014\longrightarrow\cdots",
                    caption="Some numbers grow for a while and then freeze.", hold=6)
        self.replace_caption("Why?")
        self.read(3)
        self.finish()
