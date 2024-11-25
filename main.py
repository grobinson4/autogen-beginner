import os
import autogen
from autogen import AssistantAgent, UserProxyAgent

def main():
    config_list = autogen.config_list_from_json(
        env_or_file="OAI_CONFIG_LIST.json"
    )

    assistant = AssistantAgent(
        name="Assistant",
        llm_config={
            "config_list": config_list
        }
    )

    user_proxy = UserProxyAgent(
        name="user",
        human_input_mode="NEVER",
        code_execution_config={
            "executor": autogen.coding.LocalCommandLineCodeExecutor(work_dir="coding"),
            "user_docker": False
        }
    )

    user_proxy.initiate_chat(assistant, message="Plot a chart of META and TESLA stock price change.")

    if __name__ == "__main__":
        main()