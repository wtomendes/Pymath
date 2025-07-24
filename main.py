#!/usr/bin/env python3
"""
Pymath - A fun calculator with sound effects and easter eggs.

This is the main entry point for the Pymath calculator application.
"""

from src.calculator import PymathCalculator


def main():
    """Main function to run the Pymath calculator."""
    calculator = PymathCalculator()
    calculator.run()


if __name__ == "__main__":
    main()