#!/bin/bash

cd "$(dirname "$0")"

echo "Installing Python dependencies..."

if ! command -v python3 &> /dev/null
then
    echo "Python3 not found. Install Python3 first."
    exit 1
fi

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "Done."