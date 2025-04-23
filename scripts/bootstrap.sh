#!/bin/bash
echo "📦 Setting up environment..."

# Create virtualenv
python3 -m venv venv
source venv/bin/activate

# Upgrade pip and install deps
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ All dependencies installed and environment ready."
