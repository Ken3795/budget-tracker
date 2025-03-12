
import click
from database import get_db
from models import User, Transaction

def get_session():
    engine, session = get_db()
    return session

def main():
    session = get_session()
    while True:
        print("\n📊 Budget Tracker CLI")
        print("1. Add User")
        print("2. Add Transaction")
        print("3. View Transactions")
        print("4. View User Balance")
        print("5. Delete Transaction")
        print("6. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter username: ")
            user = User(name=name)
            session.add(user)
            session.commit()
            print(f"✅ User '{name}' added successfully!")

        elif choice == '2':
            name = input("Enter username: ")
            amount = float(input("Enter amount (+ for income, - for expense): "))
            category = input("Enter category: ")
            description = input("Enter description (optional): ")
            transaction = Transaction(user_id=name, amount=amount, category=category, description=description)
            session.add(transaction)
            session.commit()
            print("✅ Transaction added successfully!")

        elif choice == '3':
            transactions = session.query(Transaction).all()
            if transactions:
                for txn in transactions:
                    print(txn)
            else:
                print("❌ No transactions found!")

        elif choice == '4':
            name = input("Enter username: ")
            balance = sum(txn.amount for txn in session.query(Transaction).filter_by(user_id=name).all())
            print(f"💰 User {name} Balance: {balance}")

        elif choice == '5':
            txn_id = int(input("Enter transaction ID to delete: "))
            transaction = session.query(Transaction).get(txn_id)
            if transaction:
                session.delete(transaction)
                session.commit()
                print("✅ Transaction deleted successfully!")
            else:
                print("❌ Transaction not found!")

        elif choice == '6':
            print("👋 Exiting...")
            session.close()
            sys.exit()

        else:
            print("❌ Invalid choice, try again!")

if __name__ == "__main__":
    main()
