# -*- coding: utf-8 -*-
"""mistune

Custom plugins for mistune.

Author: AlanDecode | 熊猫小A
Link:   https://www.imalan.cn
GitHub: https://github.com/AlanDecode
"""

from .image import ImageRenderer
from .blockcode import HighlightRenderer
from .paragraph import ParagraphRenderer


class MyRenderer(ImageRenderer, HighlightRenderer, ParagraphRenderer):

  def __init__(self, escape=True, md_path='', g_hooks=None):
    super(MyRenderer, self).__init__(escape=escape)
    self.md_path = md_path
    self.g_hooks = g_hooks
