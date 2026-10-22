# Reflection Agent

A beginner-friendly Python project demonstrating the reflection pattern in an agent workflow.

## Overview

The program generates an initial response, evaluates it using a simple rule-based check, and revises the response if it does not meet the required criteria.

## How It Works

1. Generates an initial response.
2. Checks whether the response meets a minimum word count.
3. Revises the response if it fails the check.
4. Retries up to a maximum of three attempts.
5. Displays the final result and its evaluation status.

## Features

- Rule-based response evaluation
- Automatic revision attempts
- Maximum retry limit
- Simple Python implementation

## Technologies Used

- Python
- Basic functions, loops, and conditional statements

## How to Run

```bash
python main.py
```

## Note

This is a beginner-level simulation of an agent reflection workflow. It does not use an LLM or an external AI API.