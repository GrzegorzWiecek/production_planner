import streamlit as st
from sqlalchemy.orm import Session

from database.connection import engine
from database.crud import (
    create_production_order,
    get_production_orders,
    complete_production_order,
)


st.set_page_config(
    page_title="Production Planner",
    page_icon="🏭",
    layout="wide",
)

st.title("🏭 Production Planner")

############################
# FORMULARZ
#########################
st.subheader("Add production order")

with st.form("production_order_form"):
    order_number = st.text_input("Order number")
    product = st.text_input("Product")
    quantity = st.number_input("Quantity", min_value=1, step=1)
    planned_date = st.date_input("Planned date")

    submitted = st.form_submit_button("Add order")

with Session(engine) as session:
    orders = get_production_orders(session)


##########################
######## formularz → CRUD → SQLAlchemy → SQLite
##########################
if submitted:
    if not order_number or not product:
        st.error("Order number and product are required.")
    else:
        with Session(engine) as session:
            try:
                create_production_order(
                    session=session,
                    order_number=order_number,
                    product=product,
                    quantity=quantity,
                    planned_date=planned_date,
                )

                st.success(f"Order {order_number} added successfully.")
                st.rerun()

            except Exception as e:
                session.rollback()
                st.error(f"Error: {e}")





#######################################

if orders:
    data = [
        {
            "Order": order.order_number,
            "Product": order.product,
            "Quantity": order.quantity,
            "Planned date": order.planned_date,
            "Completed": order.completed,
        }
        for order in orders
    ]

    #st.dataframe(data, width="stretch")
    st.divider()

    for order in orders:
        col1, col2, col3, col4, col5, col6 = st.columns(
            [1.5, 2, 1, 1.5, 1, 1]
        )

        col1.write(order.order_number)
        col2.write(order.product)
        col3.write(order.quantity)
        col4.write(order.planned_date)
        col5.write("✅" if order.completed else "⏳")

        if not order.completed:
            if col6.button("Complete", key=f"complete_{order.id}"):
                with Session(engine) as session:
                    complete_production_order(session, order.id)

                st.rerun()

else:
    st.info("No production orders found.")