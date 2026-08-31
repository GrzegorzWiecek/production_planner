from sqlalchemy import Boolean, Date, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class ProductionOrder(Base):
    __tablename__ = "production_orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    order_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    product: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    planned_date: Mapped[Date] = mapped_column(
        Date,
        nullable=False,
    )

    # workplace: Mapped[str] = mapped_column(
    #     String(100),
    #     nullable=False,
    # )
    #
    # workstation: Mapped[str] = mapped_column(
    #     String(100),
    #     nullable=False,
    # )
    workstation_id: Mapped[int] = mapped_column(
        ForeignKey("workstations.id"),
        nullable=False,
    )

    workstation: Mapped["Workstation"] = relationship()

    started_at: Mapped[DateTime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    completed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    completed_at: Mapped[DateTime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    completion_note: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False)

class Workplace(Base):
    __tablename__ = "workplaces"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    workstations: Mapped[list["Workstation"]] = relationship(
        back_populates="workplace"
    )


class Workstation(Base):
    __tablename__ = "workstations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    workplace_id: Mapped[int] = mapped_column(
        ForeignKey("workplaces.id"),
        nullable=False,
    )

    workplace: Mapped["Workplace"] = relationship(
        back_populates="workstations"
    )