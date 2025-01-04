from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

  
load_dotenv()

class Chain:
    def __init__(self):
        # Initialize the LLM with your API key
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")
    
    def answer_question(self, document, question):
        prompt = PromptTemplate.from_template(
        '''
        ### DOCUMENT CONTENT
        {document}
        ### QUESTION
        {question}
        ### INSTRUCTIONS
        Answer the question based on the document above. If the answer cannot be found, respond with "Answer not found."
        ### ANSWER
        '''
        )
        chain = prompt | self.llm
        #passes the formated prompt to the llm
        res = chain.invoke({"document": document, "question": question})
        return res.content
