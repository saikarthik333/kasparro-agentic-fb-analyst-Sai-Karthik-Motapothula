import json
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate 
from src.utils.prompt_utils import load_prompt
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class PlannerAgent:
    def __init__(self):
        # Initialize the LLM
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo",  # Using GPT-4 for better reasoning
            temperature=0,
            api_key=os.getenv("OPENAI_API_KEY")
        )
        self.prompt_template = load_prompt("planner_prompt.md")

    def create_plan(self, user_query: str):
        """
        Generates a plan based on the user query.
        """
        print(f"🧠 Planner is thinking about: '{user_query}'...")
        
        prompt = ChatPromptTemplate.from_template(self.prompt_template)
        chain = prompt | self.llm
        
        # Invoke the chain
        response = chain.invoke({"user_query": user_query})
        
        # Clean and Parse JSON
        try:
            content = response.content.strip()
            # Remove markdown code blocks if present
            if content.startswith("```json"):
                content = content[7:]
            if content.endswith("```"):
                content = content[:-3]
            
            plan = json.loads(content)
            return plan
        except json.JSONDecodeError:
            print(f"❌ Error parsing JSON from Planner. Raw output:\n{response.content}")
            # Fallback plan
            return {
                "steps": ["Fetch Data", "Analyze Trends", "Generate Report"],
                "reasoning": "Fallback due to parsing error."
            }

# Simple test block to run this file directly
if __name__ == "__main__":
    agent = PlannerAgent()
    plan = agent.create_plan("Analyze the performance drop in the 'Men ComfortMax' campaign.")
    print("\n📋 Generated Plan:")
    print(json.dumps(plan, indent=2))