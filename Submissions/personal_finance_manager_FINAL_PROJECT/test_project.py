import pytest
import os
import json
from project import add_transaction, view_transactions, generate_report

# Sample transactions data for testing
sample_transactions = [
    {"amount": 1000, "category": "Salary", "date": "2023-06-01", "description": "June Salary"},
    {"amount": 200, "category": "Food", "date": "2023-06-02", "description": "Groceries"},
    {"amount": 300, "category": "Rent", "date": "2023-06-03", "description": "June Rent"}
]

# Helper function to write sample transactions to file
def write_sample_transactions():
    with open('transactions.json', 'w') as file:
        json.dump(sample_transactions, file)

# Test for add_transaction function
def test_add_transaction(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '100')
    monkeypatch.setattr('builtins.input', lambda _: 'Entertainment')
    monkeypatch.setattr('builtins.input', lambda _: '2023-06-04')
    monkeypatch.setattr('builtins.input', lambda _: 'Movie Ticket')

    add_transaction()

    with open('transactions.json', 'r') as file:
        transactions = json.load(file)

    assert len(transactions) == 1
    assert transactions[0]['category'] == 'Entertainment'
    os.remove('transactions.json')

# Test for view_transactions function
def test_view_transactions(capsys):
    write_sample_transactions()

    view_transactions()
    captured = capsys.readouterr()

    assert "Salary" in captured.out
    assert "Groceries" in captured.out
    assert "June Rent" in captured.out
    os.remove('transactions.json')

# Test for generate_report function
def test_generate_report(capsys):
    write_sample_transactions()

    generate_report()
    captured = capsys.readouterr()

    assert "Salary: 1000" in captured.out
    assert "Food: 200" in captured.out
    assert "Rent: 300" in captured.out
    os.remove('transactions.json')
