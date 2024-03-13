### Capabilities approach
Trying the ScratchPad !
(Run this in command prompt)

### Clone the Repo
    git clone https://github.com/PromptEngineer48/neo-sophia.git

### Install the conda
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh

### Start up a conda env
    conda env create -f neo-sophia/env.yml
    conda activate neosophia
    
### install the neo-sophia libraries
    pip install -e neo-sophia
    cd neo-sophia
    
### Other housekeeping
    cp config_example.json config.json
    cp openai_api_key_example.txt openai_api_key.txt

### Ollama installation and Downloading Models
    bash setup.sh


## Episode 12 - Data too big for LLMs? Try Scratchpads
## Before running this, set the environment variables
    python -m examples.agent_example1

