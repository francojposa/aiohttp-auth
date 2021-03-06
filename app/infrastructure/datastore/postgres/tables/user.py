import sqlalchemy as sa

from app.infrastructure.datastore.postgres.tables.metadata import METADATA

USER = sa.Table(
    "users",
    METADATA,
    sa.Column("id", sa.String, primary_key=True),
    sa.Column("username", sa.String, unique=True, nullable=False),
    sa.Column("pass_hash", sa.String, nullable=False),
    sa.Column("email", sa.String, nullable=False),
    sa.Column("role_id", sa.String, nullable=False),
    sa.Column("enabled", sa.Boolean, nullable=False, server_default="true"),
    sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
    sa.Column(
        "updated_at",
        sa.DateTime,
        nullable=False,
        server_default=sa.func.now(),
        server_onupdate=sa.func.now(),
    ),
)
