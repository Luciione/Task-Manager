"""Initial migration

Revision ID: c00bbc465775
Revises: 5ea401f648f0
Create Date: 2023-09-10 15:23:06.271776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c00bbc465775'
down_revision = '5ea401f648f0'
branch_labels = None
depends_on = None


def upgrade():
     op.create_table(
        'grocery_lists',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('item', sa.String(), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
     op.create_table(
        'notes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('content', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
     op.create_table(
        'reminders',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('due_date', sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('grocery_lists')
    op.drop_table('notes')
    op.drop_table('reminders')