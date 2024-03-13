# Capabilities approach
Trying the ScratchPad


### Clone the Repo (Run this in command prompt)
    git clone https://github.com/PromptEngineer48/neo-sophia.git

### Install the conda (Run this in command prompt)
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh

### Start up a conda env (Run this in command prompt)
    conda env create -f neo-sophia/env.yml
    conda activate neosophia
    
### install the neo-sophia libraries
    !pip install -e neo-sophia
    %cd neo-sophia
### Other housekeeping
    %cp config_example.json config.json
    %cp openai_api_key_example.txt openai_api_key.txt


## Episode 12 - Data too big for LLMs? Try Scratchpads
````
    python -m examples.agent_example

````

