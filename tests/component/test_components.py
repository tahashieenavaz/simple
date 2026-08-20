from pathlib import Path
from simple import TemplateEngine


def test_components_can_render():
    root_path = Path(__file__).resolve().parent
    templates_path = root_path / "templates"
    engine = TemplateEngine(templates_path)
    rendered = engine.render("index.html")

    assert "This part is a part of layout component." in rendered
