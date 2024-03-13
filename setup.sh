#!/bin/bash
# Install miniconda
# echo "Installing Miniconda..."
# wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
# bash Miniconda3-latest-Linux-x86_64.sh

# Install Ollama
echo "Installing Ollama..."
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama server
echo "Starting Ollama server..."
nohup ollama serve > ollama.log 2>&1 &

# Pull from Mistral
echo "Pulling from Mistral..."
ollama pull mistral

# # Pull from Mixtral
# echo "Pulling from Mixtral..."
# ollama pull mixtral

echo "Ollama Installed and is Running"
