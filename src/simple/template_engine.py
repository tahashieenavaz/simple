import re
from typing import Optional
from pathlib import Path
from simple.mixins import PatternsMixin


class TemplateEngine(PatternsMixin):
    def __init__(self, root: str = "."):
        super().__init__()
        self.root = Path(root).resolve()

    def render(self, filename: str, _visited_files: Optional[set] = None):
        if _visited_files is None:
            _visited_files = set()

        target_path = (self.root / filename).resolve()

        if not target_path.is_relative_to(self.root):
            raise PermissionError(
                f"Access denied: {filename} is outside template root."
            )

        if not target_path.is_file():
            raise FileNotFoundError(f"Template not found: {filename}")

        if target_path in _visited_files:
            raise RecursionError(f"Infinite inclusion loop detected: {filename}")

        _visited_files.add(target_path)
        content = target_path.read_text(encoding="utf-8")

        def _match_resolver(match) -> str:
            included_filename = match.group(1)
            return self.render(included_filename, _visited_files.copy())

        return self.include_pattern.sub(_match_resolver, content)
