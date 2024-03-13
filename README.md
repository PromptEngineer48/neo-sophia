# Capabilities approach
We advise our clients to take a capabilties-based approach when building their AI. That is, create foundational solutions that allow you to solve many different business use cases. Unfortunately too many teams begin solving specifing business problems withough building a generalizable foundation.


### Install the base neo-sophia code

    git clone https://github.com/prolego-team/neo-sophia.git
    conda env create -f neo-sophia/env.yml
    conda activate neosophia
    pip install -e neo-sophia
    cd neo-sophia
    cp config_example.json config.json
    cp openai_api_key_example.txt openai_api_key.txt



## Episode 12 - Data too big for LLMs? Try Scratchpads
LLMs cannot handle data bigger than their context windows. To overcome these limitations, use temporary memory called LLM Scratchpads.

1. Checkout Episode 12, [Release v0.12.0](https://github.com/prolego-team/neo-sophia/releases/tag/v0.12.0)
````
    git checkout tags/v0.12.0
````
2. Start the demo by running

````
    python -m examples.agent_example

````

