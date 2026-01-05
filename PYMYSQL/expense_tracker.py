from mysql import connector

class ExpenseTrack:

    def __init__(self):
        try:
            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="Password@123",
                database="expense_tracker"
            )
            self.cursor = self.connection.cursor()
            print("DB connected")

        except Exception as e:
            print(e)

    # ---------------- CREATE ----------------
    def add_expense(self, **kwargs):
        try:
            columns = ""
            values = ""

            for k in kwargs.keys():
                columns += k + ","
                values += "%s,"

            columns = columns.rstrip(",")
            values = values.rstrip(",")

            query = f"INSERT INTO expense_track ({columns}) VALUES ({values})"
            data = tuple(kwargs.values())

            self.cursor.execute(query, data)
            self.connection.commit()

            print("Expense added")

        except Exception as e:
            print(e)

    # ---------------- READ (ALL) ----------------
    def list_all_expenses(self):
        try:
            query = "SELECT * FROM expense_track"
            self.cursor.execute(query)
            records = self.cursor.fetchall()

            if not records:
                print("⚠️ No expenses found")
            else:
                print("\n📋 Expense Records")
                for row in records:
                    print(row)

        except Exception as e:
            print(e)

    # ---------------- READ (ONE) ----------------
    def retrieve_expense(self, id):
        try:
            query = "SELECT * FROM expense_track WHERE id=%s"
            self.cursor.execute(query, (id,))
            record = self.cursor.fetchone()

            if record:
                print(record)
            else:
                print("⚠️ Expense not found")

        except Exception as e:
            print(e)

    # ---------------- UPDATE ----------------
    def update_expense(self, id, **kwargs):
        try:
            placeholder = ""

            for k in kwargs.keys():
                placeholder += f"{k}=%s,"

            placeholder = placeholder.rstrip(",")

            query = f"UPDATE expense_track SET {placeholder} WHERE id=%s"
            data = tuple(kwargs.values()) + (id,)

            self.cursor.execute(query, data)
            self.connection.commit()

            if self.cursor.rowcount > 0:
                print("Expense updated")
            else:
                print(" Expense ID not found")

        except Exception as e:
            print(e)

    # ---------------- DELETE ----------------
    def delete_expense(self, id):
        try:
            query = "DELETE FROM expense_track WHERE id=%s"
            self.cursor.execute(query, (id,))
            self.connection.commit()

            if self.cursor.rowcount > 0:
                print("Expense deleted")
            else:
                print("⚠️ Expense ID not found")

        except Exception as e:
            print(e)

    # ---------------- CLOSE ----------------
    def close_connection(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("DB closed")


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":

    expense = ExpenseTrack()

    # CREATE
    expense.add_expense(
        title="Food",
        amount=250,
        category="Meals",
        expense_date="2026-01-05",
        payment_mode="UPI",
        notes="Lunch"
    )

    # READ ALL
    expense.list_all_expenses()

    # READ ONE
    expense.retrieve_expense(1)

    # UPDATE
    expense.update_expense(
        id=1,
        amount=300,
        payment_mode="Cash"
    )

    # DELETE
    expense.delete_expense(2)

    # FINAL READ
    expense.list_all_expenses()

    expense.close_connection()
expense_instance1 = ExpenseTrack()

expense_instance1.add_expense(
    title="Food",
    amount=250,
    category="Food"
)

expense_instance1.list_all_expenses()

expense_instance1.update_expense(id=1, amount=300)

expense_instance1.list_all_expenses()

expense_instance1.delete_expense(id=1)

expense_instance1.close_connection()
