"""Static states of one persistent statement diagram; no animation code."""
from manim import *
from engine import reference_theme as T
from engine.components.reference_visuals import *


def character_icon(name,point,color,height):
    """Keep geometry behind the silhouette while retaining the approved glow."""
    visible=glow_icon(name,point,color,height=height)
    silhouette=visible[-1].copy().set_fill(T.BG,opacity=1).set_stroke(T.BG,width=T.PRIMARY_STROKE)
    return VGroup(silhouette,visible)


def statement_geometry(state):
    if state not in ('opening','initial','generic','rabbit','tracking','hunter','question'):
        raise ValueError(state)
    h=np.array([2.03,-1.16,0]); r=np.array([5.0,.40,0]); unit=1.25
    step=unit*np.array([np.cos(45*DEGREES),np.sin(45*DEGREES),0])
    group=VGroup()
    if state in ('opening','initial'):
        origin=np.array([4.2,.2,0])
        # Offset glyphs are callouts to ONE geometric anchor, not two positions.
        hunter=character_icon('hunter',origin+[-.42,.35,0],T.BLUE,height=.65)
        rabbit=character_icon('rabbit',origin+[.42,.35,0],T.GOLD,height=.65)
        group.add(glow_line(origin,origin+[-.42,.05,0],T.BLUE),
                  glow_line(origin,origin+[.42,.05,0],T.GOLD),
                  glow_dot(origin,T.TEXT_PRIMARY,radius=.045),hunter,rabbit)
        group.add(formula('B_0',T.LABEL,T.BLUE).next_to(hunter,LEFT,buff=.12),
                  formula('A_0',T.LABEL,T.GOLD).next_to(rabbit,RIGHT,buff=.12))
        if state=='initial':
            group.add(formula('A_0=B_0',T.MATH).move_to(origin+[0,1.18,0]))
        group.anchor_positions={'hunter':origin.copy(),'rabbit':origin.copy()}
        return group
    rabbit_moved=state in ('rabbit','tracking','hunter','question')
    hunter_moved=state in ('hunter','question')
    rp=r+step if rabbit_moved else r
    hp=h+step if hunter_moved else h
    if rabbit_moved:
        move=VGroup(dashed_circle(r,unit,T.BLUE),glow_arrow(r,rp,T.BLUE),
                    formula('1',T.LABEL,T.BLUE_SOFT).move_to(r+[-.60,-.85,0]),
                    glow_dot(r,T.GOLD,radius=.047,active=False))
        if state!='rabbit': move.fade(1-T.HISTORY_OPACITY)
        group.add(move)
    if state in ('tracking','hunter','question'):
        p=rp+[-.65,-.30,0]
        tracker=VGroup(uncertainty_disk(p,unit,T.GREEN_SOFT),
                       glow_line(p,rp,T.GREEN_SOFT),glow_dot(p,T.GREEN_SOFT,radius=.085),
                       formula('P_n',T.LABEL,T.GREEN_SOFT).move_to(p+[-.50,-.38,0]),
                       formula(r'|P_nA_n|\leq1',T.LABEL,T.GREEN).move_to([4.9,2.65,0]))
        if state!='tracking': tracker.fade(1-T.SECONDARY_OPACITY)
        group.add(tracker)
    if hunter_moved:
        move=VGroup(dashed_circle(h,unit,T.BLUE),glow_arrow(h,hp,T.BLUE),
                    formula('1',T.LABEL,T.BLUE_SOFT).move_to(h+step/2+[-.30,.20,0]),
                    glow_dot(h,T.BLUE,radius=.047,active=False))
        if state!='hunter': move.fade(1-T.HISTORY_OPACITY)
        group.add(move)
    hunter=character_icon('hunter',hp,T.BLUE,height=.60)
    rabbit=character_icon('rabbit',rp,T.GOLD,height=.65)
    hunter_label=formula('B_n' if hunter_moved else 'B_{n-1}',T.LABEL,T.BLUE).next_to(hunter,DOWN,buff=.10)
    rabbit_label=formula('A_n' if rabbit_moved else 'A_{n-1}',T.LABEL,T.GOLD).next_to(rabbit,DOWN,buff=.10)
    group.add(VGroup(hunter,hunter_label),VGroup(rabbit,rabbit_label))
    if state=='question':
        group.add(serif(accent('$10^9$',T.GREEN)+' rounds',T.BODY).move_to([5.15,-2.46,0]))
    group.anchor_positions={'hunter':hp.copy(),'rabbit':rp.copy()}
    check_bounds(group,region=T.RIGHT_DIAGRAM_COLUMN)
    return group
