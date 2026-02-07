# Learning Python Object-Oriented

Based on "Learning Python Object-Oriented" at https://github.com/vanHeemstraSystems/learning-python-object-oriented

Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications and computer programs. This repository provides a systematic approach to mastering OOP concepts in Python, from fundamental principles to advanced design patterns.

## Executive Summary

This learning repository covers Python's object-oriented programming features, focusing on classes, inheritance, polymorphism, encapsulation, and design patterns. It provides practical examples and exercises for building robust, maintainable Python applications using OOP principles.

## Table of Contents

- [100 - Introduction to OOP](#100---introduction-to-oop)
- [200 - Classes and Objects](#200---classes-and-objects)
- [300 - Encapsulation](#300---encapsulation)
- [400 - Inheritance](#400---inheritance)
- [500 - Polymorphism](#500---polymorphism)
- [600 - Abstraction](#600---abstraction)
- [700 - Magic Methods (Dunder Methods)](#700---magic-methods-dunder-methods)
- [800 - Design Patterns](#800---design-patterns)
- [900 - Best Practices](#900---best-practices)

## Directory Structure

```
learning-python-object-oriented/
├── README.md
├── 100/
│   ├── README.md
│   ├── 100-oop-concepts.md
│   ├── 200-procedural-vs-oop.md
│   ├── 300-benefits-of-oop.md
│   └── examples/
│       └── basic_comparison.py
├── 200/
│   ├── README.md
│   ├── 100-defining-classes.md
│   ├── 200-creating-objects.md
│   ├── 300-instance-attributes.md
│   ├── 400-class-attributes.md
│   ├── 500-methods.md
│   ├── 600-constructors.md
│   └── examples/
│       ├── simple_class.py
│       ├── class_vs_instance.py
│       └── constructor_examples.py
├── 300/
│   ├── README.md
│   ├── 100-access-modifiers.md
│   ├── 200-properties.md
│   ├── 300-getters-setters.md
│   ├── 400-data-hiding.md
│   └── examples/
│       ├── private_attributes.py
│       ├── property_decorator.py
│       └── encapsulation_demo.py
├── 400/
│   ├── README.md
│   ├── 100-single-inheritance.md
│   ├── 200-multiple-inheritance.md
│   ├── 300-method-resolution-order.md
│   ├── 400-super-function.md
│   ├── 500-composition-vs-inheritance.md
│   └── examples/
│       ├── basic_inheritance.py
│       ├── multiple_inheritance.py
│       ├── mro_examples.py
│       └── composition_example.py
├── 500/
│   ├── README.md
│   ├── 100-method-overriding.md
│   ├── 200-operator-overloading.md
│   ├── 300-duck-typing.md
│   └── examples/
│       ├── polymorphic_methods.py
│       ├── operator_examples.py
│       └── duck_typing_demo.py
├── 600/
│   ├── README.md
│   ├── 100-abstract-classes.md
│   ├── 200-interfaces.md
│   ├── 300-abc-module.md
│   └── examples/
│       ├── abstract_base_class.py
│       ├── protocol_example.py
│       └── interface_implementation.py
├── 700/
│   ├── README.md
│   ├── 100-init-and-new.md
│   ├── 200-str-and-repr.md
│   ├── 300-comparison-methods.md
│   ├── 400-container-methods.md
│   ├── 500-context-managers.md
│   └── examples/
│       ├── lifecycle_methods.py
│       ├── string_representation.py
│       ├── comparison_examples.py
│       ├── container_class.py
│       └── context_manager.py
├── 800/
│   ├── README.md
│   ├── 100-singleton.md
│   ├── 200-factory.md
│   ├── 300-observer.md
│   ├── 400-decorator-pattern.md
│   ├── 500-strategy.md
│   ├── 600-adapter.md
│   └── examples/
│       ├── singleton_pattern.py
│       ├── factory_pattern.py
│       ├── observer_pattern.py
│       ├── decorator_pattern.py
│       ├── strategy_pattern.py
│       └── adapter_pattern.py
├── 900/
│   ├── README.md
│   ├── 100-solid-principles.md
│   ├── 200-code-organization.md
│   ├── 300-testing-oop.md
│   ├── 400-documentation.md
│   └── examples/
│       ├── solid_examples.py
│       ├── project_structure.py
│       └── test_examples.py
└── exercises/
    ├── README.md
    ├── beginner/
    ├── intermediate/
    └── advanced/
```

## 100 - Introduction to OOP

Foundational concepts of object-oriented programming and its advantages over procedural programming.

**Key Topics:**
- OOP paradigm fundamentals
- Four pillars: Encapsulation, Inheritance, Polymorphism, Abstraction
- Comparison with procedural programming
- Real-world modeling with objects

## 200 - Classes and Objects

Understanding the building blocks of OOP: classes as blueprints and objects as instances.

**Key Topics:**
- Class definition syntax
- Object instantiation
- Instance vs. class attributes
- Instance, class, and static methods
- `__init__()` constructor
- `self` parameter

## 300 - Encapsulation

Data hiding and controlled access to object attributes.

**Key Topics:**
- Public, protected, and private attributes (naming conventions)
- Property decorators (`@property`, `@setter`, `@deleter`)
- Getter and setter methods
- Data validation and integrity
- Name mangling

## 400 - Inheritance

Reusing and extending existing code through inheritance relationships.

**Key Topics:**
- Single inheritance
- Multiple inheritance
- Method Resolution Order (MRO)
- `super()` function
- Overriding methods
- Composition vs. inheritance trade-offs

## 500 - Polymorphism

Writing flexible code that works with objects of different types.

**Key Topics:**
- Method overriding
- Operator overloading
- Duck typing
- Type hints and protocols
- Runtime polymorphism

## 600 - Abstraction

Defining interfaces and abstract base classes for consistent implementation.

**Key Topics:**
- Abstract Base Classes (ABC)
- `abc` module
- `@abstractmethod` decorator
- Protocols (PEP 544)
- Interface design

## 700 - Magic Methods (Dunder Methods)

Special methods that enable Python's built-in functionality for custom classes.

**Key Topics:**
- Object lifecycle: `__new__`, `__init__`, `__del__`
- String representation: `__str__`, `__repr__`
- Comparison operators: `__eq__`, `__lt__`, `__gt__`, etc.
- Container emulation: `__len__`, `__getitem__`, `__setitem__`
- Context managers: `__enter__`, `__exit__`
- Callable objects: `__call__`

## 800 - Design Patterns

Common, reusable solutions to recurring design problems.

**Key Topics:**
- Creational: Singleton, Factory, Builder
- Structural: Adapter, Decorator, Facade
- Behavioral: Observer, Strategy, Command
- Python-specific implementations

## 900 - Best Practices

Professional standards for writing maintainable OOP code.

**Key Topics:**
- SOLID principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion)
- Code organization and module structure
- Unit testing OOP code
- Documentation and docstrings
- Type hints and mypy

## Prerequisites

- Python 3.8 or higher
- Basic Python knowledge (variables, functions, control flow)
- Understanding of data structures (lists, dictionaries, sets)
- Text editor or IDE (VS Code, PyCharm, etc.)

## Getting Started

1. Clone this repository:
```bash
git clone https://github.com/vanHeemstraSystems/learning-python-object-oriented.git
cd learning-python-object-oriented
```

2. Set up a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -r requirements.txt
```

4. Start with section 100 and progress sequentially through the materials.

## Learning Path

### Beginner Track (Weeks 1-2)
- Complete sections 100-300
- Focus on understanding classes, objects, and encapsulation
- Practice with exercises in `exercises/beginner/`

### Intermediate Track (Weeks 3-4)
- Work through sections 400-600
- Master inheritance, polymorphism, and abstraction
- Complete `exercises/intermediate/`

### Advanced Track (Weeks 5-6)
- Study sections 700-900
- Implement design patterns
- Apply SOLID principles
- Tackle `exercises/advanced/`

## Practical Applications

- Building reusable libraries and frameworks
- Creating REST API models with FastAPI/Flask
- Django models and ORM
- Game development with Pygame
- Data modeling and domain-driven design
- Test automation frameworks

### Featured Example: FastAPI with OOP

A comprehensive, production-ready example demonstrating OOP patterns in FastAPI:

- **File:** `fastapi_oop_example.py`
- **Documentation:** `FASTAPI_README.md`
- **Tests:** `test_fastapi_oop.py`

**Patterns demonstrated:**
- Repository Pattern (data abstraction)
- Service Layer Pattern (business logic)
- Dependency Injection (FastAPI DI)
- Singleton Pattern (shared resources)
- Domain Models (rich entities)
- Pydantic Validation (type safety)

**Run the example:**
```bash
pip install -r requirements-fastapi.txt
python fastapi_oop_example.py
# Visit http://localhost:8000/docs for interactive API
```

This example shows how to build a scalable, maintainable REST API using proper OOP principles. Perfect for learning how OOP concepts translate to real-world applications.

## Related Resources

- **Official Python Documentation**: https://docs.python.org/3/tutorial/classes.html
- **Real Python OOP Tutorials**: https://realpython.com/python3-object-oriented-programming/
- **Design Patterns in Python**: https://refactoring.guru/design-patterns/python
- **Clean Code in Python** by Mariano Anaya
- **Fluent Python** by Luciano Ramalho

## Integration with Other Learning Repositories

This repository complements:
- **learning-python**: Core Python fundamentals
- **learning-python-testing**: Testing OOP code with pytest
- **learning-design-patterns**: Language-agnostic pattern concepts
- **learning-clean-code**: Code quality principles

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add examples or improve documentation
4. Submit a pull request

Follow the existing structure and naming conventions.

## Code Smell Detective Integration

Apply Code Smell Detective principles to identify:
- **God Objects**: Classes with too many responsibilities
- **Feature Envy**: Methods that use other classes' data excessively
- **Inappropriate Intimacy**: Classes that access each other's internals
- **Refused Bequest**: Subclasses that don't use inherited methods
- **Lazy Class**: Classes that don't do enough to justify existence

## Progress Tracking

- [ ] Section 100: Introduction completed
- [ ] Section 200: Classes and Objects completed
- [ ] Section 300: Encapsulation completed
- [ ] Section 400: Inheritance completed
- [ ] Section 500: Polymorphism completed
- [ ] Section 600: Abstraction completed
- [ ] Section 700: Magic Methods completed
- [ ] Section 800: Design Patterns completed
- [ ] Section 900: Best Practices completed
- [ ] All exercises completed
- [ ] Final project: Build a complete OOP application

## License

MIT License - see LICENSE file for details

## Acknowledgments

Built on industry best practices and Python community standards. Special thanks to the Python Software Foundation and the broader Python education community.

---

**Part of the vanHeemstraSystems learning repository collection**

*Systematic learning through structured documentation and hands-on practice*
