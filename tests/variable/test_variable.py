from pathlib import Path
from simple import TemplateEngine


def test_single_variables_are_rendered():
    root_path = Path(__file__).resolve().parent
    templates_path = root_path / "templates"
    engine = TemplateEngine(templates_path)
    rendered = engine.render("index.html", {"name": "John Doe"})
    assert "Name: John Doe" in rendered
