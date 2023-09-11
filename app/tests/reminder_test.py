from app.cli import add_reminder
def test_add_reminder(runner):
    result = runner.invoke(
        add_reminder,
        ["--title", "Meeting", "--description", "Team meeting", "--due_date", "2023-12-31 14:00:00"],
    )
    assert result.exit_code == 0
    assert "Reminder added successfully." in result.output
