import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

OPENAI_API_KEY = None
llm = None

def init_env():
    '''
    @param: None
    @return: None
    @description: This function is used to initialize the environment by loading the .env file and setting the OPENAI_API_KEY.
    '''
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # TODO: We should require the user to set their own .env file with the OPENAI_API_KEY
    if not OPENAI_API_KEY:
        # raise ValueError("OPENAI_API_KEY is not set")
        print("OPENAI_API_KEY is not set in the .env file")        

    return OPENAI_API_KEY
    

def llm_init(model = str('gpt-3.5-turbo'), temperature = float(0.1)):
    '''
    @param: model: str
    @param: temperature: float
    @return: llm
    @description: This function is used to initialize the LLM configuration.
    '''
    OPENAI_API_KEY = init_env()

    # print("model: ", model)
    # print("temperature: ", temperature)
    # print("OPENAI_API_KEY: ", OPENAI_API_KEY)    

    if not OPENAI_API_KEY:
      llm = ChatOpenAI(model, temperature=temperature)  
      return llm

    llm = ChatOpenAI(model=model, temperature=temperature, openai_api_key=OPENAI_API_KEY)
    return llm
    
