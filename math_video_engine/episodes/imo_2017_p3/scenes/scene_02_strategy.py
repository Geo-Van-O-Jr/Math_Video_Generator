from manim import *
from engine.components.living_canvas import *
from episodes.imo_2017_p3.visuals import game_state,block_state


class EpisodeScene(PersistentCanvas):
    def construct(self):
        old,parts=game_state(); self.add(*old[0],old[1])
        proof=ProofWriter(self)
        self.wait(.5)
        definition=math(r"d_n=H_nR_n",39).move_to([0,2.8,0])
        self.play(ReplacementTransform(old[1],definition),run_time=1.5)
        h=MovingPoint([-3.6,.3,0],"H_n",BLUE,DOWN,icon="hunter")
        r=MovingPoint([.3,.3,0],"R_n",GOLD,UP,icon="rabbit")
        line=Line(h.location(),r.location(),color=MUTED,stroke_width=1.4)
        self.play(*[FadeOut(obj) for name,obj in parts.items() if name not in ('h','rend')],
                  ReplacementTransform(parts['h'],h),
                  ReplacementTransform(parts['rend'],r),Create(line),run_time=2)
        condition=proof.write_math(r"d_n>100",[-3.8,1.7,0],color=MINT)
        away=proof.write("Move straight away from the hunter.",[0,-1.5,0],size=32)
        rnext=r.location()+RIGHT
        arrow=Arrow(r.location(),rnext,buff=.05,color=GOLD)
        self.play(Create(arrow),r.move_marker_to(rnext),run_time=1.8)
        hnext=h.location()+RIGHT
        self.play(h.move_marker_to(hnext),run_time=1.8)
        monotone=math(r"d_{n+1}\geq(d_n+1)-1=d_n",37).move_to([0,-2.5,0])
        self.play(Write(monotone),run_time=2.3)
        self.cue("Once strictly beyond 100, moving away preserves it",5)
        self.play(FadeOut(condition),run_time=.6)
        equality=proof.write("At exactly $100$, use one more block.",[0,1.7,0],size=29,color=MUTED)
        self.cue("Equality must also be defeated",3)
        goal=prose("So we need to force the distance beyond $100$.",33).move_to([0,2.8,0])
        self.play(ReplacementTransform(definition,goal),FadeOut(away),FadeOut(monotone),
                  FadeOut(equality),FadeOut(arrow),FadeOut(line),run_time=1.3)
        start=TrackedPoint([0,.3,0],"O",GREEN,DOWN)
        self.play(h.animate.shift([2.6,0,0]),r.animate.shift([-1.3,0,0]),FadeIn(start),run_time=1.8)
        # h and r now coincide; a common ping hides the direction of the first jump.
        first=proof.write("Fix any hunter strategy. Report $P_1=O$.",[0,1.55,0],size=31)
        circle=UncertaintyDisk([0,.3,0],1.5,GREEN)
        self.play(GrowFromCenter(circle),run_time=1.4)
        self.bring_to_back(circle)
        ghost=Arrow([0,.3,0],[-1.5,.3,0],color=BLUE,buff=0).set_opacity(.35)
        self.play(Create(ghost),run_time=1.3)
        determined=proof.write("The hunter's first move is determined.",[0,-1.7,0],size=29)
        self.wait(3)
        choice=prose("Choose the rabbit's first move in the opposite direction.",29).move_to([0,-1.7,0])
        self.play(ReplacementTransform(determined,choice),run_time=1.4)
        self.play(r.move_marker_to([1.5,.3,0]),run_time=1.6)
        self.play(h.move_marker_to([-1.5,.3,0]),run_time=1.6)
        seed=math(r"d_1=2",38,GOLD).move_to([0,-2.65,0])
        self.play(Write(seed),run_time=1.4)
        self.cue("A legal first round creates positive separation",5)
        self.play(FadeOut(circle),FadeOut(start),FadeOut(ghost),FadeOut(first),FadeOut(choice),
                  FadeOut(goal),run_time=1.3)
        target,p=block_state()
        self.play(ReplacementTransform(h,p['hunter']),ReplacementTransform(r,p['rabbit']),
                  ReplacementTransform(seed,p['distance']),Create(p['axis']),run_time=2)
        self.play(Write(p['fact']),FadeIn(p['note']),run_time=1.2)
        reveal=proof.write("At the start of a block, reveal the rabbit's exact position.",
                           [0,1.65,0],size=30)
        self.play(Indicate(p['rabbit'],color=GOLD,scale_factor=1.15),run_time=1.5)
        history=proof.write("Even with this extra information, the hunter cannot win.",
                            [0,-2.25,0],size=29,color=MUTED)
        self.cue("The exact reveal removes uncertainty from all previous history",6)
        self.play(FadeOut(reveal),FadeOut(history),run_time=1.1)
        self.cue("block_start",2)
