"""Reference-led 16:9 visual system. All distances are design-canvas units.

This is the replacement design API for new/revised scenes. Legacy episode
adapters remain intact until their compositions are separately migrated.
"""
from dataclasses import dataclass
from manim import TexTemplate

FRAME_WIDTH, FRAME_HEIGHT = 16.0, 9.0
RENDER_WIDTH, RENDER_HEIGHT = 1920, 1080
BG = '#0D131D'
BG_LIFT = '#182331'
TEXT_PRIMARY = '#E6ECF7'
TEXT_SECONDARY = '#BBC5DB'
TEXT_MUTED = '#8995AC'
BLUE = '#79C7FF'
BLUE_SOFT = '#B0D4FA'
BLUE_GLOW = '#389EF2'
GOLD = '#FFD46E'
GOLD_SOFT = '#FFE5A0'
GOLD_GLOW = '#D79B32'
GREEN = '#66E2BD'
GREEN_SOFT = '#BCE7B3'
GREEN_GLOW = '#329F80'
RED = '#F48CA7'
RED_SOFT = '#F8B1C3'
AXIS_COLOR = '#9AAAC2'
DASHED_LINE_COLOR = '#89A8D0'
AUXILIARY_LINE_COLOR = '#60728C'
BOX_BORDER_COLOR = '#3D5574'

TITLE_SIZE = 64
SUBTITLE_SIZE = 42
BODY_LARGE = 46
BODY = 43
BODY_SMALL = 36
MATH_LARGE = 60
MATH = 54
LABEL = 44
FOOTNOTE = 27
MIN_BODY_SIZE = BODY_SMALL
MIN_LABEL_SIZE = 38
SERIF_FAMILY = 'Latin Modern Roman'

SAFE_MARGIN_X = .95
SAFE_MARGIN_Y = .38
COLUMN_GAP = .58
TEXT_LINE_SPACING = .57
BLOCK_SPACING = .31
TITLE_TO_BODY_SPACING = .67
TITLE_Y = 3.82
BODY_TOP = 2.88
QUESTION_Y = -3.62
QUESTION_HEIGHT = .94
QUESTION_WIDTH = 10.6
BOX_PADDING_X = .34
BOX_PADDING_Y = .20
BOX_RADIUS = .19

PRIMARY_STROKE = 2.35
SECONDARY_STROKE = 1.55
AUXILIARY_STROKE = 1.15
DASH_LENGTH = .095
DASH_RATIO = .49
CIRCLE_DASH_COUNT = 44
POINT_RADIUS = .135
POINT_GLOW_RADIUS = .48
POINT_GLOW_LAYERS = 36
GLOW_LAYERS = 12
GLOW_RADIUS = .10
GLOW_OPACITY = .022
REGION_OPACITY = .09
ACTIVE_OPACITY = 1.0
SECONDARY_OPACITY = .64
HISTORY_OPACITY = .32
CONSTRUCTION_OPACITY = .28


@dataclass(frozen=True)
class Region:
    left: float
    right: float
    bottom: float
    top: float

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.top - self.bottom

    @property
    def center(self):
        return ((self.left+self.right)/2, (self.bottom+self.top)/2, 0)


SAFE_ZONE = Region(-7.05, 7.05, -4.12, 4.12)
LEFT_TEXT_COLUMN = Region(-7.05, .15, -2.79, BODY_TOP)
RIGHT_DIAGRAM_COLUMN = Region(.73, 7.05, -2.79, 2.99)


def tex_template():
    template = TexTemplate()
    template.add_to_preamble(r'\usepackage[T1]{fontenc}')
    template.add_to_preamble(r'\usepackage{lmodern}')
    template.add_to_preamble(r'\usepackage{xcolor}')
    template.add_to_preamble(r'\usepackage{amsmath,amssymb}')
    return template

# Frozen component internals. Change only with canonical calibration review.
STYLE_VERSION = '1.0-approved'
LINE_GLOW_RADIUS, LINE_GLOW_OPACITY = .08, .017
ARROW_GLOW_RADIUS, ARROW_GLOW_OPACITY = .075, .012
ARROW_TIP_LENGTH = .15
PATH_GLOW_RADIUS, PATH_GLOW_LAYERS, PATH_GLOW_OPACITY = .045, 6, .010
BOX_GLOW_RADIUS, BOX_GLOW_LAYERS, BOX_GLOW_OPACITY = .15, 18, .013
BOX_FILL_OPACITY = .025
QUESTION_FILL_OPACITY = .012
ICON_GLOW_RADIUS, ICON_GLOW_LAYERS, ICON_GLOW_OPACITY = .14, 16, .025
ICON_FILL_OPACITY = .13
POINT_RIM_WIDTH = 1.6
POINT_HALO_BASE, POINT_HALO_PEAK = .008, .021
