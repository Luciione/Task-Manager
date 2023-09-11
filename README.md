# TASK MANAGER CLI FOR GROCERY LIST, NOTES AND REMINDERS

This is a command-line interface (CLI) application for managing grocery lists, notes, and reminders using SQLAlchemy and SQLite as the database backend. You can add, list, update, and delete grocery items, notes, and reminders with this application.

# Table of Contents
Installation
Usage
Commands for Grocery List
Commands for Notes
Commands for Reminders
Contributing
License

# Installation

Clone the repository to your local machine:

git clone git@github.com:Luciione/Task-Manager.git

Navigate to the project directory:

cd TM

Install the required dependencies using pip:

pip install -r requirements.txt

Initialize the SQLite database:

python init_db.py

Now, the application is ready to use.

Usage
To use the CLI, run the following command from the project directory:

python cli.py [COMMAND]

Replace [COMMAND] with one of the available commands described below.

Commands for Grocery List

Add a Grocery Item:

python cli.py add_grocery
You will be prompted to enter the item name and quantity.

List Grocery Items:

python cli.py list_grocery
Update a Grocery Item:

python cli.py update_grocery
You will be prompted to enter the item name and the new quantity.

Delete a Grocery Item:

python cli.py delete_grocery
You will be prompted to enter the item name to delete.

Commands for Notes
Add a Note:

python cli.py add_note
You will be prompted to enter the note content.

List Notes:

python cli.py list_notes
Update a Note:

python cli.py update_note
You will be prompted to enter the note content and the new content.

Delete a Note:

python cli.py delete_note
You will be prompted to enter the note content to delete.

Commands for Reminders
Add a Reminder:

python cli.py add_reminder
You will be prompted to enter the reminder title, description, and due date in the format "YYYY-MM-DD HH:MM:SS".

List Reminders:

python cli.py list_reminders
Update a Reminder:

python cli.py update_reminder
You will be prompted to enter the reminder title and provide new information for title, description, and due date.

Delete a Reminder:

python cli.py delete_reminder
You will be prompted to enter the reminder title to delete.

# Contributing

If you'd like to contribute to this project, please follow these steps:

Fork the repository on GitHub.

Create a new branch with your changes: git checkout -b feature/your-feature-name.

Make your changes and commit them: git commit -m "Add your feature".

Push your changes to your fork: git push origin feature/your-feature-name.

Create a pull request to the main repository.

# License

This project is licensed under the MIT License - see the LICENSE file for details.




