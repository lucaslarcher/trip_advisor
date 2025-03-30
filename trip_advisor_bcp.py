# Warning control
import warnings

warnings.filterwarnings('ignore')

from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import os
import litellm
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from config import load_config


def setup_travel_crew(inputs):
    # Configuração inicial
    config = load_config()
    os.environ["OPENAI_API_KEY"] = config["OPENAI_API_KEY"]
    os.environ["OPENAI_MODEL_NAME"] = config["MODEL"]
    os.environ["SERPER_API_KEY"] = config["SERPER_API_KEY"]
    llm = ChatOpenAI()

    litellm.model_aliases = {
        "gpt-4o": "openai/gpt-4o"
    }

    # Ferramentas
    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()

    # Agents
    destiny_researcher = Agent(
        role="Destiny Researcher",
        goal="Find the best travel options based on user preferences",
        tools=[scrape_tool, search_tool],
        verbose=True,
        backstory="Expert in finding hidden gems and best deals for travelers"
    )

    traveler_profiler = Agent(
        role="Traveler Profiler",
        goal="Understand deeply the traveler preferences and constraints",
        verbose=True,
        backstory="Specialist in creating detailed traveler profiles"
    )

    itinerary_planner = Agent(
        role="Itinerary Planner",
        goal="Create optimized travel itineraries",
        tools=[search_tool, scrape_tool],
        verbose=True,
        backstory="Master in crafting perfect travel schedules"
    )

    budget_advisor = Agent(
        role="Budget Advisor",
        goal="Optimize travel costs without compromising experience",
        tools=[search_tool],
        verbose=True,
        backstory="Financial wizard for travel planning"
    )

    # Tasks
    research_task = Task(
        description=f"Research destinations that match {inputs['travel_preferences']} and {inputs['destination']}",
        expected_output="List of potential destinations with pros and cons",
        agent=destiny_researcher
    )

    profile_task = Task(
        description=f"Create detailed traveler profile from {inputs['user_input']}",
        expected_output="Comprehensive traveler profile document",
        agent=traveler_profiler
    )

    planning_task = Task(
        description=f"Create day-by-day itinerary for {inputs['destination']}",
        expected_output="Detailed travel itinerary with activities",
        agent=itinerary_planner,
        context=[research_task, profile_task]
    )

    budget_task = Task(
        description="Optimize budget for the proposed itinerary",
        expected_output="Cost-optimized itinerary with budget breakdown",
        agent=budget_advisor,
        context=[planning_task]
    )

    # Crew
    travel_crew = Crew(
        agents=[destiny_researcher, traveler_profiler, itinerary_planner, budget_advisor],
        tasks=[research_task, profile_task, planning_task, budget_task],
        verbose=False
    )

    # Execution
    return travel_crew.kickoff(inputs=inputs)


if __name__ == "__main__":
    inputs = {
        'travel_preferences': 'street food, moderate budget, historical places, outdoor activities',
        'destination': 'Brazil, Minas Gerais',
        'user_input': 'Lucas, de 31 anos, planeja uma viagem em casal entre os dias 31 de março e 4 de abril de 2025. Ele ainda não possui passaporte e dispõe de um orçamento total de 10.000 reais, com uma flexibilidade moderada. Sua preferência de hospedagem é por hotéis que ofereçam comodidades como Wi-Fi e café da manhã incluso. Durante a viagem, ele tem interesse em atividades culturais, como visitar museus, sítios históricos e festivais locais. Também gosta de passeios ao ar livre, como caminhadas e natação, além de apreciar a culinária de rua. No momento das compras, pretende explorar lojas de souvenirs. Lucas fala português e inglês.'
    }

    result = setup_travel_crew(inputs)
    print(result)