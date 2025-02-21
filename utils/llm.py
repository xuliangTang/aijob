from langchain_community.chat_models import ChatZhipuAI
from langchain_openai import ChatOpenAI
import os

def kimi():
    return ChatOpenAI(
        model = "moonshot-v1-8k",
        base_url = "https://api.moonshot.cn/v1",
        api_key = os.environ.get("llm_moonshot"),
    )

def qwen():
    return ChatOpenAI(
        model = "qwen-max-2025-01-25",
        base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1",
        api_key = os.environ.get("llm_qwen")
    )

def zhipu():
    return ChatZhipuAI(
        model = "glm-4-flash",
        base_url = "https://open.bigmodel.cn/api/paas/v4/chat/completions",
        api_key = os.environ.get("llm_zhipu"),
        temperature = 0.5
    )