"""ensure_admin_user

Revision ID: 5da41f08259d
Revises: 17d6d190084e
Create Date: 2023-12-13 14:38:15.856682

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

from dundie.models.user import User

# revision identifiers, used by Alembic.
revision = '5da41f08259d'
down_revision = '17d6d190084e'
branch_labels = None
depends_on = None


def upgrade() -> None:  # NEW
    bind = op.get_bind()
    session = sqlmodel.Session(bind=bind)

    admin = User(
        name="Admin",
        username="admin",
        email="admin@dm.com",
        dept="management",
        currency="USD",
        password="admin",  # pyright: ignore
    )
    # if admin user already exists it will raise IntegrityError
    try:
        session.add(admin)
        session.commit()
    except sa.exc.IntegrityError:
        session.rollback()


def downgrade() -> None:
    pass
