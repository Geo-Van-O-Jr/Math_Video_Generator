from manim import *
from engine.components.living_canvas import *
from episodes.imo_2017_p3.visuals import block_state,routes_state,estimate_state


class EpisodeScene(PersistentCanvas):
    def construct(self):
        base,p=block_state(); self.add(base)
        proof=ProofWriter(self)
        construction=proof.write("Two possible destinations. Each $200$ units from $R_n$.",
                                  [0,2.95,0],size=31)
        self.play(FadeOut(p['fact']),run_time=.7)
        choices=SymmetricChoices(p['r'],p['top'],.25)
        self.play(Create(choices.routes[0]),FadeIn(choices.ends[0]),run_time=2.5)
        upper=math("200",28,PINK).move_to([.4,1.5,0])
        self.play(Write(upper),run_time=1)
        self.cue("First route constructed",2)
        reflected=choices.ends[0].copy()
        self.add(reflected)
        self.play(Transform(reflected,choices.ends[1]),Create(choices.routes[1]),run_time=2.5)
        self.remove(reflected); self.add(choices.ends[1])
        lower=math("200",28,BLUE).move_to([.4,-1,0])
        cross=VGroup(DistanceAnnotation(p['z'],p['top'],"1",RIGHT,color=PINK),
                     DistanceAnnotation(p['z'],p['bottom'],"1",RIGHT,color=BLUE))
        self.play(Write(lower),Create(cross),run_time=2)
        midpoint=TrackedPoint(p['z'],'Z',IVORY,LEFT)
        midpoint.label.shift(DOWN*.22)
        self.play(FadeIn(midpoint),run_time=.8)
        self.cue("Reflected routes: 200 along each path, one off the line",4)
        sentence=prose("Follow either straight route, one unit per round.",31).move_to([0,2.95,0])
        self.play(ReplacementTransform(construction,sentence),run_time=1.5)
        # A single parameter drives both hypothetical rabbits and the same ping.
        # The displayed map is affine; the exact world coordinates are given below.
        t=ValueTracker(0)
        a=p['r']; du=p['top']-a; dl=p['bottom']-a
        rabbit1=always_redraw(lambda: TrackedPoint(a+t.get_value()*du,color=PINK,icon="rabbit"))
        rabbit2=always_redraw(lambda: TrackedPoint(a+t.get_value()*dl,color=BLUE,icon="rabbit"))
        ping=always_redraw(lambda: Dot(a+t.get_value()*(p['z']-a),radius=.07,color=GREEN))
        tie1=always_redraw(lambda: Line(a+t.get_value()*(p['z']-a),a+t.get_value()*du,
                                         color=GREEN,stroke_width=1.4))
        tie2=always_redraw(lambda: Line(a+t.get_value()*(p['z']-a),a+t.get_value()*dl,
                                         color=GREEN,stroke_width=1.4))
        self.play(p['rabbit'].animate.set_opacity(.25),FadeIn(rabbit1),FadeIn(rabbit2),
                  FadeIn(ping),FadeIn(tie1),FadeIn(tie2),run_time=.8)
        formula=math(r"P_k=R_n+\frac{k}{200}(Z-R_n)",31,GREEN).move_to([0,-2.25,0])
        self.play(Write(formula),run_time=2)
        # Four long traced movements, separated by actual admissible common pings.
        pingdots=VGroup()
        for value in (.20,.45,.70,1.0):
            self.play(t.animate.set_value(value),run_time=3,rate_func=linear)
            dot=Dot(a+value*(p['z']-a),radius=.034,color=GREEN)
            self.add(dot)
            pingdots.add(dot)
            self.play(Flash(ping.get_center(),color=GREEN,flash_radius=.18,
                            line_length=.08,num_lines=8),run_time=.6)
        error=math(r"|P_kR_{n+k}^{\,+}|=|P_kR_{n+k}^{\,-}|=\frac{k}{200}\leq1",
                   32,GREEN).move_to([0,-2.85,0])
        self.play(Write(error),run_time=2.5)
        self.cue("Both moving rabbits remain compatible with every common ping",6)
        same=prose("Same information.",35).move_to([0,2.95,0])
        self.play(ReplacementTransform(sentence,same),run_time=1.2)
        self.wait(2)
        same2=prose("Same information. Same hunter strategy.",32).move_to([0,2.95,0])
        self.play(ReplacementTransform(same,same2),run_time=1.5)
        self.cue("two_worlds",5)
        # Continue from these two endpoints; the minimax argument is spatial.
        self.play(FadeOut(rabbit1),FadeOut(rabbit2),FadeOut(tie1),FadeOut(tie2),
                  FadeOut(ping),FadeOut(formula),FadeOut(error),FadeOut(pingdots),run_time=1.2)
        travel=math(r"|H_nQ|\leq200",33,BLUE).move_to([-3,-2.35,0])
        self.play(Write(travel),run_time=1.5)
        positive=math(r"2\leq d_n\leq100",26,MUTED).move_to([-3.8,2.2,0])
        self.play(Write(positive),run_time=1)
        favorable=Arrow(p['h'],p['hp'],buff=.12,color=BLUE,stroke_width=2)
        hp=TrackedPoint(p['hp'],"H'",BLUE,DOWN)
        self.play(GrowArrow(favorable),TransformFromCopy(p['hunter'].marker,hp),run_time=2.8)
        reach=math("200",27,BLUE).next_to(favorable,DOWN,.65)
        self.play(Write(reach),run_time=1)
        endpoint=MovingPoint(p['hp'],"Q",BLUE,LEFT)
        self.play(FadeIn(endpoint),run_time=.6)
        worse=always_redraw(lambda: Line(endpoint.location(),
            p['bottom'] if endpoint.location()[1] >= .25 else p['top'],
            color=GOLD,stroke_width=2))
        self.add(worse)
        above=prose("Above the line: $Y_2$ is farther.",31).move_to([0,-2.95,0])
        self.play(Write(above),endpoint.move_marker_to([2.3,1.1,0]),run_time=2.2)
        self.cue("Above-line endpoint exposes the lower route",3)
        below=prose("Below the line: $Y_1$ is farther.",31).move_to([0,-2.95,0])
        self.play(ReplacementTransform(above,below),endpoint.move_marker_to([2.3,-.6,0]),run_time=2.2)
        self.cue("Below-line endpoint exposes the upper route",3)
        limit=prose("No reachable endpoint lies to the right of $H'$.",31).move_to([0,-2.95,0])
        boundary=DashedLine([3.15,-1.5,0],[3.15,2,0],color=BLUE,stroke_width=1)
        self.play(ReplacementTransform(below,limit),Create(boundary),
                  endpoint.move_marker_to(p['hp']),run_time=2)
        self.cue("H prime minimizes the maximum of the two distances",4)
        self.play(FadeOut(endpoint),FadeOut(worse),FadeOut(boundary),FadeOut(limit),
                  FadeOut(travel),FadeOut(reach),FadeOut(favorable),FadeOut(positive),run_time=1.1)
        state,q=estimate_state()
        self.play(ReplacementTransform(same2,q['title']),Create(q['ys']),Write(q['yl']),run_time=2)
        forward=Arrow(p['r'],p['rp'],buff=.1,color=GOLD,stroke_width=1.5)
        lengths=math(r"R_nR'=H_nH'=200",31,GOLD).move_to([0,-2.65,0])
        self.play(FadeIn(q['rprime']),GrowArrow(forward),Write(lengths),run_time=2)
        self.cue("R prime lies 200 units along the central line",3)
        translated=math(r"H'R'=H_nR_n=d_n",31).move_to(lengths)
        self.play(ReplacementTransform(lengths,translated),FadeOut(forward),run_time=1.5)
        self.cue("Equal forward translations preserve the original gap",3)
        self.play(Create(q['eps']),Write(q['base']),FadeOut(translated),run_time=2.5)
        # Canonicalize at a held state, identical to the objects just constructed.
        self.play(p['rabbit'].animate.set_opacity(1),run_time=.6)
        self.remove(*self.mobjects); self.add(state)
        self.cue("estimate_geometry",5)
