"""
data_generator.py
Generate various types of random data for testing iterative design patterns

USAGE:
------
# Import specific generators:
from data_generator import generate_students, generate_products, generate_numbers

# Generate data:
students = generate_students(100)  # 100 student records
numbers = generate_numbers(50, min_val=0, max_val=100)  # 50 integers from 0-100

# Import everything:
from test_data_generator import *
all_data = generate_all_datasets()  # Dictionary with all data types

# Working with generated objects:
students = generate_students(30)
cs_students = [s for s in students if s.major == 'CS']
high_achievers = [s.name for s in students if s.grade >= 90]
average_grade = sum(s.grade for s in students) / len(students)

AVAILABLE GENERATORS:
--------------------
- generate_numbers(n, min_val, max_val, type='int'/'float')
- generate_strings(n, min_len, max_len)
- generate_words(n)
- generate_sentences(n)
- generate_students(n) -> List[Student(name, age, grade, major, credits)]
- generate_products(n) -> List[Product(id, name, price, quantity, category, rating)]
- generate_transactions(n) -> List[Transaction(id, date, amount, category, merchant, status)]
- generate_logs(n) -> List[LogEntry(timestamp, level, message, module, user_id)]
- generate_matrix(rows, cols, min_val, max_val)
- generate_grades_dict(n_students, n_assignments)
- generate_time_series(days, initial_value)
- generate_user_data(n)
- generate_mixed_types()
- generate_emails_text()
- generate_pattern_numbers()
"""

import random
import string
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import List, Dict, Any

# Seed for reproducibility (comment out for true randomness)
random.seed(42)

# ============================================================================
# BASIC DATA GENERATORS
# ============================================================================

def generate_numbers(n=100, min_val=-100, max_val=100, type='int'):
    """Generate random numbers"""
    if type == 'int':
        return [random.randint(min_val, max_val) for _ in range(n)]
    elif type == 'float':
        return [random.uniform(min_val, max_val) for _ in range(n)]
    else:
        raise ValueError("type must be 'int' or 'float'")

def generate_strings(n=50, min_len=3, max_len=15):
    """Generate random strings"""
    strings = []
    for _ in range(n):
        length = random.randint(min_len, max_len)
        s = ''.join(random.choices(string.ascii_lowercase, k=length))
        strings.append(s)
    return strings

def generate_words(n=100):
    """Generate semi-realistic words"""
    prefixes = ['pre', 'anti', 'de', 'dis', 'over', 'under', 'semi', 'non', 'sub', '']
    roots = ['work', 'play', 'think', 'run', 'walk', 'talk', 'read', 'write', 'code', 'test']
    suffixes = ['ing', 'ed', 'er', 'est', 'ly', 'ness', 'ment', 'ful', 'less', '']
    
    words = []
    for _ in range(n):
        word = random.choice(prefixes) + random.choice(roots) + random.choice(suffixes)
        words.append(word)
    return words

def generate_sentences(n=30):
    """Generate random sentences"""
    subjects = ['The student', 'A professor', 'The algorithm', 'Python', 'The data']
    verbs = ['processes', 'analyzes', 'transforms', 'filters', 'aggregates', 'computes']
    objects = ['the results', 'large datasets', 'complex patterns', 'user input', 'the output']
    
    sentences = []
    for _ in range(n):
        sentence = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}."
        if random.random() > 0.7:  # 30% chance to add a clause
            clauses = [' quickly', ' efficiently', ' with precision', ' carefully']
            sentence = sentence[:-1] + random.choice(clauses) + '.'
        sentences.append(sentence)
    return sentences

# ============================================================================
# STRUCTURED DATA GENERATORS
# ============================================================================

@dataclass
class Student:
    name: str
    age: int
    grade: float
    major: str
    credits: int
    
def generate_students(n=50):
    """Generate student records"""
    first_names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller']
    majors = ['CS', 'Math', 'Physics', 'Biology', 'Chemistry', 'English', 'History', 'Art']
    
    students = []
    for i in range(n):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        age = random.randint(18, 26)
        grade = round(random.uniform(55, 100), 1)
        major = random.choice(majors)
        credits = random.randint(12, 18)
        students.append(Student(name, age, grade, major, credits))
    
    return students

@dataclass
class Product:
    id: int
    name: str
    price: float
    quantity: int
    category: str
    rating: float
    
def generate_products(n=100):
    """Generate product inventory"""
    prefixes = ['Ultra', 'Pro', 'Basic', 'Premium', 'Eco', 'Smart', 'Power', 'Mini']
    items = ['Laptop', 'Phone', 'Tablet', 'Watch', 'Speaker', 'Camera', 'Headphones']
    categories = ['Electronics', 'Computers', 'Audio', 'Photography', 'Wearables']
    
    products = []
    for i in range(n):
        name = f"{random.choice(prefixes)} {random.choice(items)}"
        price = round(random.uniform(29.99, 2999.99), 2)
        quantity = random.randint(0, 500)
        category = random.choice(categories)
        rating = round(random.uniform(1.0, 5.0), 1)
        products.append(Product(i+1000, name, price, quantity, category, rating))
    
    return products

@dataclass
class Transaction:
    id: int
    date: datetime
    amount: float
    category: str
    merchant: str
    status: str
    
def generate_transactions(n=200):
    """Generate financial transactions"""
    categories = ['Food', 'Transport', 'Entertainment', 'Shopping', 'Bills', 'Healthcare']
    merchants = ['Amazon', 'Walmart', 'Starbucks', 'Uber', 'Netflix', 'CVS', 'Target']
    statuses = ['completed', 'completed', 'completed', 'pending', 'failed']  # 60% completed
    
    transactions = []
    start_date = datetime.now() - timedelta(days=90)
    
    for i in range(n):
        date = start_date + timedelta(days=random.randint(0, 90),
                                     hours=random.randint(0, 23))
        amount = round(random.uniform(5.0, 500.0), 2)
        category = random.choice(categories)
        merchant = random.choice(merchants)
        status = random.choice(statuses)
        transactions.append(Transaction(i+5000, date, amount, category, merchant, status))
    
    return transactions

@dataclass
class LogEntry:
    timestamp: datetime
    level: str
    message: str
    module: str
    user_id: int
    
def generate_logs(n=500):
    """Generate log entries"""
    levels = ['INFO', 'INFO', 'INFO', 'WARNING', 'WARNING', 'ERROR', 'DEBUG', 'CRITICAL']
    modules = ['auth', 'database', 'api', 'payment', 'email', 'cache']
    messages = {
        'INFO': ['User logged in', 'Request processed', 'File uploaded', 'Cache updated'],
        'WARNING': ['High memory usage', 'Slow query detected', 'Rate limit approaching'],
        'ERROR': ['Connection failed', 'Invalid input', 'Timeout occurred', 'Permission denied'],
        'DEBUG': ['Variable value', 'Function called', 'Loop iteration'],
        'CRITICAL': ['System crash', 'Data corruption detected', 'Security breach']
    }
    
    logs = []
    start_time = datetime.now() - timedelta(hours=24)
    
    for i in range(n):
        timestamp = start_time + timedelta(minutes=random.randint(0, 1440))
        level = random.choice(levels)
        message = random.choice(messages.get(level, ['Generic message']))
        module = random.choice(modules)
        user_id = random.randint(1000, 9999)
        logs.append(LogEntry(timestamp, level, message, module, user_id))
    
    return logs

# ============================================================================
# SPECIAL DATA GENERATORS
# ============================================================================

def generate_matrix(rows=5, cols=5, min_val=0, max_val=10):
    """Generate 2D matrix"""
    return [[random.randint(min_val, max_val) for _ in range(cols)] 
            for _ in range(rows)]

def generate_grades_dict(n_students=20, n_assignments=5):
    """Generate dictionary of student grades"""
    students = [f"Student_{i:02d}" for i in range(1, n_students+1)]
    assignments = [f"HW_{i}" for i in range(1, n_assignments+1)]
    
    grades = {}
    for student in students:
        grades[student] = {
            assignment: random.randint(60, 100) 
            for assignment in assignments
        }
    
    return grades

def generate_time_series(days=30, initial=100):
    """Generate time series data"""
    data = []
    value = initial
    start_date = datetime.now() - timedelta(days=days)
    
    for i in range(days):
        date = start_date + timedelta(days=i)
        # Random walk
        change = random.uniform(-10, 12)  # Slight upward bias
        value = max(0, value + change)
        data.append({
            'date': date,
            'value': round(value, 2),
            'volume': random.randint(1000, 10000)
        })
    
    return data

def generate_user_data(n=100):
    """Generate user profiles with nested data"""
    users = []
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia']
    
    for i in range(n):
        user = {
            'id': i + 1,
            'username': f"user_{i:04d}",
            'email': f"user_{i:04d}@example.com",
            'age': random.randint(18, 65),
            'city': random.choice(cities),
            'active': random.random() > 0.2,  # 80% active
            'premium': random.random() > 0.7,  # 30% premium
            'purchases': [
                {
                    'item': f"item_{random.randint(1, 50)}",
                    'price': round(random.uniform(10, 200), 2),
                    'date': datetime.now() - timedelta(days=random.randint(1, 90))
                }
                for _ in range(random.randint(0, 10))
            ]
        }
        users.append(user)
    
    return users

def generate_mixed_types():
    """Generate list with mixed types for testing type filtering"""
    return [
        42, "hello", 3.14, None, True, [1, 2, 3], "world", 
        -17, False, {'key': 'value'}, 0, "", [], {}, 
        "Python", 100, 2.718, set([1, 2]), (1, 2, 3)
    ] * 5  # Repeat for larger dataset

# ============================================================================
# DATA WITH SPECIFIC PATTERNS
# ============================================================================

def generate_emails_text():
    """Generate text containing email addresses"""
    domains = ['gmail.com', 'yahoo.com', 'company.com', 'university.edu']
    text_parts = [
        "Contact us at",
        "Send feedback to",
        "Email:",
        "Reach out to",
        "For support, contact"
    ]
    
    lines = []
    for _ in range(30):
        if random.random() > 0.3:  # 70% have emails
            username = ''.join(random.choices(string.ascii_lowercase, k=8))
            email = f"{username}@{random.choice(domains)}"
            text = f"{random.choice(text_parts)} {email}"
            if random.random() > 0.5:  # Add noise
                text += f" or call {random.randint(100, 999)}-{random.randint(1000, 9999)}"
        else:
            text = "This line contains no email address."
        lines.append(text)
    
    return lines

def generate_pattern_numbers():
    """Generate numbers with specific patterns"""
    numbers = []
    
    # Add some perfect squares
    numbers.extend([i**2 for i in range(1, 11)])
    
    # Add some primes
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    numbers.extend(primes)
    
    # Add some Fibonacci numbers
    fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    numbers.extend(fibs)
    
    # Add random numbers
    numbers.extend([random.randint(1, 100) for _ in range(50)])
    
    random.shuffle(numbers)
    return numbers

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def print_sample(data, name="Data", n=5):
    """Print a sample of the generated data"""
    print(f"\n{name} (first {n} items):")
    print("-" * 50)
    for item in data[:n]:
        print(f"  {item}")
    print(f"  ... (total: {len(data)} items)")

def generate_all_datasets():
    """Generate all types of data and return as dictionary"""
    return {
        'numbers': generate_numbers(),
        'floats': generate_numbers(type='float'),
        'strings': generate_strings(),
        'words': generate_words(),
        'sentences': generate_sentences(),
        'students': generate_students(),
        'products': generate_products(),
        'transactions': generate_transactions(),
        'logs': generate_logs(),
        'matrix': generate_matrix(),
        'grades': generate_grades_dict(),
        'time_series': generate_time_series(),
        'users': generate_user_data(),
        'mixed_types': generate_mixed_types(),
        'emails_text': generate_emails_text(),
        'pattern_numbers': generate_pattern_numbers()
    }

# ============================================================================
# MAIN - Demo all generators
# ============================================================================

if __name__ == "__main__":
    print("DATA GENERATOR FOR ITERATIVE PATTERNS TESTING")
    print("=" * 50)
    
    # Generate all datasets
    datasets = generate_all_datasets()
    
    # Show samples
    for name, data in datasets.items():
        if isinstance(data, dict) and name == 'grades':
            print(f"\n{name}:")
            print("-" * 50)
            for student, grades in list(data.items())[:3]:
                print(f"  {student}: {grades}")
            print(f"  ... (total: {len(data)} students)")
        else:
            print_sample(data, name)
    
    print("\n" + "=" * 50)
    print("Data generation complete!")
    print("\nUsage example:")
    print("  from test_data_generator import generate_students")
    print("  students = generate_students(100)")
    print("  cs_students = [s for s in students if s.major == 'CS']")