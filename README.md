# Budget Tracker CLI App

# Author
Kenneth Too

## 📌 Descriptions
The **Budget Tracker CLI App** allows users to track their expenses and income through a simple command-line interface (CLI). Users can add transactions, categorize them, and view their financial summaries.

## 🚀 Features
- Add and manage users.
- Record income and expenses with descriptions and categories.
- View all transactions.
- Check the balance for each user.
- Delete transactions.
- Persistent data storage using SQLite and SQLAlchemy ORM.

## 🛠️ Technologies Used
- **Python** (3.12)
- **SQLite** (for database storage)
- **SQLAlchemy** (ORM for database interaction)

## 📂 Project Structure
```
📦 budget-tracker
├── database.py         
├── models.py           
├── cli.py              
├── README.md           
└── Pipfile             
```

## 🏗️ Installation & Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/Ken3795/budget-tracker.git
   cd budget-tracker
   ```

2. **Create a virtual environment:** 

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   
   ```sh
   pipenv install
   ```

4. **Create the database:**
   ```sh
   python database.py
   ```

5. **Run the CLI application:**
   ```sh
   python cli.py
   ```

## 📖 Usage
Upon running `cli.py`, the CLI presents a menu with options:

1. **Add User** → Creates a new user.
2. **Add Transaction** → Records income/expense for a user.
3. **View Transactions** → Lists all transactions.
4. **View User Balance** → Shows total balance for a user.
5. **Delete Transaction** → Removes a transaction by ID.
6. **Exit** → Closes the application.

### Example Usage
#### ➕ Adding a User
```
Enter choice: 1
Enter username: Kenneth
✅ User 'Kenneth' added successfully!
```

#### 💰 Adding a Transaction
```
Enter choice: 2
Enter username: Kenneth
Enter amount (+ for income, - for expense): -50
Enter category: Food
Enter description (optional): Dinner at a restaurant
✅ Transaction added successfully!
```

#### 📊 Viewing User Balance
```
Enter choice: 4
Enter username: Kenneth
💰 User 1 Balance: -50.0
```

## ❗ Notes
- Ensure `database.py` is run **before** using `cli.py` to set up the database.
- Use **unique usernames** when adding users.
- Transactions require a **valid user ID** to be recorded.

## 🤝 Contributions
Feel free to submit issues or pull requests to improve the project!

## 📞 Contact
For questions, reach out at: **kenkipkoech57@gmail.com**


## 📜 License
Copyright @2025 Kenneth Too

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
