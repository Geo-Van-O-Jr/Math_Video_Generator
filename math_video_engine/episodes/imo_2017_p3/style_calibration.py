"""First gate: typography and vector finishing, before reference compositions."""
from manim import *
from engine import reference_theme as T
from engine.components.reference_visuals import *

config.frame_width=T.FRAME_WIDTH
config.frame_height=T.FRAME_HEIGHT


class StyleCalibration(ReferenceStill):
    def construct(self):
        title=serif('A language for a beautiful proof',T.TITLE_SIZE,role='title')
        title.move_to([0,3.75,0])
        subtitle=serif('Serif typography. Luminous geometry. Deliberate emphasis.',T.BODY_SMALL,
                       T.TEXT_SECONDARY).move_to([0,2.86,0])
        body=paragraph([
            'A hunter and an '+accent('invisible rabbit',T.GOLD,True),
            'play a game in the Euclidean plane.',
            'Moves have length '+accent('exactly 1 unit',T.BLUE,True)+'.',
        ],size=T.BODY,leading=.60)
        place_text_column(body,top=1.95)
        muted=paragraph(['Past information remains available,',
                         'quietly behind the active argument.'],size=T.BODY_SMALL,
                        color=T.TEXT_MUTED,leading=.52)
        place_text_column(muted,top=-.25)
        equation=formula(r'|P_kR_{n+k}|\leq1',T.MATH,T.GREEN_SOFT).move_to([-3.4,-1.65,0])
        question=serif('Can the hunter get '+accent('within 100',T.GREEN,True)+'?',T.BODY_LARGE)
        question.move_to([0,-3.62,0])
        box=glow_box(question,T.GREEN,width=12.9,height=T.QUESTION_HEIGHT,border=T.BOX_BORDER_COLOR)
        disk=uncertainty_disk([4.2,.75,0],1.38,T.GREEN_SOFT)
        hunter=glow_dot([1.38,.45,0],T.BLUE)
        rabbit=glow_icon('rabbit',[4.60,1.18,0],T.GOLD,height=.86)
        hlabel=formula('H',T.LABEL,T.BLUE).next_to(hunter.core,DOWN,buff=.19)
        rlabel=formula('R',T.LABEL,T.GOLD).move_to([5.32,1.0,0])
        path=dashed_path([[1.38,.45,0],[2.35,.30,0],[3.15,.7,0],[4.45,1.0,0]],T.BLUE)
        primary=glow_arrow([1.38,.45,0],[2.14,1.30,0],T.BLUE_SOFT)
        auxiliary=Line([1.38,-.6,0],[6.35,-.6,0],color=T.AUXILIARY_LINE_COLOR,
                       stroke_width=T.AUXILIARY_STROKE).set_opacity(.6)
        big=formula(r'd_{n+200}^{\,2}>d_n^2+\frac12',T.MATH_LARGE,T.BLUE_SOFT)
        big.move_to([3.8,-1.8,0])
        result=glow_box(big,T.GOLD)
        self.checked_add(title,subtitle,body,muted,equation,box,disk,hunter,rabbit,
                         hlabel,rlabel,path,primary,auxiliary,result)
        no_overlap(body,disk,.3)
        no_overlap(muted,equation,.2)
