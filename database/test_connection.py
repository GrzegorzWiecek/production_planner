# from database.connection import engine
#
# with engine.connect() as connection:
#     print("Database connection: OK")

# from database.connection import engine
# from database.models import Base
#
#
# Base.metadata.create_all(engine)
#
# print("Database connection: OK")
# print("Database tables: CREATED")

from datetime import date

# from database.connection import engine
# from database.models import Base, ProductionOrder
# from sqlalchemy.orm import Session
#
#
# Base.metadata.create_all(engine)

# with Session(engine) as session:
#     order = ProductionOrder(
#         order_number="PO-0001",
#         product="Test Product",
#         quantity=100,
#         planned_date=date.today(),
#     )
#
#     session.add(order)
#     session.commit()
#
#     print(f"Order created: {order.order_number}")

# with Session(engine) as session:
#     orders = session.query(ProductionOrder).all()
#
#     for order in orders:
#         print(
#             order.id,
#             order.order_number,
#             order.product,
#             order.quantity,
#             order.planned_date,
#             order.completed,
#         )

from datetime import date

from sqlalchemy.orm import Session

from database.connection import engine
from database.models import Base
from database.crud import create_production_order, get_production_orders


Base.metadata.create_all(engine)


with Session(engine) as session:

    try:
        order = create_production_order(
            session=session,
            order_number="PO-0002",
            product="Test Product 2",
            quantity=250,
            planned_date=date.today(),
        )

        print(f"Order created: {order.order_number}")

    except Exception as e:
        session.rollback()
        print(f"Error: {e}")


with Session(engine) as session:

    orders = get_production_orders(session)

    for order in orders:
        print(
            order.id,
            order.order_number,
            order.product,
            order.quantity,
            order.planned_date,
            order.completed,
        )