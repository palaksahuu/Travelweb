from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import StructuredOutputParser

from langchain_community.chat_models import ChatOpenAI

itinerary_prompt = ChatPromptTemplate.from_messages([
    ("system", """Create detailed itinerary for {destination} from {start_date} to {end_date}.
Budget: {budget}. Style: {travel_style}. Preferences: {preferences}.
Include:
1. Time-specific activities with durations
2. Logical geographic grouping
3. Transportation options
4. Cost estimates"""),
])

def generate_itinerary(request, activities):
    parser = StructuredOutputParser.from_response_schemas([

    ])
    
    chain = itinerary_prompt | ChatOpenAI() | parser
    return chain.invoke({
        **request.dict(),
        "activities": activities
    })