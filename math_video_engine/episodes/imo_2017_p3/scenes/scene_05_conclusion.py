from manim import *
from engine.components.living_canvas import *
from episodes.imo_2017_p3.visuals import result_state


class EpisodeScene(PersistentCanvas):
    def construct(self):
        state=result_state(); self.add(state)
        self.wait(.6)
        proof=ProofWriter(self)
        # Reuse the proved gain as a remembered fact at the top right.
        previous=state[0].named_objects
        self.remove(state[0]); self.add(*state[0])
        self.play(state[2].animate.scale(.90).move_to([2.75,2.15,0]),
                  FadeOut(state[1]),FadeOut(state[3]),
                  *[FadeOut(obj) for obj in state[0]
                    if obj not in (previous['hunter'],previous['rabbit'])],run_time=2)
        scope=prose(r"While $d_n\leq100$, in $200$ rounds:",27,MUTED).move_to([2.75,3.05,0])
        self.play(Write(scope),run_time=1.6)
        hunter=TrackedPoint([-4.0,-.15,0],color=BLUE,icon="hunter")
        rabbit=TrackedPoint([-2.9,.9,0],color=GOLD,icon="rabbit")
        radial=Line(hunter.location(),rabbit.location(),color=IVORY,stroke_width=1.5)
        old=DashedVMobject(Circle(radius=1.52,color=MUTED,stroke_width=1.2),num_dashes=60)
        old.move_to(hunter.location())
        dl=math("d",32).move_to([-3.7,.8,0])
        geometry=VGroup(old,radial,hunter,rabbit,dl)
        self.play(ReplacementTransform(previous['hunter'],hunter),
                  ReplacementTransform(previous['rabbit'],rabbit),run_time=1.8)
        self.play(Create(old),Create(radial),Write(dl),run_time=1.8)
        grown=DashedVMobject(Circle(radius=2.35,color=BLUE,stroke_width=1.4),num_dashes=74)
        grown.move_to(hunter.location())
        endpoint=np.array([-2.35,1.525,0])
        newrabbit=TrackedPoint(endpoint,color=GOLD,icon="rabbit")
        arrow=Arrow(hunter.location(),endpoint,buff=.13,color=BLUE,stroke_width=1.8)
        newlabel=math(r"d_{\rm new}",30,BLUE).move_to([-4.4,2.5,0])
        self.play(TransformFromCopy(old,grown),TransformFromCopy(rabbit,newrabbit),
                  GrowArrow(arrow),Write(newlabel),rabbit.animate.set_opacity(.28),run_time=2.4)
        caption=prose("At block endpoints",24,MUTED).move_to([-4.0,-2.95,0])
        self.play(Write(caption),run_time=1)
        writer=EquationDerivation(self,anchor=[2.65,.5,0],width=7)
        definition=writer.write_math(r"D_j=d_{1+200j},\qquad D_0=2",size=30)
        self.cue("Block endpoints begin with the first-round separation",4)
        writer.transform_last(r"D_N^2>4+\frac{N}{2}",size=41)
        condition=proof.write("Until the distance exceeds $100$.",[2.65,-.6,0],size=28,color=MUTED)
        self.cue("Accumulate the squared-distance increase",5)
        writer.transform_last(r"4+\frac{19{,}992}{2}=10^4",size=39)
        self.cue("The strict increment crosses 100, not just reaches it",5)
        blocks=math(r"N\leq19{,}992<2\cdot10^4",34,GOLD).move_to([2.65,-.8,0])
        self.play(ReplacementTransform(condition,blocks),run_time=1.6)
        self.cue("Fewer than twenty thousand blocks suffice",4)
        writer.transform_last(r"T\leq1+200\cdot19{,}992",size=36)
        counted=proof.write("Including the initial round.",[2.65,-1.8,0],size=26,color=MUTED)
        self.cue("Account for every round",4)
        writer.transform_last(r"T<200\cdot2\cdot10^4",size=40)
        self.cue("A clean four-million upper bound",4)
        self.play(FadeOut(blocks),FadeOut(counted),run_time=1)
        # Bring the numerical comparison into place in the requested order.
        four=math(r"4{,}000{,}000",44,GOLD).move_to([1.4,-.2,0])
        billion=math(r"10^9",44,BLUE).move_to([5.3,-.2,0])
        lt=math("<",44,BLUE).move_to([4.1,-.2,0])
        self.play(ReplacementTransform(writer.last,four),run_time=1.8)
        goldbox=ResultHighlight(four,GOLD)
        self.play(Create(goldbox[0]),Create(goldbox[1]),run_time=1)
        self.play(Write(billion),run_time=1.3)
        bluebox=ResultHighlight(billion,BLUE)
        self.play(Create(bluebox[0]),Create(bluebox[1]),run_time=.8)
        self.play(Write(lt),run_time=1)
        enough=prose("Fewer than four million rounds suffice.",32).move_to([2.3,-1.55,0])
        self.play(Write(enough),run_time=2)
        self.cue("quantitative_conclusion",6)
        maintained=math(r"d_T>100\quad\Longrightarrow\quad d_{10^9}>100",37,MINT)
        maintained.move_to([0,-2.8,0])
        self.play(Write(maintained),run_time=2.3)
        self.cue("Moving away preserves the strict separation to the final round",5)
        answer=ResultHighlight(prose("No. The hunter cannot guarantee a distance of at most $100$.",31),MINT)
        answer.move_to([0,-2.8,0])
        self.play(ReplacementTransform(maintained,answer),run_time=1.8)
        self.cue("The answer to the official question",8)
