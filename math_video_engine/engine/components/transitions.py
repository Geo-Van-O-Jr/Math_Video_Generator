from manim import FadeOut, FadeIn, AnimationGroup
from engine import theme


def crossfade(old, new):
    return AnimationGroup(FadeOut(old), FadeIn(new),
                          run_time=theme.TRANSITION_TIME)
