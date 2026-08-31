import streamlit as st
from sqlalchemy.orm import Session

from database.connection import engine
from database.crud import (
    create_production_order,
    get_production_orders,
    start_production_order,
    complete_production_order,
    get_workplaces,
    get_workstations,
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

with Session(engine) as session:
    workplaces = get_workplaces(session)

with st.form("production_order_form"):
    order_number = st.text_input("Order number")
    product = st.text_input("Product")
    quantity = st.number_input("Quantity", min_value=1, step=1)
    planned_date = st.date_input("Planned date")

    workplace = st.selectbox(
        "Workplace",
        workplaces,
        format_func=lambda x: x.name,
    )

    with Session(engine) as session:
        workstations = get_workstations(session, workplace.id)

    workstation = st.selectbox(
        "Workstation",
        workstations,
        format_func=lambda x: x.name,
    )

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
                    workstation_id=workstation.id,
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

        st.divider()

        col1, col2, col3, col4, col5 = st.columns([1.5, 2, 1, 1.5, 1.5])

        col1.write(f"**{order.order_number}**")
        col2.write(order.product)
        col3.write(f"Qty: {order.quantity}")
        col4.write(order.workstation.name)

        if order.completed:

            col5.success("COMPLETED")

            if order.started_at and order.completed_at:
                execution_time = order.completed_at - order.started_at
                st.write(
                    f"Execution time: **{execution_time}**"
                )

            if order.completion_note:
                st.info(f"Note: {order.completion_note}")

        elif order.started_at:

            col5.warning("IN PROGRESS")

            st.write(
                f"Started: **{order.started_at.strftime('%Y-%m-%d %H:%M:%S')}**"
            )

            completion_note = st.text_input(
                "Completion note",
                key=f"note_{order.id}",
                placeholder="Optional: explain any deviations...",
            )

            if st.button(
                    "Complete",
                    key=f"complete_{order.id}",
            ):
                with Session(engine) as session:
                    complete_production_order(
                        session,
                        order.id,
                        completion_note,
                    )

                st.rerun()

        else:

            col5.info("PLANNED")

            if st.button(
                    "Start",
                    key=f"start_{order.id}",
            ):
                with Session(engine) as session:
                    start_production_order(
                        session,
                        order.id,
                    )

                st.rerun()

else:
    st.info("No production orders found.")