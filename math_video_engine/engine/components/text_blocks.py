import textwrap
from manim import Text, VGroup, RoundedRectangle
from engine import theme


def fit(mob, width, height=None):
    if mob.width > width:
        mob.scale_to_fit_width(width)
    if height and mob.height > height:
        mob.scale_to_fit_height(height)
    return mob


class CaptionBlock(Text):
    def __init__(self, text, **kwargs):
        lines = text.split("\n") if "\n" in text else textwrap.wrap(text, 78)
        if len(lines) > 3:
            raise ValueError("Split narration into shorter captions (maximum 3 lines).")
        super().__init__("\n".join(lines), font=theme.FONT,
                         font_size=theme.CAPTION_SIZE, color=theme.MUTED_TEXT,
                         line_spacing=0.8, **kwargs)
        fit(self, theme.CAPTION_WIDTH, 1.0)
        self.move_to([0, -2.95, 0])


class ResultBox(VGroup):
    def __init__(self, content, color=theme.SUCCESS):
        super().__init__()
        fit(content, theme.BODY_WIDTH - 0.8, theme.BODY_HEIGHT - 0.8)
        box = RoundedRectangle(width=content.width + 0.7,
                               height=content.height + 0.6,
                               corner_radius=0.16, color=color,
                               fill_color=color, fill_opacity=0.055)
        content.move_to(box)
        self.add(box, content)
