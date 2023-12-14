"""ensure_admin_user

Revision ID: f728b90d8558
Revises: 2828ccb1145f
Create Date: 2023-12-12 22:36:37.984623

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

from dundie.models.user import User

# revision identifiers, used by Alembic.
revision = 'f728b90d8558'
down_revision = '2828ccb1145f'
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
