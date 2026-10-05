"""A persistent mathematical board, without presentation chrome.

These components are opt-in: existing episodes retain their original theme.
Positions are scene coordinates; mathematical-to-screen maps belong to episodes.
"""
import json
from pathlib import Path
import numpy as np
from manim import *

NAVY = "#10151E"
IVORY = "#E9ECF5"
MUTED = "#A6B0C6"
BLUE = "#73BFFF"
GOLD = "#F5CE69"
GREEN = "#ABE095"
PINK = "#F28DA5"
MINT = "#65DEBB"
ASSETS = Path(__file__).resolve().parents[1] / "assets"


def prose(text, size=32, color=IVORY, width=None):
    obj = Tex(text, font_size=size, color=color)
    if width and obj.width > width:
        obj.scale_to_fit_width(width)
    return obj


def math(text, size=38, color=IVORY, width=None):
    obj = MathTex(text, font_size=size, color=color)
    if width and obj.width > width:
        obj.scale_to_fit_width(width)
    return obj


class PersistentCanvas(Scene):
    """Named objects, semantic cues and bounds checking; no automatic clearing."""
    def setup(self):
        self.camera.background_color = NAVY
        self.objects = {}
        self.cues = []

    def remember(self, key, obj):
        self.objects[key] = obj
        return obj

    def reveal(self, obj, seconds=1.5):
        self.play(Write(obj), run_time=seconds)
        return obj

    def cue(self, name, hold=2):
        self.check_bounds()
        self.cues.append({"time": float(self.time + hold / 2), "caption": name})
        self.wait(hold)

    def check_bounds(self):
        for obj in self.mobjects:
            if not obj.has_points() and not obj.submobjects:
                continue
            if (obj.get_left()[0] < -config.frame_width / 2 + .08 or
                    obj.get_right()[0] > config.frame_width / 2 - .08 or
                    obj.get_top()[1] > config.frame_height / 2 - .08 or
                    obj.get_bottom()[1] < -config.frame_height / 2 + .08):
                raise ValueError(f"Object outside canvas: {obj!r}")

    def dim_others(self, keep, opacity=.22):
        return [obj.animate.set_opacity(opacity) for obj in self.mobjects
                if obj not in keep]

    def tear_down(self):
        dest = Path(config.media_dir) / "cues"
        dest.mkdir(parents=True, exist_ok=True)
        (dest / f"{type(self).__name__}.json").write_text(
            json.dumps(self.cues, indent=2), encoding="utf-8")
        super().tear_down()


class ProofWriter:
    """Progressive prose and algebra, with explicit positions and retained facts."""
    def __init__(self, scene, anchor=ORIGIN, width=12):
        self.scene, self.anchor, self.width = scene, np.array(anchor), width
        self.last = None

    def write(self, text, pos=None, size=32, color=IVORY, run_time=2):
        obj = prose(text, size, color, self.width).move_to(
            self.anchor if pos is None else pos)
        self.scene.play(Write(obj), run_time=run_time)
        return obj

    def write_lines(self, lines, pos=None, size=30, gap=.18, run_time=1.7):
        block = VGroup(*[prose(line, size, width=self.width) for line in lines])
        block.arrange(DOWN, aligned_edge=LEFT, buff=gap).move_to(
            self.anchor if pos is None else pos)
        for line in block:
            self.scene.play(Write(line), run_time=run_time)
        # Consolidate to make subsequent lifetime management predictable.
        self.scene.remove(*block)
        self.scene.add(block)
        return block

    def write_math(self, text, pos=None, size=38, color=IVORY, run_time=2):
        obj = math(text, size, color, self.width).move_to(
            self.anchor if pos is None else pos)
        self.scene.play(Write(obj), run_time=run_time)
        self.last = obj
        return obj

    next_math = write_math

    def transform_last(self, text, pos=None, size=38, color=IVORY, run_time=2):
        if self.last is None:
            return self.write_math(text, pos, size, color, run_time)
        target = math(text, size, color, self.width).move_to(
            self.last if pos is None else pos)
        self.scene.play(TransformMatchingTex(self.last, target), run_time=run_time)
        self.last = target
        return target

    def pin_fact(self, obj, pos, scale=.72):
        self.scene.play(obj.animate.scale(scale).move_to(pos).set_color(MUTED),
                        run_time=1.3)
        return obj

    def fade_secondary(self, *objects):
        self.scene.play(*[obj.animate.set_opacity(.25) for obj in objects])


class TrackedPoint(VGroup):
    def __init__(self, point, label=None, color=BLUE, direction=DOWN, icon=None):
        super().__init__()
        self.marker = (SVGMobject(str(ASSETS / f"{icon}.svg"), color=color,
                                fill_opacity=.75, stroke_width=1.3).set_height(.55)
                       if icon else Dot(radius=.075, color=color))
        self.marker.set_color(color)
        self.marker.move_to(point)
        # Wide low-opacity strokes produce a restrained vector halo.
        self.halo = self.marker.copy().set_fill(opacity=.04).set_stroke(color, 8, .055)
        self.add(self.halo, self.marker)
        if label:
            self.label = math(label, 29, color).next_to(self.marker, direction, buff=.15)
            self.add(self.label)

    def location(self):
        return self.marker.get_center()


class MovingPoint(TrackedPoint):
    def move_marker_to(self, point):
        """Animation moving the marker, glow and label by the same displacement."""
        return self.animate.shift(np.asarray(point) - self.location())


class UncertaintyDisk(VGroup):
    def __init__(self, center, radius=1, color=GREEN):
        super().__init__()
        fill = Circle(radius, stroke_width=0, fill_color=color, fill_opacity=.075)
        rim = DashedVMobject(Circle(radius, color=color, stroke_width=1.5),
                            num_dashes=64, dashed_ratio=.47)
        self.add(fill, rim).move_to(center)


class DashedTrajectory(DashedLine):
    def __init__(self, start, end, color=BLUE, **kwargs):
        super().__init__(start, end, color=color, stroke_width=2,
                         dash_length=.10, dashed_ratio=.52, **kwargs)


class DistanceAnnotation(VGroup):
    def __init__(self, start, end, text, direction=UP, color=IVORY, buff=.14):
        line = Line(start, end, color=color, stroke_width=1.35)
        label = math(text, 27, color).next_to(line, direction, buff=buff)
        super().__init__(line, label)
        self.line, self.label = line, label


class SymmetricChoices(VGroup):
    """Explicit reflection about a horizontal line, with a shared start."""
    def __init__(self, start, upper, axis_y, colors=(PINK, BLUE)):
        lower = np.array(upper, dtype=float)
        lower[1] = 2 * axis_y - upper[1]
        self.upper, self.lower = np.array(upper), lower
        self.routes = VGroup(DashedTrajectory(start, upper, colors[0]),
                             DashedTrajectory(start, lower, colors[1]))
        self.ends = VGroup(TrackedPoint(upper, "Y_1", colors[0], UP),
                           TrackedPoint(lower, "Y_2", colors[1], DOWN))
        super().__init__(self.routes, self.ends)


class ResultHighlight(VGroup):
    def __init__(self, content, color=GOLD, padding=.23):
        outline = SurroundingRectangle(content, buff=padding, corner_radius=.12,
                                       color=color, stroke_width=1.4,
                                       fill_color=color, fill_opacity=.035)
        glow = outline.copy().set_stroke(color, width=9, opacity=.055)
        super().__init__(glow, outline, content)


class PersistentFact(ResultHighlight):
    """A compact equation retained while the next part is constructed."""
    pass


class EquationDerivation(ProofWriter):
    """Semantic alias for a writer used as a single transforming equation."""
    pass
