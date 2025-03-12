import sys
import click
from database import get_db
from models import User, Transaction

def get_session():
    engine, session = get_db()
    return session

def display_menu():
    """Display menu options"""
    print("\n📊 Budget Tracker CLI")
    print("1. Add User")
    print("2. Add Transaction")
    print("3. View Transactions")
    print("4. View User Balance")
    print("5. Delete Transaction")
    print("6. Exit")

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
def add_user(name):
    """Add a new user"""
    session = get_session()
    user = User(name=name)
    session.add(user)
    session.commit()
    print(f"✅ User '{name}' added successfully!")

@cli.command()
@click.argument('name')
@click.argument('amount', type=float)
@click.argument('category')
@click.argument('description', required=False)
def add_transaction(name, amount, category, description):
    """Add a transaction for a user"""
    session = get_session()
    transaction = Transaction(user_id=name, amount=amount, category=category, description=description)
    session.add(transaction)
    session.commit()
    print("✅ Transaction added successfully!")

@cli.command()
def view_transactions():
    """View all transactions"""
    session = get_session()
    transactions = session.query(Transaction).all()
    if transactions:
        for txn in transactions:
            print(txn)
    else:
        print("❌ No transactions found!")

@cli.command()
@click.argument('name')
def view_balance(name):
    """View user balance"""
    session = get_session()
    balance = sum(txn.amount for txn in session.query(Transaction).filter_by(user_id=name).all())
    print(f"💰 User {name} Balance: {balance}")

@cli.command()
@click.argument('txn_id', type=int)
def delete_transaction(txn_id):
    """Delete a transaction by ID"""
    session = get_session()
    transaction = session.query(Transaction).get(txn_id)
    if transaction:
        session.delete(transaction)
        session.commit()
        print("✅ Transaction deleted successfully!")
    else:
        print("❌ Transaction not found!")

def main():
    while True:
        display_menu()
        choice = input("Enter choice: ")
        
        if choice == '1':
            name = input("Enter username: ")
            ctx = click.Context(add_user)
            ctx.invoke(add_user, name=name)
        elif choice == '2':
            name = input("Enter username: ")
            amount = float(input("Enter amount (+ for income, - for expense): "))
            category = input("Enter category: ")
            description = input("Enter description (optional): ")
            ctx = click.Context(add_transaction)
            ctx.invoke(add_transaction, name=name, amount=amount, category=category, description=description)
        elif choice == '3':
            ctx = click.Context(view_transactions)
            ctx.invoke(view_transactions)
        elif choice == '4':
            name = input("Enter username: ")
            ctx = click.Context(view_balance)
            ctx.invoke(view_balance, name=name)
        elif choice == '5':
            txn_id = int(input("Enter transaction ID to delete: "))
            ctx = click.Context(delete_transaction)
            ctx.invoke(delete_transaction, txn_id=txn_id)
        elif choice == '6':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice, try again!")

if __name__ == "__main__":
    main()