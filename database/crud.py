from datetime import date
from sqlalchemy.orm import Session
from database.models import ProductionOrder


def create_production_order(
    session: Session,
    order_number: str,
    product: str,
    quantity: int,
    planned_date: date,
):
    order = ProductionOrder(
        order_number=order_number,
        product=product,
        quantity=quantity,
        planned_date=planned_date,
    )

    session.add(order)
    session.commit()
    session.refresh(order)

    return order


def get_production_orders(session: Session):
    return session.query(ProductionOrder).all()

def complete_production_order(session: Session, order_id: int):
    order = session.get(ProductionOrder, order_id)

    if order is None:
        raise ValueError("Production order not found.")

    order.completed = True
    session.commit()

    return order