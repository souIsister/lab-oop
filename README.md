# Python Laboratory Projects

A collection of Python laboratory assignments from my Computer Science coursework at City College of Angeles.

## 🐍 Projects Overview

### Lab 1: Input/Output & String Formatting
**File:** `lab1.py`

Learn the fundamentals of Python I/O operations and string formatting techniques.

**Concepts Covered:**
- Print statements and ASCII art
- Basic input/output operations
- String formatting with f-strings and % specifiers
- Type casting (int, float)
- String manipulation

**Key Programs:**
1. ASCII art display (CODE text)
2. Database record formatting
3. Email template with user input
4. Social media post scheduling with formatted output
5. Type casting and arithmetic operations

**What It Does:**
The program takes user input and demonstrates various formatting techniques like ASCII art, f-strings, and the % operator. Then it performs type casting to show the difference between integers and floats.

---

### Lab 2: Loops & Nested Structures
**File:** `lab2.py`

Master control flow with loops and nested iterations.

**Concepts Covered:**
- For loops and while loops
- Nested loops
- Time module usage
- Loop control (range function)
- Time formatting

**Key Programs:**
1. **Countdown Timer** - Takes user input (time in seconds) and counts down, displaying hours:minutes:seconds format. Uses time.sleep() to create real-time countdown.
2. **Multiplication Table** - Generates a multiplication table based on user-specified rows and columns.

---

### Lab 3: List Operations & Menu System
**File:** `lab3.py`

Build interactive menu-driven applications using lists.

**Concepts Covered:**
- List manipulation (append, remove, sort)
- While loops with menu systems
- String searching and comparison
- List iteration
- Conditional logic

**Features:**
- Add games to a list
- Search for games in the list
- Remove games from the list
- View all games sorted alphabetically
- Exit program gracefully

**Menu-Driven Interface:**
- `1` - Add a game
- `2` - Search for a game
- `3` - Remove a game
- `4` - View all games (sorted)
- `0` - Exit

---

### Lab 4: Dictionary Operations & Shopping System
**File:** `lab4.py`

Work with dictionaries to create a simple shopping/ordering system.

**Concepts Covered:**
- Dictionary creation and iteration
- Dictionary lookups and retrieval
- List operations for order tracking
- Price calculations
- Formatted currency output

**Features:**
- Displays a menu of items with prices
- Allows user to add items to order
- Tracks order items and prices in separate lists
- Calculates and displays total cost
- User-friendly command-line interface

---

### Lab 5: Object-Oriented Programming - User Class
**Files:** `lab5/main.py`, `lab5/testUser.py`

Introduction to classes and object-oriented programming with a social media user system.

**Concepts Covered:**
- Class definition and constructors (`__init__`)
- Instance methods and attributes
- Object instantiation
- Lists of objects
- Module imports and file organization

**Files:**
- **main.py** - Defines the `User` class with:
  - Attributes: first name, last name, followers, friends list
  - Method: `describe()` - displays user information
  
- **testUser.py** - Test file that imports and uses the `User` class to:
  - Create user profiles interactively
  - Store multiple user records
  - Display all user information
  - Count total members

**Features:**
- Create user profiles with name, follower count, and friends list
- Store multiple user records in a list
- Display user information in a formatted way
- Interactive menu-driven input system
- Count total members

---

### Lab 6: Object-Oriented Programming - Money Class
**Files:** `lab6/bankAccount.py`, `lab6/testMoney.py`

Learn about class constructors with default parameters and flexible parameter handling.

**Concepts Covered:**
- Class definition with default parameters
- Type hints in Python
- Constructor overloading (using default values)
- Object creation with different parameter combinations
- Module imports and testing

**Files:**
- **bankAccount.py** - Defines the `Money` class with:
  - Attributes: amount (default: 0), denomination (default: "Unknown")
  - Type hints for better code documentation
  
- **testMoney.py** - Test file that demonstrates:
  - Creating `Money` objects with no parameters
  - Creating `Money` objects with amount only
  - Creating `Money` objects with amount and denomination
  - Shows how default parameters work

**Features:**
- Create money objects with flexible parameters
- Default values for amount and denomination
- Multiple ways to invoke the constructor
- Shows OOP principles with simple practical example

---

## 📚 Learning Outcomes

After working through these labs, you'll understand:
- ✅ Basic Python syntax and data types
- ✅ Input/output operations
- ✅ String formatting techniques
- ✅ Control flow structures (loops, conditionals)
- ✅ Data structures (lists, dictionaries)
- ✅ Menu-driven application design
- ✅ Object-Oriented Programming (OOP) basics
- ✅ Classes, constructors, and methods
- ✅ Module imports and code organization
- ✅ Type hints and documentation

## 📝 How These Labs Work

Labs 1-4 are **interactive command-line programs**. Users run the program in their terminal/console and interact by typing inputs:

- **Lab 1** asks for user input and displays formatted output
- **Lab 2** asks how many seconds for countdown, or rows/columns for the table
- **Lab 3** displays a menu and lets you add/search/remove games
- **Lab 4** shows a menu of items and lets you build an order

Labs 5-6 use **multiple related files** with imports:

- **Lab 5** imports the `User` class from `main.py` into `testUser.py` to test functionality
- **Lab 6** imports the `Money` class from `bankAccount.py` into `testMoney.py` to demonstrate constructor flexibility

---

## ⛓️ Repository Structure

```
├── lab1/
│   └── lab1.py
├── lab2/
│   └── lab2.py
├── lab3/
│   └── lab3.py
├── lab4/
│   └── lab4.py
├── lab5/
│   ├── main.py
│   └── testUser.py
├── lab6/
│   ├── bankAccount.py
│   └── testMoney.py
└── README.md
```

---

## 🛠 Requirements

- Python 3.x
- No external libraries required (all use standard library)
- Run from command line/terminal

---

## 👤 Author

**Aj Jovan**  
Computer Science Student  
City College of Angeles

---

*Last updated: October 2025*  
*All code written as part of laboratory coursework*
