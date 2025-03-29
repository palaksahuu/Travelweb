from langchain.prompts import ChatPromptTemplate

from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
import os


clarification_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a travel assistant. When user provides:
{draft_input}, identify missing/ambiguous info from: 
1. Exact dates 2. Budget range 3. Activity types 
Ask ONE most critical question to clarify."""),
])


async def clarify_inputs(request):
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        openai_api_key=os.getenv("OPENAI_API_KEY")  
    )
  
    if any(word in request.preferences.lower() for word in ["mix", "some", "variety"]):
        response = await chain.ainvoke({
            "draft_input": request.preferences
        })
        return {"requires_clarification": response.content}
    
    return request
