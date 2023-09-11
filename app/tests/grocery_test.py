#Testing grocery item:
import pytest
from click.testing import CliRunner
from models import add_grocery, list_grocery, update_grocery, delete_grocery

@pytest.fixture
def runner():
    return CliRunner()

def test_add_grocery(runner):
    result = runner.invoke(add_grocery, ["--item", "Apples", "--quantity", "5"])
    assert result.exit_code == 0
    assert "Item added to the grocery list successfully." in result.output

@pytest.fixture
def runner():
    return CliRunner()

def test_list_grocery_empty(runner):
    result = runner.invoke(list_grocery)
    assert result.exit_code == 0
    assert "Grocery list is empty." in result.output

def test_update_grocery(runner):
    # First, add a grocery item
    result_add = runner.invoke(add_grocery, ["--item", "    Onions", "--quantity", "2"])
    assert result_add.exit_code == 0

    # Now, update the item
    result_update = runner.invoke(update_grocery, ["--item", "Onions", "--quantity", "3"])
    assert result_update.exit_code == 0
    assert "Item updated successfully: Milk" in result_update.output

def test_update_grocery_not_found(runner):
    result = runner.invoke(update_grocery, ["--item", "NonexistentItem", "--quantity", "3"])
    assert result.exit_code == 0
    assert 'Item "NonexistentItem" not found in the grocery list.' in result.output

def test_delete_grocery(runner):
    # First, add a grocery item
    result_add = runner.invoke(add_grocery, ["--item", "Oranges", "--quantity", "1"])
    assert result_add.exit_code == 0

    # Now, delete the item
    result_delete = runner.invoke(delete_grocery, ["--item", "Oranges"])
    assert result_delete.exit_code == 0
    assert "Item deleted successfully: Eggs" in result_delete.output

def test_delete_grocery_not_found(runner):
    result = runner.invoke(delete_grocery, ["--item", "NonexistentItem"])
    assert result.exit_code == 0
    assert 'Item "NonexistentItem" not found in the grocery list.' in result.output


