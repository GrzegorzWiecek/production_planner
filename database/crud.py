from datetime import date, datetime
from sqlalchemy.orm import Session, joinedload
from database.models import ProductionOrder, Workplace, Workstation


def create_production_order(
    session: Session,
    order_number: str,
    product: str,
    quantity: int,
    planned_date: date,
    workstation_id: int,
):
    order = ProductionOrder(
        order_number=order_number,
        product=product,
        quantity=quantity,
        planned_date=planned_date,
        workstation_id=workstation_id,
    )

    session.add(order)
    session.commit()
    session.refresh(order)

    return order


def get_production_orders(session: Session):
    return (
        session.query(ProductionOrder)
        .options(joinedload(ProductionOrder.workstation))
        .all()
    )


def complete_production_order(
    session: Session,
    order_id: int,
    completion_note: str | None = None,
):
    order = session.get(ProductionOrder, order_id)

    if order is None:
        raise ValueError("Production order not found.")

    if order.started_at is None:
        raise ValueError("Production order has not been started.")

    if order.completed:
        raise ValueError("Production order is already completed.")

    order.completed = True
    order.completed_at = datetime.now()
    order.completion_note = completion_note

    session.commit()
    session.refresh(order)

    return order

def create_workplace(session: Session, name: str):
    workplace = Workplace(name=name)

    session.add(workplace)
    session.commit()
    session.refresh(workplace)

    return workplace


def create_workstation(
    session: Session,
    name: str,
    workplace_id: int,
):
    workstation = Workstation(
        name=name,
        workplace_id=workplace_id,
    )

    session.add(workstation)
    session.commit()
    session.refresh(workstation)

    return workstation

def get_workplaces(session: Session):
    return session.query(Workplace).all()


def get_workstations(session: Session, workplace_id: int):
    return (
        session.query(Workstation)
        .filter(Workstation.workplace_id == workplace_id)
        .all()
    )

def start_production_order(session: Session, order_id: int):
    order = session.get(ProductionOrder, order_id)

    if order is None:
        raise ValueError("Production order not found.")

    if order.started_at is not None:
        raise ValueError("Production order has already been started.")

    order.started_at = datetime.now()
    session.commit()
    session.refresh(order)

    return order

def get_production_order_by_number(
    session: Session,
    order_number: str,
):
    return (
        session.query(ProductionOrder)
        .filter(ProductionOrder.order_number == order_number)
        .first()
    )