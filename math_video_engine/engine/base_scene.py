import json
import os
from pathlib import Path
from manim import Scene, Text, Line, FadeIn, FadeOut, Write, TransformMatchingTex, VGroup, config
from engine import theme
from engine.components import CaptionBlock, EquationStep, ResultBox
from engine.components.transitions import crossfade
from engine.components.text_blocks import fit


class MathScene(Scene):
    """Independent scene with caption lifecycle and checked presentation regions."""
    def setup(self):
        self.camera.background_color = theme.BACKGROUND
        self.caption = None
        self.body = None
        self.cues = []

    def heading(self, title, number):
        text = Text(title, font=theme.FONT, font_size=theme.TITLE_SIZE,
                    color=theme.TEXT)
        fit(text, 10.0)
        text.move_to([-0.5, 3.25, 0])
        total = os.environ.get("MATH_VIDEO_SCENE_COUNT")
        label = f"{number:02d}" + (f" / {int(total):02d}" if total else "")
        badge = Text(label, font=theme.FONT, font_size=16,
                     color=theme.MUTED_TEXT).move_to([5.8, 3.25, 0])
        rule = Line([-6, 2.8, 0], [6, 2.8, 0], color=theme.MUTED_TEXT,
                    stroke_opacity=0.3)
        self.play(FadeIn(text), FadeIn(badge), Write(rule), run_time=1)

    def show_caption(self, text):
        new = CaptionBlock(text)
        if self.caption is None:
            self.play(FadeIn(new), run_time=0.7)
        else:
            self.play(crossfade(self.caption, new))
        self.caption = new

    replace_caption = show_caption

    def clear_caption(self):
        if self.caption is not None:
            self.play(FadeOut(self.caption), run_time=0.6)
            self.caption = None

    def present(self, mob, caption=None, hold=6, transform=False):
        if caption:
            self.show_caption(caption)
        if self.body is None:
            self.play(Write(mob), run_time=1.5)
        elif transform and isinstance(self.body, EquationStep) and isinstance(mob, EquationStep):
            self.play(TransformMatchingTex(self.body, mob), run_time=1.4)
        else:
            self.play(crossfade(self.body, mob))
        self.body = mob
        self.read(hold)

    def equation(self, *lines, caption=None, hold=6, color=theme.PRIMARY_MATH):
        self.present(EquationStep(*lines, color=color), caption, hold, transform=True)

    def result(self, *lines, caption=None, hold=7):
        box = ResultBox(EquationStep(*lines))
        box.move_to([0, 0.25, 0])
        self.present(box, caption, hold)

    def read(self, seconds=6):
        self.check_layout()
        self.cues.append({"time": float(self.time + seconds / 2),
                          "caption": self.caption.text if self.caption else ""})
        self.wait(seconds)

    def check_layout(self):
        for mob in (self.body, self.caption):
            if mob is None:
                continue
            if (mob.get_left()[0] < -config.frame_width / 2 + 0.2 or
                mob.get_right()[0] > config.frame_width / 2 - 0.2 or
                mob.get_top()[1] > config.frame_height / 2 - 0.2 or
                mob.get_bottom()[1] < -config.frame_height / 2 + 0.2):
                raise ValueError(f"Presentation outside frame in {type(self).__name__}")
        if self.body is not None and self.caption is not None:
            if self.body.get_bottom()[1] < self.caption.get_top()[1] + 0.2:
                raise ValueError("Equation/caption overlap")

    def finish(self):
        self.play(*[FadeOut(mob) for mob in list(self.mobjects)], run_time=1.2)

    def tear_down(self):
        destination = Path(config.media_dir) / "cues"
        destination.mkdir(parents=True, exist_ok=True)
        (destination / f"{type(self).__name__}.json").write_text(
            json.dumps(self.cues, indent=2), encoding="utf-8")
        super().tear_down()
