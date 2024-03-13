""" Example script to interact with the Agent class """

import os

import yaml
import click

import neosophia.agents.utils as autils

from examples import project

from neosophia.db import sqlite_utils as sql_utils
from neosophia.llmtools import openaiapi as oaiapi
from neosophia.agents.agent import Agent
from neosophia.agents.data_classes import Variable
from neosophia.agents.system_prompts import PARAM_AGENT_BP, TOOL_AGENT_BP
import psycopg2

opj = os.path.join

os.environ.setdefault('BOT_TOKEN','6833712512:AAEF7MuxIhqZAYxQiuPr7lrasid2W8CWv3g')
os.environ.setdefault('DB_USERNAME','postgres_ro')
os.environ.setdefault('DB_PASSWORD','password')
os.environ.setdefault('DB_NAME','VyttahAccounting')
os.environ.setdefault('DB_URL','vyttah-database.ceu03herukvs.us-east-1.rds.amazonaws.com')
os.environ.setdefault('OPENAI_API_BASE','http://localhost:11434/v1')
os.environ.setdefault('OPENAI_API_KEY','ollama')

def get_database_connection():
    # Retrieve database credentials from environment variables
    db_user = os.environ.get("DB_USERNAME")
    db_password = os.environ.get("DB_PASSWORD")
    db_host = os.environ.get("DB_URL")

    # Use DB_PORT as a string, and no need for explicit conversion
    db_port = 5432

    db_name = os.environ.get("DB_NAME")

    # Create a database connection string
    connection_string = (
        f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    # Establish a connection to the database using SQLAlchemy
    # engine = create_engine(connection_string)

    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    return conn


@click.command()
@click.option("--toggle", "-t", is_flag=True, help="Toggle variables")
def main(toggle):
    """main"""
    print("\n")

    oaiapi.set_api_key(oaiapi.load_api_key(project.OPENAI_API_KEY_FILE_PATH))

    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    # Create a workspace for the agent to save things
    workspace_dir = autils.create_workspace_dir(config)

    # Load and/or generate tools
    tools_filepath = opj(workspace_dir, config["Agent"]["tools_filename"])
    tool_descriptions = autils.setup_and_load_yaml(tools_filepath, "tools")
    tools = autils.setup_tools(config["Tools"], tool_descriptions)
    autils.save_tools_to_yaml(tools, tools_filepath)

    # Dictionary to store all variables the Agent has access to
    variables = {}

    # Put all data from databases into Pandas DataFrame Variables
    for db_info in config["Resources"]["SQLite"]:
        # conn = sql_utils.get_conn(db_info["path"])
        conn = get_database_connection()

        name = os.environ.get("DB_NAME")
        tables = sql_utils.get_tables_from_postgres(conn)

        for table in tables:

            # Don't include system tables
            if table in ["sqlite_master", "sqlite_sequence"]:
                continue

            data = sql_utils.execute_query_pd(conn, f"SELECT * FROM {table};")

            description = f"All data from the {table} {table} in database {name}\n"
            variable = Variable(
                name=f"{table}_data", value=data, description=description
            )

            variables[f"{table}_data"] = variable

    agent_base_prompt = TOOL_AGENT_BP
    agent = Agent(
        workspace_dir, TOOL_AGENT_BP, PARAM_AGENT_BP, tools, variables, toggle=toggle
    )
    agent.chat()


if __name__ == "__main__":
    main()
