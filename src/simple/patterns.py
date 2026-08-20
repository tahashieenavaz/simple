import re

_include_pattern = re.compile(r'@include\(\s*["\']?(.*?)["\']?\s*\)')
_variable_pattern = re.compile(r"\{\{\s*([\w-]+)\s*\}\}")
