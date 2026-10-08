🐍 Python Mastery Roadmap: 6 Progressive Projects
A curated collection of 6 hands-on projects designed to systematically test and build Python expertise — from foundational scripting to advanced concurrent systems. Each project is intentionally scoped with a "Twist": a specific technical constraint that forces you to apply idiomatic, production-grade patterns instead of taking shortcuts.

This isn't a tutorial series. It's a gauntlet. By the end, you'll have practical experience with OOP design, decorators, async I/O, and multi-core parallelism — the exact skills that separate intermediate Python users from engineers who ship real systems.

📋 Table of Contents
Philosophy
Roadmap Overview
Project 1: CLI Expense Tracker
Project 2: Multi-Criteria Text Analyzer
Project 3: E-Commerce Cart Engine
Project 4: API Logger & Rate Limiter
Project 5: Async Multi-Source Web Scraper
Project 6: Log Processing Pipeline
Suggested Repo Structure
How to Use This Roadmap
🎯 Philosophy
Most beginner projects teach syntax. This roadmap teaches design decisions.

Each project below has a deliberate constraint ("The Twist") that blocks the easy, naive solution and forces you toward the pattern that professional Python code actually uses — whether that's swapping for loops for functional tools, enforcing encapsulation with dunder methods, or reasoning about the GIL instead of just reading about it.

Difficulty increases progressively:

text

🟢 Easy           →  Core syntax, file I/O, error handling
🟡 Intermediate   →  OOP design, decorators, metaprogramming
🔴 Advanced       →  Concurrency, async I/O, performance profiling
🗺️ Roadmap Overview
#	Project	Difficulty	Core Focus
1	CLI Expense Tracker	🟢 Easy	Data structures, file handling, custom modules
2	Multi-Criteria Text Analyzer	🟢 Easy–Intermediate	Functional programming (map/filter/comprehensions)
3	E-Commerce Cart Engine	🟡 Intermediate	OOP pillars, dunder methods, encapsulation
4	API Logger & Rate Limiter	🟡 Intermediate–Advanced	Decorators, closures, custom exceptions
5	Async Multi-Source Web Scraper	🔴 Advanced	asyncio, async context managers, async generators
6	Log Processing Pipeline	🔴 Advanced	threading vs multiprocessing, GIL, __slots__
🟢 Project 1: Command-Line Expense Tracker & CSV Exporter
Difficulty: Easy
Core Topics: Core Data Structures, File Handling, Error Handling, Custom Modules

The Blueprint
Build a CLI tool that lets a user log daily expenses with a category, amount, and date, then review a summary of spending.

The Twist
Split logic into a custom module (storage.py) dedicated entirely to file persistence.
Use context managers (with open(...)) so files are always safely closed, even on failure.
Wrap numeric input collection in try/except ValueError blocks — the program must never crash on a typo like "twenty bucks".
Skills Exercised
Lists & dictionaries for in-session state
while True menu loops with if/elif/else routing
Defensive input validation
Modular code organization (app.py imports storage.py)
🟢 Project 2: Advanced Multi-Criteria Text Analyzer
Difficulty: Easy to Intermediate
Core Topics: Type Casting, Control Flow, Functional Programming Tools, Regex

The Blueprint
Build a processor that ingests raw text (or an uploaded .txt file) and returns descriptive statistics: sentence count, word frequency, stop-word filtering, and more.

The Twist
No for loops allowed for core formatting logic. You must rely on:

map() and filter() for transformations
List and dictionary comprehensions
lambda functions for inline logic
The re module for sentence/word tokenization
Skills Exercised
Functional-style Python (declarative over imperative)
Regex pattern matching
Dynamic sorting of frequency dictionaries (sorted() with custom key=)
🟡 Project 3: Custom E-Commerce Cart Engine
Difficulty: Intermediate
Core Topics: OOP Pillars, Dunder Methods, Access Modifiers

The Blueprint
Build the backend logic for a shopping cart system supporting multiple product types and discount codes.

The Twist
Implement a Product base class, inherited by specialized subclasses like DigitalProduct and PhysicalProduct (polymorphism in action).
Protect sensitive attributes (e.g., __price) using name-mangled private attributes with controlled access via properties.
Implement dunder methods:
__len__ → returns total item quantity in the cart (not just number of unique products)
__str__ → renders a clean, human-readable cart summary
__getitem__ → allows indexing into the cart like a list
Skills Exercised
Inheritance & polymorphism
Encapsulation via private attributes and @property
Operator overloading through dunder methods
🟡 Project 4: API Request Logger & Rate Limiter Decorator
Difficulty: Intermediate to Advanced
Core Topics: Advanced Decorators, Custom Classes, Type Hinting

The Blueprint
Mock an API endpoint handler and build a decorator that restricts how frequently any given method can be invoked.

The Twist
Implement @rate_limit(max_per_minute=5) as either a class-based decorator or a closure-based decorator that maintains call-timestamp state across invocations.
On the 6th call within a 60-second window, raise a custom exception: RateLimitExceeded.
Add type hints throughout for method signatures and the decorator itself.
Skills Exercised
Decorators that accept arguments (decorator factories)
Stateful closures vs. stateful decorator classes (__call__)
Custom exception hierarchies
Basic metaprogramming & type annotations
🔴 Project 5: Async Multi-Source Web Scraper
Difficulty: Advanced
Core Topics: asyncio, aiohttp, Async Context Managers, Async Generators

The Blueprint
Build a scraper that concurrently pulls data from 3–5 different URLs simultaneously, without blocking on any single slow request.

The Twist
Schedule all scraping coroutines concurrently using asyncio.gather() or asyncio.create_task().
Use async context managers (async with) for connection handling via aiohttp.
Implement an async generator (async def ... yield) that streams parsed HTML fragments to a tracking class as each request resolves, rather than waiting for all requests to finish.
Skills Exercised
Coroutines and the event loop
Non-blocking I/O patterns
Async iteration (async for)
Real-world concurrency vs. sequential blocking requests
🔴 Project 6: Multi-Threaded/Multi-Process Log Processing Pipeline
Difficulty: Advanced
Core Topics: threading, multiprocessing, GIL Management, __slots__

The Blueprint
Build a pipeline that reads massive mock log files (hundreds of thousands of lines), detects anomalies, and aggregates metrics.

The Twist
Use __slots__ in your log record classes to reduce per-instance memory overhead.
Build two parallel implementations:
A multi-threaded version for the I/O-bound file-reading stage
A multi-processing version for the CPU-bound text-parsing/aggregation stage
Profile and compare execution time between the two to directly observe how the Global Interpreter Lock (GIL) throttles CPU-bound threads but not I/O-bound ones.
Skills Exercised
threading.Thread / concurrent.futures.ThreadPoolExecutor
multiprocessing.Pool / ProcessPoolExecutor
Memory profiling and optimization
Empirical understanding of the GIL (not just theoretical)
📁 Suggested Repo Structure
text

python-mastery-roadmap/
│
├── 01_expense_tracker/
│   ├── storage.py
│   ├── app.py
│   └── expenses.csv
│
├── 02_text_analyzer/
│   ├── analyzer.py
│   └── sample_text.txt
│
├── 03_ecommerce_cart/
│   ├── products.py
│   ├── cart.py
│   └── main.py
│
├── 04_rate_limiter/
│   ├── decorators.py
│   ├── exceptions.py
│   └── mock_api.py
│
├── 05_async_scraper/
│   ├── scraper.py
│   ├── tracker.py
│   └── requirements.txt
│
├── 06_log_pipeline/
│   ├── log_record.py
│   ├── threaded_reader.py
│   ├── multiprocess_parser.py
│   ├── benchmark.py
│   └── sample_logs/
│
└── README.md
🚀 How to Use This Roadmap
Don't skip the Twist. The constraint is the entire point — it's what forces the "correct" pattern instead of the quick hack.
Build sequentially. Project difficulty compounds; Project 6 assumes comfort with OOP from Project 3 and decorators from Project 4.
Refactor backwards. Once you finish Project 4, go back and add a @log_execution_time decorator to Project 1. Once you finish Project 6, consider converting Project 5's scraper to use __slots__ too.
Profile everything in Projects 5 & 6. Use time.perf_counter(), cProfile, or asyncio's built-in debug mode to measure the concurrency gains rather than assuming them.
Requirements
Bash

pip install aiohttp  # Required for Project 5
All other projects use only the Python standard library — no external dependencies needed.

