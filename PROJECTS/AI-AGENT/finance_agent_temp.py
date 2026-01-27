from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools

load_dotenv()


def get_company_symbol(company):
    symbols = {"Microsoft": "MSFT", "Tesla": "TSLA", "Apple": "AAPL"}
    return symbols.get(company, "Unknown")


finance_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(
            analyst_recommendations=True,
            stock_fundamentals=True,
            key_financial_ratios=True,
        ),
        get_company_symbol,
    ],
    instructions=[
        "Use tables to display data",
        "If you need to find the symbol for a company, use get_company_symbol tool",
    ],
    # description="You are an expert stock analyst",
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

finance_agent.print_response(
    "Summarize and compare analyst recommendations and fundamentals for Microsoft and Tesla.",
    stream=True,
)
