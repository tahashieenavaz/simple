import re

_include_pattern = re.compile(r'@include\(\s*[\'"]?(.*?)[\'"]?\s*\)')
_variable_pattern = re.compile(r"\{\{\s*([\w-]+)\s*\}\}")
_property_pattern = re.compile(r'([\w-]+)=[\'"](.*?)[\'"]')
_component_pattern = re.compile(
    r"<x-([\w.-]+)\s*([^>]*?)(?:/>|>(.*?)</x-\1>)", re.DOTALL
)
