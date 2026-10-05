from manim import *
from engine.components.living_canvas import *
from episodes.imo_2017_p3.visuals import estimate_state,compact_estimate,result_state


class EpisodeScene(PersistentCanvas):
    def construct(self):
        diagram,p=estimate_state(); self.add(diagram)
        self.wait(.6)
        self.play(FadeOut(p['title']),FadeOut(p['note']),run_time=1)
        diagram.remove(p['title'],p['note'])
        compact=compact_estimate()
        self.play(Transform(diagram,compact),run_time=2)
        proof=EquationDerivation(self,anchor=[0,-1.55,0],width=12)
        assumption=math(r"2\leq d_n<100",30,MUTED).move_to([-4.5,3.2,0])
        self.play(Write(assumption),run_time=1.5)
        proof.write_math(r"y^2=1+(d_n-\varepsilon)^2",size=43)
        self.cue("Pythagoras in the smaller triangle",5)
        remembered=proof.last
        proof.pin_fact(remembered,[3.0,3.2,0],scale=.63)
        proof.last=None
        proof.write_math(r"\varepsilon=200-\sqrt{200^2-1}",size=41)
        description=proof.write("The tiny loss in forward progress.",[0,-2.65,0],size=29,color=GOLD)
        self.cue("Pythagoras in the 200-unit triangle",5)
        proof.transform_last(r"\varepsilon=\frac{1}{200+\sqrt{200^2-1}}",size=41)
        self.cue("Rationalize the difference",5)
        proof.transform_last(r"\varepsilon=\frac{1}{200+\sqrt{200^2-1}}>\frac{1}{400}",size=41)
        self.cue("A strict lower bound for epsilon",5)
        bound=math(r"\varepsilon>\frac1{400}",29,GOLD).move_to([-4.9,-2.85,0])
        self.play(TransformFromCopy(proof.last,bound),FadeOut(description),run_time=1.4)
        proof.transform_last(r"(200-\varepsilon)^2=200^2-1",size=41)
        self.cue("The same right triangle gives an exact identity",4)
        proof.transform_last(r"\varepsilon^2+1=400\varepsilon",size=42,color=GOLD)
        self.cue("Exact epsilon identity",5)
        identity=proof.last
        proof.pin_fact(identity,[3.9,-2.85,0],scale=.68)
        proof.last=remembered
        proof.transform_last(r"y^2=1+(d_n-\varepsilon)^2",pos=[0,-1.55,0],size=43)
        self.wait(2)
        proof.transform_last(r"y^2=d_n^2-2\varepsilon d_n+\varepsilon^2+1",size=41)
        self.cue("Expand the squared distance",5)
        proof.transform_last(r"y^2=d_n^2+\varepsilon(400-2d_n)",size=42)
        self.cue("Substitute the exact identity",5)
        factor=math(r"400-2d_n>200",31,GOLD).move_to([0,-2.65,0])
        self.play(Write(factor),Indicate(assumption,color=GOLD),run_time=2)
        self.cue("The active assumption supplies the second bound",5)
        self.play(Indicate(bound,color=GOLD),Indicate(factor,color=GOLD),run_time=1.5)
        proof.transform_last(r"y^2>d_n^2+\frac12",size=45,color=BLUE)
        self.cue("Both bounds combine to give a uniform increment",5)
        boundary=prose("At $d_n=100$, the increment is still strictly greater than $1/2$.",28)
        boundary.move_to([0,-2.65,0])
        self.play(FadeOut(factor),FadeOut(identity),FadeOut(bound),run_time=.9)
        self.play(Write(boundary),run_time=2)
        inclusive=math(r"2\leq d_n\leq100",30,MUTED).move_to(assumption)
        self.play(ReplacementTransform(assumption,inclusive),run_time=1.3)
        self.cue("The contest's equality case is included",5)
        result=result_state()
        self.play(ReplacementTransform(proof.last,result[2][2]),run_time=1.6)
        self.play(Create(result[2][0]),Create(result[2][1]),
                  ReplacementTransform(boundary,result[3]),run_time=1.8)
        self.remove(*self.mobjects); self.add(result)
        self.cue("block_gain",5)
