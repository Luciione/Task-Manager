# cli.py
from grocery_list import GroceryList
from note import Note
from reminder import Reminder 
import click
import datetime
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from database import engine

Session = sessionmaker(bind=engine)

@click.group()
def cli():
    pass

# Define a validation function for quantity
def validate_quantity(ctx, param, value):
     if value is None or value <= 0:
        raise click.BadParameter('Quantity must be a positive integer.')
     return value
  # Commands for Grocery List  
@cli.command()
@click.option('-i', '--item', prompt='Item name', help='Item name', required=True)
@click.option('-q', '--quantity', type=int, prompt='Quantity', help='Item quantity', callback=validate_quantity)
def add_grocery(item, quantity):
    """Add an item to the grocery list"""
    session = Session()
    grocery_item = GroceryList(item=item, quantity=quantity)
    session.add(grocery_item)
    session.commit()
    session.close()
    click.echo('Item added to the grocery list successfully.')



@cli.command()
def list_grocery():
    """List all items in the grocery list"""
    session = Session()
    items = session.query(GroceryList).all()
    session.close()
    if not items:
        click.echo('Grocery list is empty.')
    else:
        click.echo('Grocery List:')
        for item in items:
            click.echo(f'Item: {item.item}, Quantity: {item.quantity}')

@cli.command()
@click.option('-i', '--item', prompt='Item name', help='Item name', required=True)
@click.option('-q', '--quantity', type=int, prompt='Quantity', help='Item quantity')
def update_grocery(item, quantity):
    """Update an item in the grocery list"""
    with Session() as session:
         grocery_item = session.query(GroceryList).filter(GroceryList.item == item).first()

    if not grocery_item:
        click.echo(f'Item "{item}" not found in the grocery list.')
        return

    grocery_item.quantity = quantity
    session.commit()
    click.echo(f'Item updated successfully: {grocery_item.item}')

@cli.command()
@click.option('-i', '--item', prompt='Item name', help='Item name', required=True)
def delete_grocery(item):
    """Delete an item from the grocery list by name"""
    session = Session()
    grocery_item = session.query(GroceryList).filter(GroceryList.item == item).first()

    if not grocery_item:
        session.close()
        click.echo(f'Item "{item}" not found in the grocery list.')
        return

    session.delete(grocery_item)
    session.commit()
    session.close()
    click.echo(f'Item deleted successfully: {grocery_item.item}')

# Commands for Notes
@cli.command()
@click.option('-c', '--content', prompt='Note content', help='Note content', required=True)
def add_note(content):
    """Add a note"""
    session = Session()
    note = Note(content=content)
    session.add(note)
    session.commit()
    session.close()
    click.echo('Note added successfully.')

@cli.command()
def list_notes():
    """List all notes"""
    session = Session()
    notes = session.query(Note).all()
    session.close()
    if not notes:
        click.echo('No notes found.')
    else:
        click.echo('Notes:')
        for note in notes:
            click.echo(f'Note #{note.id}: {note.content}')

@cli.command()
@click.option('-c', '--content', prompt='Note content', help='Note content', required=True)
def update_note(content):
    """Update a note"""
    with Session() as session:
      note = session.query(Note).filter(Note.content == content).first()

    if not note:
        click.echo(f'Note with content "{content}" not found.')
        return

    new_content = click.prompt('New note content', default=note.content)
    note.content = new_content
    session.commit()
    click.echo(f'Note updated successfully: {note.content}')

@cli.command()
@click.option('-c', '--content', prompt='Note content', help='Note content', required=True)
def delete_note(content):
    """Delete a note by content"""
    session = Session()
    note = session.query(Note).filter(Note.content == content).first()

    if not note:
        session.close()
        click.echo(f'Note with content "{content}" not found.')
        return

    session.delete(note)
    session.commit()
    session.close()
    click.echo(f'Note deleted successfully: {note.content}')

# Commands for Reminders
@cli.command()
@click.option('-t', '--title', prompt='Reminder title', help='Reminder title', required=True)
@click.option('-d', '--description', prompt='Reminder description', help='Reminder description')
@click.option('-due', '--due_date', prompt='Due date (YYYY-MM-DD HH:MM:SS)', help='Due date')
def add_reminder(title, description, due_date):
    """Add a reminder"""
    try:
        due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        click.echo('Invalid date format. Please use the format "YYYY-MM-DD HH:MM:SS"')
        return

    with Session() as session:
     reminder = Reminder(title=title, description=description, due_date=due_date)
    session.add(reminder)
    session.commit()
    click.echo('Reminder added successfully.')

    def validate_date(ctx, param, value):
     try:
        return datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
     except ValueError:
        raise click.BadParameter('Invalid date format. Please use the format "YYYY-MM-DD HH:MM:SS".')


@cli.command()
def list_reminders():
    """List all reminders"""
    session = Session()
    reminders = session.query(Reminder).all()
    session.close()
    if not reminders:
        click.echo('No reminders found.')
    else:
        click.echo('Reminders:')
        for reminder in reminders:
            click.echo(f'Reminder #{reminder.id}: {reminder.title}, Due Date: {reminder.due_date}')

@cli.command()
@click.option('-t', '--title', prompt='Reminder title', help='Reminder title', required=True)
def update_reminder(title):
    """Update a reminder"""
    session = Session()
    reminder = session.query(Reminder).filter(Reminder.title == title).first()

    if not reminder:
        session.close()
        click.echo(f'Reminder with title "{title}" not found.')
        return

    new_title = click.prompt('New reminder title', default=reminder.title)
    new_description = click.prompt('New reminder description', default=reminder.description)
    new_due_date = click.prompt('New due date (YYYY-MM-DD HH:MM:SS)', default=reminder.due_date)

    try:
        new_due_date = datetime.strptime(new_due_date, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        click.echo('Invalid date format. Please use the format "YYYY-MM-DD HH:MM:SS"')
        session.close()
        return

    reminder.title = new_title
    reminder.description = new_description
    reminder.due_date = new_due_date
    session.commit()

    # Reload the reminder after the commit to avoid DetachedInstanceError
    reminder = session.query(Reminder).filter(Reminder.title == new_title).first()

    session.close()
    click.echo(f'Reminder updated successfully: {reminder.title}')


@cli.command()
@click.option('-t', '--title', prompt='Reminder title', help='Reminder title', required=True)
def delete_reminder(title):
    """Delete a reminder by title"""
    session = Session()
    reminder = session.query(Reminder).filter(Reminder.title == title).first()

    if not reminder:
        session.close()
        click.echo(f'Reminder with title "{title}" not found.')
        return

    session.delete(reminder)
    session.commit()
    session.close()
    click.echo(f'Reminder deleted successfully: {reminder.title}')

if __name__ == '__main__':
    cli()
