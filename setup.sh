#!/bin/bash

# Install Ollama
echo "Installing Ollama..."
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama server
echo "Starting Ollama server..."
nohup ollama serve > ollama.log 2>&1 &

# Pull from Mixtral
echo "Pulling from Mixtral..."
ollama pull mixtral

echo "Ollama Installed and is Running"
