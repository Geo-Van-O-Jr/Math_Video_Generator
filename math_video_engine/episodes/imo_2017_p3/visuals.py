"""Canonical boundary states. Every segment imports the same constructors."""
from manim import *
from engine.components.living_canvas import *


def game_diagram():
    axis = VGroup(Arrow([-5.8,-1.65,0],[5.8,-1.65,0],buff=0,
                        stroke_width=1.4,color=MUTED,max_tip_length_to_length_ratio=.018),
                  Arrow([-5.35,-2,0],[-5.35,2.7,0],buff=0,
                        stroke_width=1.4,color=MUTED,max_tip_length_to_length_ratio=.04))
    h0, h1 = [-4.45,-.75,0], [-2.45,-.75,0]
    r0, r1, p = [-.05,1.05,0],[1.95,1.05,0],[3,.55,0]
    h = TrackedPoint(h0,"H",BLUE,LEFT)
    hend = TrackedPoint(h1,color=BLUE)
    hm = Arrow(h0,h1,buff=.14,color=BLUE,stroke_width=2.5)
    hl = math(r"|\Delta H|=1",29,BLUE).next_to(hm,DOWN,.17)
    r = TrackedPoint(r0,"R",GOLD,LEFT,icon="rabbit")
    rend = TrackedPoint(r1,color=GOLD,icon="rabbit")
    rm = DashedTrajectory(r0,r1,GOLD)
    rl = math(r"|\Delta R|=1",29,GOLD).next_to(rm,UP,.4)
    disk = UncertaintyDisk(p,2,GREEN)
    ping = TrackedPoint(p,"P",GREEN,RIGHT)
    err = DashedTrajectory(p,r1,GREEN)
    errlabel = math(r"PR\leq 1",26,GREEN).move_to([3.3,1.65,0])
    radius = Arrow(p,[4.4,-.878,0],buff=.08,color=GREEN,stroke_width=1.4)
    radlabel = math("1",26,GREEN).move_to([4.05,-.03,0])
    # The region is behind its points and trajectories.
    parts = dict(axis=axis,disk=disk,h=h,hend=hend,hm=hm,hl=hl,r=r,
                 rend=rend,rm=rm,rl=rl,ping=ping,err=err,errlabel=errlabel,
                 radius=radius,radlabel=radlabel)
    group = VGroup(*parts.values())
    return group,parts


def game_state():
    group,parts=game_diagram()
    question=math(r"10^9\ \text{rounds}\qquad HR\leq100\ ?",38,MINT).move_to([0,-2.8,0])
    return VGroup(group,question),parts


def block_state():
    # Affine schematic: vertical separations enlarged; all labels are exact.
    h=np.array([-5.3,.25,0]); r=np.array([-3.45,.25,0])
    top=np.array([4.55,1.9,0]); bottom=np.array([4.55,-1.4,0])
    hp=np.array([3.15,.25,0]); z=np.array([4.55,.25,0])
    rp=np.array([5.0,.25,0])
    axis=DashedLine([-6.0,.25,0],[5.9,.25,0],dash_length=.12,
                    color=MUTED,stroke_width=1.4)
    hunter=TrackedPoint(h,"H_n",BLUE,DOWN,icon="hunter")
    rabbit=TrackedPoint(r,"R_n",GOLD,UP,icon="rabbit")
    distance=DistanceAnnotation(h+DOWN*.8,r+DOWN*.8,"d_n",DOWN,color=IVORY)
    fact=math(r"d_n=H_nR_n",31).move_to([-4.4,2.9,0])
    note=prose(r"Schematic: transverse separation and $\varepsilon$ enlarged.",19,MUTED).move_to([2.4,-3.3,0])
    group=VGroup(axis,hunter,rabbit,distance,fact,note)
    return group,dict(axis=axis,h=h,r=r,top=top,bottom=bottom,hp=hp,z=z,rp=rp,
                      hunter=hunter,rabbit=rabbit,distance=distance,fact=fact,note=note)


def routes_state():
    group,p=block_state()
    choices=SymmetricChoices(p['r'],p['top'],.25)
    upper=math("200",28,PINK).move_to([.4,1.5,0])
    lower=math("200",28,BLUE).move_to([.4,-1.0,0])
    cross=VGroup(DistanceAnnotation(p['z'],p['top'],"1",RIGHT,color=PINK),
                 DistanceAnnotation(p['z'],p['bottom'],"1",RIGHT,color=BLUE))
    ping=TrackedPoint(p['z'],"P_{200}=Z",GREEN,LEFT)
    # Label on the line's left would collide with H'; relocate it below.
    ping.label.move_to([4.55,-.22,0])
    same=prose("Same information. Same hunter strategy.",32).move_to([0,2.95,0])
    group.remove(p['fact'])
    group.add(choices,upper,lower,cross,ping,same)
    p.update(choices=choices,upper=upper,lower=lower,cross=cross,ping=ping,same=same)
    return group,p


def estimate_state():
    group,p=routes_state()
    group.remove(p['same'],p['ping'])
    hp=TrackedPoint(p['hp'],"H'",BLUE,DOWN)
    rp=TrackedPoint(p['rp'],"R'",GOLD,DOWN)
    zz=TrackedPoint(p['z'],"Z",IVORY,LEFT)
    zz.label.shift(DOWN*.22)
    ys=VGroup(Line(p['hp'],p['top'],color=IVORY,stroke_width=1.6),
              Line(p['hp'],p['bottom'],color=IVORY,stroke_width=1.6))
    yl=math("y",30).move_to([3.5,1.38,0])
    eps=DistanceAnnotation(p['z']+UP*.5,p['rp']+UP*.5,r"\varepsilon",UP,color=GOLD)
    eps.label.shift(RIGHT*.7)
    base=math(r"H'Z=d_n-\varepsilon",29).move_to([1.9,-2.1,0])
    title=prose("One of the two endpoints is at least $y$ away.",32).move_to([0,2.95,0])
    group.add(hp,rp,zz,ys,yl,eps,base,title)
    p.update(hprime=hp,rprime=rp,zz=zz,ys=ys,yl=yl,eps=eps,base=base,title=title)
    return group,p


def compact_estimate():
    group,p=estimate_state()
    group.remove(p['title'],p['note'])
    group.scale(.72).move_to([0,1.3,0])
    note=prose(r"Schematic: transverse separation and $\varepsilon$ enlarged.",18,MUTED).move_to([0,-.62,0])
    group.add(note)
    group.named_objects=p
    return group


def result_state():
    diagram=compact_estimate()
    condition=math(r"2\leq d_n\leq100",30,MUTED).move_to([-4.5,3.2,0])
    result=ResultHighlight(math(r"d_{n+200}^{\,2}>d_n^2+\frac12",44,BLUE),BLUE)
    result.move_to([0,-1.55,0])
    line=prose("A definite increase, every $200$ rounds.",32).move_to([0,-2.75,0])
    return VGroup(diagram,condition,result,line)
