from app.cli import add_note
def test_add_note(runner):
    result = runner.invoke(add_note, ["--content", "Important Note"])
    assert result.exit_code == 0
    assert "Note added successfully." in result.output

    
