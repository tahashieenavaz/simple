from simple import TemplateEngine
from pathlib import Path


def test_files_could_be_included():
    root_path = Path(__file__).resolve().parent
    templates_path = root_path / "templates"
    engine = TemplateEngine(templates_path)
    rendered = engine.render("index.html")
    assert "This part comes from extra.html." in rendered


def test_multiple_files_could_be_included():
    root_path = Path(__file__).resolve().parent
    templates_path = root_path / "templates"
    engine = TemplateEngine(templates_path)
    rendered = engine.render("index-multiple.html")

    assert "this is coming from part-1.html file" in rendered
    assert "this is coming from part-2.html file" in rendered
