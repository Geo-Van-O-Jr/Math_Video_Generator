"""Reference fidelity stills only; not included in episode.yaml or any video."""
from manim import *
from engine import reference_theme as T
from engine.components.reference_visuals import *
from engine.components.statement_geometry import statement_geometry, character_icon

config.frame_width=T.FRAME_WIDTH
config.frame_height=T.FRAME_HEIGHT


def statement_title():
    obj=serif(r'\textbf{IMO 2017} '+accent(r'$\cdot$ Problem 3',T.TEXT_SECONDARY),
              T.TITLE_SIZE,role='title')
    obj.move_to([T.LEFT_TEXT_COLUMN.left,T.SAFE_ZONE.top,0],aligned_edge=UL)
    return obj


def movement_vignette(state):
    return statement_geometry(state)


def statement_frame(scene,blocks,state="generic"):
    title=statement_title()
    paragraphs=VGroup()
    top=T.LEFT_TEXT_COLUMN.top
    for lines in blocks:
        block=paragraph(lines,size=T.BODY)
        place_text_column(block,top=top)
        paragraphs.add(block)
        top=block.get_bottom()[1]-T.BLOCK_SPACING
    diagram=movement_vignette(state)
    question=question_box() if state=="question" else VGroup()
    check_bounds(paragraphs,region=T.LEFT_TEXT_COLUMN)
    enforce_safe_gap(paragraphs,diagram,gap=T.COLUMN_GAP)
    if state=="question":
        no_overlap(paragraphs,question,gap=.25)
    scene.checked_add(title,paragraphs,diagram,question)


class ProblemOpeningReference(ReferenceStill):
    def construct(self):
        statement_frame(self,[['A hunter and an '+accent('invisible rabbit',T.GOLD,True),
                              'play a game in the Euclidean plane.']],state='opening')


class ProblemInitialReference(ReferenceStill):
    def construct(self):
        statement_frame(self,[
            ['A hunter and an '+accent('invisible rabbit',T.GOLD,True),
             'play a game in the Euclidean plane.'],
            ["The rabbit's starting point, $A_0$,",
             "and the hunter's starting point, $B_0$,", 'are the same.'],
        ],state='initial')


class ProblemStatementReference(ReferenceStill):
    def construct(self):
        statement_frame(self,[
            ['A hunter and an '+accent('invisible rabbit',T.GOLD,True),
             'play a game in the Euclidean plane.'],
            ["The rabbit's starting point, $A_0$,",
             "and the hunter's starting point, $B_0$,",
             'are the same.'],
            ['After $n-1$ rounds of the game,',
             'the rabbit is at point $A_{n-1}$ and',
             'the hunter is at point $B_{n-1}$.'],
        ])


class ProblemRulesReference(ReferenceStill):
    def construct(self):
        statement_frame(self,[
            ['In the $n^{\\rm th}$ round of the game,',
             'three things occur in order.'],
            ['(i) The rabbit moves invisibly to',
             'a point $A_n$ such that the distance',
             'between $A_{n-1}$ and $A_n$ is',
             accent('exactly $1$.',T.BLUE,True)],
        ],state='rabbit')


class ProblemTrackingReference(ReferenceStill):
    def construct(self):
        statement_frame(self,[
            ['(ii) A tracking device reports a point',
             '$P_n$ to the hunter. The only',
             'guarantee provided by the tracking',
             'device to the hunter is that the',
             'distance between $P_n$ and $A_n$ is',
             accent('at most $1$.',T.GREEN_SOFT,True)],
        ],state='tracking')


class ProblemHunterReference(ReferenceStill):
    def construct(self):
        statement_frame(self,[
            ['(iii) The hunter moves visibly to',
             'a point $B_n$ such that the distance',
             'between $B_{n-1}$ and $B_n$ is '+accent('exactly $1$.',T.BLUE,True)],
        ],state='hunter')


class ProblemQuestionReference(ReferenceStill):
    def construct(self):
        statement_frame(self,[
            ['Is it always possible, no matter how',
             'the rabbit moves, and no matter',
             'what points are reported by the',
             'tracking device, for the hunter to',
             'choose her moves so that after '+accent('$10^9$',T.GREEN),
             'rounds she can ensure that the',
             'distance between her and the rabbit',
             'is '+accent('at most $100$?',T.GREEN,True)],
        ],state='question')


class TwoWorldsReference(ReferenceStill):
    def construct(self):
        title=serif('Two indistinguishable possible worlds',T.TITLE_SIZE,role='title')
        title.move_to([0,T.SAFE_ZONE.top,0],aligned_edge=UP)
        subtitle=serif('The same tracker reports are valid in both worlds.',T.SUBTITLE_SIZE,
                       T.TEXT_SECONDARY).move_to([0,3.02,0])
        # Rotate the official construction: B_n, A_n and all common pings
        # lie on the vertical axis; Y_1 and Y_2 are its reflected endpoints.
        # The final unit-error disk is independently enlarged for visibility.
        r=np.array([0,-.68,0]); h=np.array([0,-1.38,0]); z=np.array([0,1.22,0])
        y1=np.array([-4.25,1.22,0]); y2=np.array([4.25,1.22,0])
        region=split_uncertainty_region(z,width=8.5,height=2.6)
        # Leave a clean label pocket around Z=P_200.
        axis=VGroup(*[DashedLine([0,a,0],[0,b,0],dash_length=T.DASH_LENGTH,
                        color=T.AXIS_COLOR,stroke_width=T.AUXILIARY_STROKE)
                      for a,b in ((-1.60,1.58),(2.24,2.52))])
        axis.set_opacity(T.SECONDARY_OPACITY)
        paths=VGroup(dashed_path([r,y1],T.RED,curve=False),
                     dashed_path([r,y2],T.BLUE,curve=False))
        radii=VGroup(glow_arrow(z,y1,T.RED_SOFT),glow_arrow(z,y2,T.BLUE_SOFT))
        one_left=formula('1',T.LABEL,T.RED_SOFT).move_to([-2.2,1.56,0])
        one_right=formula('1',T.LABEL,T.BLUE_SOFT).move_to([2.2,1.56,0])
        labels=VGroup(
            formula('Y_1',T.MATH_LARGE,T.RED).move_to([-4.60,1.85,0]),
            formula('Y_2',T.MATH_LARGE,T.BLUE).move_to([4.60,1.85,0]),
            formula('A_n',T.LABEL,T.GOLD).move_to([.53,-.69,0]),
            formula('B_n',T.LABEL,T.BLUE_SOFT).move_to([-.65,-1.16,0]),
            formula('Z=P_{200}',T.LABEL,T.TEXT_PRIMARY).move_to([0,1.91,0]),
            formula('200',T.LABEL,T.RED_SOFT).move_to([-2.55,-.14,0]),
            formula('200',T.LABEL,T.BLUE_SOFT).move_to([2.55,-.14,0]),
        )
        pings=VGroup()
        crossbars=VGroup()
        for t in (.25,.50,.75):
            p=r+t*(z-r)
            pings.add(glow_dot(p,T.GREEN_SOFT,radius=.045))
            start,end=r+t*(y1-r),r+t*(y2-r)
            segments=[(start,end)] if t!=.50 else [(start,np.array([.25,p[1],0])),
                                                   (np.array([1.03,p[1],0]),end)]
            for a,b in segments:
                crossbars.add(Line(a,b,color=T.GREEN_SOFT,
                    stroke_width=T.AUXILIARY_STROKE).set_opacity(T.CONSTRUCTION_OPACITY))
        pinglabel=formula('P_k',T.LABEL,T.GREEN_SOFT).move_to([.64,.26,0])
        points=VGroup(glow_dot(y1,T.RED),glow_dot(y2,T.BLUE),
                      glow_dot(z,T.TEXT_PRIMARY),character_icon('rabbit',r,T.GOLD,height=.53),
                      character_icon('hunter',h,T.BLUE,height=.48))
        equation=formula(r'|P_kA_{n+k}^{(+)}|=|P_kA_{n+k}^{(-)}|=\frac{k}{200}\leq1',
                         T.MATH,T.TEXT_PRIMARY).move_to([0,-2.14,0])
        conclusion=serif('Same information. '+accent('Same hunter strategy.',T.GOLD,True),T.BODY_LARGE)
        conclusion.move_to([0,-3.28,0])
        box=glow_box(conclusion,T.GOLD,width=12.25,height=.83)
        note=serif('Schematic: transverse scale and the final error disk are enlarged.',T.FOOTNOTE,
                   T.TEXT_SECONDARY,role='note').move_to([0,-4.00,0])
        self.checked_add(title,subtitle,region,axis,crossbars,paths,radii,
                         pings,points,labels,pinglabel,one_left,one_right,equation,box,note)
        no_overlap(title,subtitle,.12)
        no_overlap(subtitle,region,.20)
        no_overlap(equation,box,.13)
        no_overlap(box,note,.14)
        no_overlap(labels[3],equation,.12)
