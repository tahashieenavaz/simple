from simple import TemplateEngine


def test_files_could_be_included():
    engine = TemplateEngine("templates")
    rendered = engine.render("index.html")
    assert "extra.html" in rendered
