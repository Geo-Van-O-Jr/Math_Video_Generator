"""Large serif typography, luminous vectors and checked composition regions."""
from pathlib import Path
import numpy as np
from manim import *
from engine import reference_theme as T


def accent(text, color=T.GOLD, bold=False):
    content = r'\textbf{' + text + '}' if bold else text
    return r'\textcolor[HTML]{' + color.lstrip('#') + '}{' + content + '}'


def question_box():
    """Frozen statement payoff; callers control its late entrance."""
    content=serif('Can the hunter guarantee getting '+accent('within 100',T.GREEN)+'?',T.BODY)
    content.move_to([0,T.QUESTION_Y,0])
    if content.width>T.QUESTION_WIDTH-2*T.BOX_PADDING_X:
        raise ValueError('Question needs explicit reflow')
    return glow_box(content,T.GREEN,width=T.QUESTION_WIDTH,height=T.QUESTION_HEIGHT,
                    border=T.BOX_BORDER_COLOR,fill_opacity=T.QUESTION_FILL_OPACITY)


def serif(text, size=T.BODY, color=T.TEXT_PRIMARY, role='body'):
    minimum = T.MIN_BODY_SIZE if role == 'body' else T.MIN_LABEL_SIZE if role == 'label' else T.FOOTNOTE
    if size < minimum:
        raise ValueError(f'{role} text {size}pt is below its {minimum}pt minimum')
    return Tex(text, font_size=size, color=color, tex_template=T.tex_template())


def formula(text, size=T.MATH, color=T.TEXT_PRIMARY, role='math'):
    if size < (T.MIN_LABEL_SIZE if role == 'label' else T.BODY_SMALL):
        raise ValueError('Mathematical typography is below the minimum scale')
    return MathTex(text, font_size=size, color=color, tex_template=T.tex_template())


def paragraph(lines, size=T.BODY, leading=T.TEXT_LINE_SPACING,
              color=T.TEXT_PRIMARY, role='body'):
    """Explicit editorial line breaks; never shrink a line to disguise overflow."""
    objects = [serif(line, size, color, role=role) for line in lines]
    for index, obj in enumerate(objects):
        obj.move_to([0,-index*leading,0], aligned_edge=LEFT)
    return VGroup(*objects)


def fit_text_block(block, region=T.LEFT_TEXT_COLUMN):
    """Validate intended size. Reflow is required if it does not fit."""
    if block.width > region.width + .015 or block.height > region.height + .015:
        raise ValueError(f'Reflow text: {block.width:.2f} × {block.height:.2f} exceeds '
                         f'{region.width:.2f} × {region.height:.2f}; shrinking is disabled')
    return block


def place_text_column(block, top=None, region=T.LEFT_TEXT_COLUMN):
    fit_text_block(block, region)
    block.move_to([region.left,region.top if top is None else top,0],aligned_edge=UL)
    return block


def place_diagram_column(group, region=T.RIGHT_DIAGRAM_COLUMN):
    # Diagrams are laid out at the target scale; this is deliberately not a fit-to-box scaler.
    if group.width > region.width or group.height > region.height:
        raise ValueError('Diagram exceeds its composition region')
    return group.move_to(region.center)


def enforce_safe_gap(left, right, gap=T.COLUMN_GAP):
    actual=right.get_left()[0]-left.get_right()[0]
    if actual < gap-.01:
        raise ValueError(f'Column collision: gap {actual:.3f}, required {gap:.3f}')


def check_bounds(*objects, region=T.SAFE_ZONE):
    for obj in objects:
        if (obj.get_left()[0]<region.left-.02 or obj.get_right()[0]>region.right+.02
                or obj.get_bottom()[1]<region.bottom-.02 or obj.get_top()[1]>region.top+.02):
            raise ValueError(f'Outside safe region: {obj!r}')


def no_overlap(a,b,gap=.10):
    if not (a.get_right()[0]+gap<=b.get_left()[0] or
            b.get_right()[0]+gap<=a.get_left()[0] or
            a.get_top()[1]+gap<=b.get_bottom()[1] or
            b.get_top()[1]+gap<=a.get_bottom()[1]):
        raise ValueError('Unintended overlap between registered composition elements')


def soft_glow(mobject, color, radius=T.GLOW_RADIUS,
              layers=T.GLOW_LAYERS, opacity=T.GLOW_OPACITY):
    """Stroke convolution approximated by many broad, faint vector copies."""
    halo=VGroup()
    for t in np.linspace(1,.08,layers):
        halo.add(mobject.copy().set_fill(opacity=0).set_stroke(
            color,width=radius*110*t+1,opacity=opacity*(1-.45*t)))
    return halo


def point_halo(point,color,radius=T.POINT_GLOW_RADIUS):
    halo=VGroup()
    for t in np.linspace(1,.08,T.POINT_GLOW_LAYERS):
        halo.add(Circle(radius=radius*t,stroke_width=0,fill_color=color,
                        fill_opacity=T.POINT_HALO_BASE+T.POINT_HALO_PEAK*(1-t)**2).move_to(point))
    return halo


def glow_dot(point,color=T.BLUE,radius=T.POINT_RADIUS,active=True):
    point=np.array(point)
    halo=point_halo(point,color,radius=T.POINT_GLOW_RADIUS*radius/T.POINT_RADIUS)
    core=Circle(radius=radius,fill_color=color,fill_opacity=1,stroke_color=interpolate_color(
        ManimColor(color),ManimColor(T.TEXT_PRIMARY),.35),stroke_width=T.POINT_RIM_WIDTH).move_to(point)
    light=Circle(radius=radius*.50,stroke_width=0,fill_color=T.TEXT_PRIMARY,
                 fill_opacity=.12).move_to(point+UL*radius*.22)
    result=VGroup(halo,core,light)
    if not active:
        result.fade(1-T.HISTORY_OPACITY)
    result.core=core
    return result


def glow_line(start,end,color=T.BLUE,width=T.PRIMARY_STROKE):
    line=Line(start,end,color=color,stroke_width=width)
    return VGroup(soft_glow(line,color,radius=T.LINE_GLOW_RADIUS,opacity=T.LINE_GLOW_OPACITY),line)


def glow_arrow(start,end,color=T.BLUE,tip_length=T.ARROW_TIP_LENGTH):
    arrow=Arrow(start,end,buff=0,color=color,stroke_width=T.PRIMARY_STROKE,
                tip_length=tip_length,max_tip_length_to_length_ratio=.18)
    return VGroup(soft_glow(arrow,color,radius=T.ARROW_GLOW_RADIUS,opacity=T.ARROW_GLOW_OPACITY),arrow)


def dashed_path(points,color=T.BLUE,curve=True,width=T.PRIMARY_STROKE):
    path=VMobject().set_points_smoothly(points) if curve else VMobject().set_points_as_corners(points)
    path.set_stroke(color,width)
    count=max(8,int(path.get_arc_length()/T.DASH_LENGTH*T.DASH_RATIO))
    dashes=DashedVMobject(path,num_dashes=count,dashed_ratio=T.DASH_RATIO)
    return VGroup(soft_glow(dashes,color,radius=T.PATH_GLOW_RADIUS,layers=T.PATH_GLOW_LAYERS,opacity=T.PATH_GLOW_OPACITY),dashes)


def dashed_circle(center,radius,color=T.DASHED_LINE_COLOR,fill=.0):
    area=Circle(radius,fill_color=color,fill_opacity=fill,stroke_width=0).move_to(center)
    rim=DashedVMobject(Circle(radius,stroke_color=color,stroke_width=T.SECONDARY_STROKE),
        num_dashes=T.CIRCLE_DASH_COUNT,dashed_ratio=T.DASH_RATIO).move_to(center)
    return VGroup(area,rim)


def uncertainty_disk(center,radius,color=T.GREEN_SOFT):
    disk=dashed_circle(center,radius,color,fill=T.REGION_OPACITY)
    # A few softly layered interior shapes avoid a flat filled-disc appearance.
    glow=point_halo(center,color,radius=radius).fade(.85)
    return VGroup(disk[0],glow,disk[1])


def split_uncertainty_region(center,width,height,left_color=T.RED,right_color=T.BLUE):
    """One shared disk, shown schematically as an ellipse, with two semantic halves.

    It is a single report region, not two fictitious distance-only worlds.
    The caller must identify any enlarged schematic scale in its composition.
    """
    left=Sector(radius=1,start_angle=PI/2,angle=PI,
                stroke_width=0,fill_color=left_color,fill_opacity=T.REGION_OPACITY)
    right=Sector(radius=1,start_angle=-PI/2,angle=PI,
                 stroke_width=0,fill_color=right_color,fill_opacity=T.REGION_OPACITY)
    for half in (left,right):
        half.stretch(width/2,0,about_point=ORIGIN).stretch(height/2,1,about_point=ORIGIN)
        half.shift(center)
    rim=DashedVMobject(Ellipse(width=width,height=height,color=T.DASHED_LINE_COLOR,
        stroke_width=T.SECONDARY_STROKE),num_dashes=76,dashed_ratio=T.DASH_RATIO).move_to(center)
    return VGroup(left,right,rim)


def glow_box(content,color=T.GOLD,width=None,height=None,border=None,fill_opacity=T.BOX_FILL_OPACITY):
    outline=RoundedRectangle(width=width or content.width+2*T.BOX_PADDING_X,
        height=height or content.height+2*T.BOX_PADDING_Y,corner_radius=T.BOX_RADIUS,
        stroke_color=border or color,stroke_width=T.SECONDARY_STROKE,
        fill_color=color,fill_opacity=fill_opacity).move_to(content)
    halo=soft_glow(outline,border or color,radius=T.BOX_GLOW_RADIUS,layers=T.BOX_GLOW_LAYERS,opacity=T.BOX_GLOW_OPACITY)
    result=VGroup(halo,outline,content)
    result.content=content
    result.outline=outline
    return result


def glow_icon(name,point,color=T.GOLD,height=.82):
    asset=Path(__file__).resolve().parents[1]/'assets'/f'{name}.svg'
    icon=SVGMobject(str(asset)).set_height(height).move_to(point)
    icon.set_fill(color,opacity=T.ICON_FILL_OPACITY).set_stroke(color,width=T.SECONDARY_STROKE)
    return VGroup(soft_glow(icon,color,radius=T.ICON_GLOW_RADIUS,layers=T.ICON_GLOW_LAYERS,opacity=T.ICON_GLOW_OPACITY),icon)


def reference_background():
    bg=Rectangle(width=T.FRAME_WIDTH,height=T.FRAME_HEIGHT,stroke_width=0,
                 fill_color=T.BG,fill_opacity=1)
    glow=VGroup()
    for t in np.linspace(1,.08,48):
        glow.add(Ellipse(width=22*t+.4,height=13*t+.4,stroke_width=0,
                        fill_color=T.BG_LIFT,fill_opacity=.008).shift(UP*.4))
    return VGroup(bg,glow).set_z_index(-100)


def debug_regions():
    return VGroup(*[Rectangle(width=r.width,height=r.height,color=T.RED,stroke_width=.7,
                              fill_opacity=0).move_to(r.center)
                    for r in (T.SAFE_ZONE,T.LEFT_TEXT_COLUMN,T.RIGHT_DIAGRAM_COLUMN)])


class ReferenceStill(Scene):
    """Static-only design review surface. It never plays or writes a video."""
    def setup(self):
        self.camera.background_color=T.BG
        self.add(reference_background())

    def checked_add(self,*objects):
        check_bounds(*objects)
        self.add(*objects)
