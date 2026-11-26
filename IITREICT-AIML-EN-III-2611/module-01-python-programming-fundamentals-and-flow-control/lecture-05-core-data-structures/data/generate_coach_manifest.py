"""Generate 120 invented coach-manifest rows for the Core Data Structures lecture."""
import csv
import random

random.seed(42)
NAMES = [
    "Meera", "Arjun", "Priya", "Dev", "Riya", "Kiran", "Ananya", "Rohan",
    "Sneha", "Vikram", "Isha", "Nitin", "Pooja", "Aditya", "Neha", "Karthik",
]
COACHES = ["S1", "S2", "S3", "S4", "S5", "S6"]
BERTH = ["LB", "MB", "UB", "SL", "SU"]
STATUS = ["confirmed", "waitlisted"]

rows = []
for i in range(1, 121):
    pnr = f"{4829000 + i}"
    name = random.choice(NAMES)
    if i % 17 == 0:
        name = name + " " + random.choice(["K", "S", "R"])
    coach = random.choice(COACHES)
    row = random.randint(0, 8)
    col = random.randint(0, 2)
    berth = random.choice(BERTH)
    fee = random.choice([280, 350, 420, 420, 350])
    status = STATUS[0] if random.random() > 0.08 else STATUS[1]
    if i == 44:
        coach, row, col = "S3", 2, 1
    if i == 89:
        coach, row, col = "S3", 2, 1
    rows.append(
        {
            "pnr": pnr,
            "passenger": name,
            "coach": coach,
            "row": row,
            "col": col,
            "berth_code": berth,
            "fee_rs": fee,
            "status": status,
        }
    )

path = __file__.replace("generate_coach_manifest.py", "coach_manifest.csv")
with open(path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "pnr",
            "passenger",
            "coach",
            "row",
            "col",
            "berth_code",
            "fee_rs",
            "status",
        ],
    )
    w.writeheader()
    w.writerows(rows)
print(len(rows), "rows ->", path)