from database.connection import engine
from database.models import Base


Base.metadata.create_all(engine)

print("Database connection: OK")
print("Database tables: OK")
#
# from database.connection import engine
# from database.models import Base
# from database.crud import create_workplace, create_workstation
# from sqlalchemy.orm import Session
#
#
# Base.metadata.create_all(engine)
#
#
# with Session(engine) as session:
#     workplace = create_workplace(
#         session,
#         "Production Hall 1",
#     )
#
#     workstation_1 = create_workstation(
#         session,
#         "CNC-01",
#         workplace.id,
#     )
#
#     workstation_2 = create_workstation(
#         session,
#         "CNC-02",
#         workplace.id,
#     )
#
#     print(f"Workplace: {workplace.name}")
#     print(f"Workstations: {workstation_1.name}, {workstation_2.name}")