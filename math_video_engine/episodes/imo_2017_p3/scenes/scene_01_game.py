from manim import *
from engine.components.living_canvas import *
from episodes.imo_2017_p3.visuals import game_diagram,game_state


class EpisodeScene(PersistentCanvas):
    def construct(self):
        proof=ProofWriter(self)
        context=proof.write("International Mathematical Olympiad",[0,1.6,0],size=39)
        city=proof.write("Rio de Janeiro, 2017",[0,.65,0],size=34,color=MUTED)
        count=proof.write("615 contestants.",[0,-.45,0],size=33,run_time=1.5)
        self.cue("Factual context",5)
        title=prose("IMO 2017 $\\cdot$ Problem 3",40).move_to([-2.9,3.05,0])
        self.play(ReplacementTransform(context,title),FadeOut(city),FadeOut(count),run_time=1.8)
        diagram,p=game_diagram()
        diagram.scale(.47).move_to([3.75,.45,0])
        writer=ProofWriter(self,width=7.4)
        opening=writer.write_lines([
            "A hunter and an invisible rabbit play a game",
            "in the Euclidean plane.",
            "The rabbit's starting point, $A_0$, and the hunter's",
            "starting point, $B_0$, are the same."
        ],[-2.5,1.4,0],size=29,run_time=1.7)
        common=TrackedPoint([3.4,.8,0],"A_0=B_0",IVORY,DOWN)
        self.play(FadeIn(common),run_time=1)
        self.cue("Statement: common starting position",6)
        history=writer.write_lines([
            "After $n-1$ rounds of the game, the rabbit is at",
            "point $A_{n-1}$ and the hunter is at point $B_{n-1}$.",
            "In the $n^{\\text{th}}$ round of the game,",
            "three things occur in order."
        ],[-2.5,-1.0,0],size=28,run_time=1.6)
        self.cue("Statement: round order",6)
        self.play(FadeOut(opening),FadeOut(history),FadeOut(common),run_time=1.2)
        first=writer.write_lines([
            "(i) The rabbit moves invisibly to a point $A_n$",
            "such that the distance between $A_{n-1}$ and $A_n$",
            "is exactly $1$."
        ],[-2.5,1.7,0],size=28,run_time=1.9)
        self.play(Create(p['axis']),FadeIn(p['r']),run_time=1.4)
        self.play(Create(p['rm']),TransformFromCopy(p['r'].marker,p['rend']),
                  Write(p['rl']),run_time=2.3)
        self.cue("Rabbit moves first, exactly one unit",4)
        second=writer.write_lines([
            "(ii) A tracking device reports a point $P_n$ to the hunter.",
            "The only guarantee provided by the tracking device",
            "to the hunter is that the distance between $P_n$",
            "and $A_n$ is at most $1$."
        ],[-2.5,-.2,0],size=27,run_time=2)
        self.play(FadeIn(p['ping']),GrowFromCenter(p['disk']),run_time=2)
        self.bring_to_back(p['disk'])
        self.play(Create(p['err']),Write(p['errlabel']),Create(p['radius']),Write(p['radlabel']),run_time=2)
        self.cue("The tracker gives a point, not a distance",6)
        third=writer.write_lines([
            "(iii) The hunter moves visibly to a point $B_n$",
            "such that the distance between $B_{n-1}$ and $B_n$",
            "is exactly $1$."
        ],[-2.5,-2.25,0],size=28,run_time=1.9)
        self.play(FadeIn(p['h']),run_time=.6)
        self.play(Create(p['hm']),TransformFromCopy(p['h'].marker,p['hend']),Write(p['hl']),run_time=2)
        self.cue("Official rules parsed beside growing geometry",6)
        self.play(FadeOut(first),FadeOut(second),FadeOut(third),run_time=1.2)
        question=writer.write_lines([
            "Is it always possible, no matter how the rabbit moves,",
            "and no matter what points are reported by the tracking",
            "device, for the hunter to choose her moves so that",
            "after $10^9$ rounds she can ensure that the distance",
            "between her and the rabbit is at most $100$?"
        ],[-2.5,.35,0],size=28,run_time=2)
        self.cue("problem_statement",11)
        self.play(FadeOut(question),FadeOut(title),run_time=1.3)
        # Consolidate components and expand the actual diagram, not a screenshot.
        self.remove(*p.values())
        self.add(diagram)
        target,unused=game_diagram()
        self.play(Transform(diagram,target),run_time=2.6)
        notation=proof.write(r"From here on: $R_n=A_n$, $H_n=B_n$.",[0,-2.5,0],size=28,color=MUTED)
        self.wait(3)
        canonical,_=game_state()
        self.play(ReplacementTransform(notation,canonical[1]),run_time=1.4)
        self.cue("game_geometry",5)
