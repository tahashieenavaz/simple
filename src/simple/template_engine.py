import re
from typing import Optional
from pathlib import Path, PosixPath
from simple.mixins import PatternsMixin


class TemplateEngine(PatternsMixin):
    def __init__(self, root: str = "."):
        super().__init__()
        self.root = Path(root).resolve()

    def check_target_path_relativity(self, *, path: PosixPath, filename: str):
        if path.is_relative_to(self.root):
            return

        raise PermissionError(f"Access denied: {filename} is outside template root.")

    def check_target_existence(self, *, path: PosixPath, filename: str):
        if path.is_file():
            return

        raise FileNotFoundError(f"Template not found: {filename}")

    def check_visited_path_infinite_loop(
        self, *, filename: str, path: PosixPath, visited_paths: set
    ):
        if path not in visited_paths:
            return

        raise RecursionError(f"Infinite inclusion loop detected: {filename}")

    def render(
        self,
        filename: str,
        _visited_paths: Optional[set] = None,
        _context: Optional[dict] = {},
    ):
        if _visited_paths is None:
            _visited_paths = set()

        if _context is None:
            _context = set()

        target_path = (self.root / filename).resolve()

        self.check_target_path_relativity(path=target_path, filename=filename)
        self.check_target_existence(path=target_path, filename=filename)
        self.check_visited_path_infinite_loop(
            path=target_path, filename=filename, visited_paths=_visited_paths.copy()
        )

        _visited_paths.add(target_path)
        content = target_path.read_text(encoding="utf-8")

        def _match_resolver(match) -> str:
            included_filename = match.group(1)
            return self.render(included_filename, _visited_paths.copy())

        return self.include_pattern.sub(_match_resolver, content)
