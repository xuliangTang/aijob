import sys,os
# sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__), '../../')))
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from spider.list import listjob_by_keyword
from utils.llm import qwen
from utils.helper import load_prompt_file

def test():
    llm = qwen()
    prompt_tpl = load_prompt_file()
    prompt = PromptTemplate.from_template(prompt_tpl)

    chain = ({"job_list":RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser())
    ret = chain.invoke(listjob_by_keyword("golang"))
    print(ret)

if __name__ == '__main__':
    test()