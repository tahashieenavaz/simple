import re
from .patterns_base_mixin import PatternsBaseMixin


class IncludePatternMixin(PatternsBaseMixin):
    def __init__(self):
        super().__init__()
        self.include_pattern = re.compile(r'@include\(\s*[\'"]?(.*?)[\'"]?\s*\)')
