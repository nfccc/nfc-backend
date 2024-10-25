#!/bin/bash

# Check if 'pip' command exists, if not, use 'pip3'
if command -v pip >/dev/null 2>&1; then
    PIP=pip
elif command -v pip3 >/dev/null 2>&1; then
    PIP=pip3
else
    echo "Error: 'pip' command not found."
    exit 1
fi

# Check if 'python' command exists, if not, use 'python3'
if command -v python >/dev/null 2>&1; then
    PYTHON=python
elif command -v python3 >/dev/null 2>&1; then
    PYTHON=python3
else
    echo "Error: 'python' command not found."
    exit 1
fi

# Install dependencies
$PIP install -r requirements.txt

# Run Django's collectstatic command
$PYTHON manage.py collectstatic --noinput

# Apply database migrations
$PYTHON manage.py migrate
