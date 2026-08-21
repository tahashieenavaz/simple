from pathlib import Path
from simple.patterns import (
    _variable_pattern,
    _include_pattern,
    _property_pattern,
    _component_pattern,
)


class TemplateEngine:
    def __init__(self, root_directory: str):
        self.root_directory = Path(root_directory).resolve()
        self.load_patterns()

    def load_patterns(self):
        self.variable_pattern = _variable_pattern
        self.include_pattern = _include_pattern
        self.property_pattern = _property_pattern
        self.component_pattern = _component_pattern

    def render(
        self,
        template_name: str,
        context_data: dict = None,
        visited_paths: frozenset = None,
    ) -> str:
        context_data = context_data or {}
        visited_paths = visited_paths or frozenset()

        absolute_path = (self.root_directory / template_name).resolve()

        if (
            not absolute_path.is_relative_to(self.root_directory)
            or not absolute_path.is_file()
        ):
            raise ValueError(f"Invalid or missing template: {template_name}")

        if absolute_path in visited_paths:
            raise RecursionError(f"Infinite include cycle detected at: {template_name}")

        template_content = absolute_path.read_text(encoding="utf-8")
        updated_visited_paths = visited_paths | {absolute_path}

        def inject_variable(match) -> str:
            variable_name = match.group(1)
            return str(context_data.get(variable_name, ""))

        def process_include(match) -> str:
            included_filename = match.group(1)
            return self.render(included_filename, context_data, updated_visited_paths)

        def process_component(match) -> str:
            component_name = match.group(1)
            properties_string = match.group(2)
            slot_content = match.group(3)

            component_props = dict(self.property_pattern.findall(properties_string))
            component_props["slot"] = (slot_content or "").strip()

            component_filename = f"components/{component_name}.html"
            return self.render(
                component_filename, component_props, updated_visited_paths
            )

        template_content = self.variable_pattern.sub(inject_variable, template_content)
        template_content = self.include_pattern.sub(process_include, template_content)
        template_content = self.component_pattern.sub(
            process_component, template_content
        )

        return template_content
