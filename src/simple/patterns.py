import re

include_pattern = re.compile(r'@include\(\s*["\']?(.*?)["\']?\s*\)')
variable_pattern = re.compile(r"\{\{\s*([\w-]+)\s*\}\}")
