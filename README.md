# AI Trip Advisor – Multi-Agent Travel Planning with CrewAI

This project is an experimental AI-powered travel advisor that utilizes Generative AI and a multi-agent system with CrewAI to create personalized travel recommendations. The system considers user preferences, budget constraints, and travel goals to provide optimized itineraries.
## Features

    Multi-Agent Collaboration: Different AI agents specialize in research, planning, profiling, and budgeting.

    Web Scraping & Search Integration: Uses tools to fetch real-time travel data.

    Customizable Inputs: User can specify their travel preferences, destination, and budget.

    Future Plans: A Streamlit-based frontend will be added for a more interactive experience.

## Project Workflow

1️⃣ Agents

| Agent Name          | Role                      | Goal                                                   |
|---------------------|--------------------------|--------------------------------------------------------|
| Destiny Researcher | Travel Destination Expert | Find the best travel options based on user preferences. |
| Traveler Profiler  | User Analysis Specialist  | Understand traveler needs, constraints, and preferences. |
| Itinerary Planner  | Travel Planner            | Create optimized itineraries for the trip.             |
| Budget Advisor     | Financial Optimizer       | Optimize trip costs while maintaining a great experience. |


2️⃣ Tasks 

| Task Name       | Description                                    | Assigned Agent        |
|----------------|------------------------------------------------|-----------------------|
| Research Task  | Research destinations matching the user’s interests. | Destiny Researcher    |
| Profile Task   | Generate a detailed traveler profile.          | Traveler Profiler     |
| Planning Task  | Build a day-by-day travel itinerary.           | Itinerary Planner     |
| Budget Task    | Optimize travel costs for the proposed itinerary. | Budget Advisor       |



3️⃣ Tools

| Tool              | Description                                      |
|------------------|--------------------------------------------------|
| SerperDevTool    | Search tool for retrieving relevant travel information. |
| ScrapeWebsiteTool | Scrapes real-time data from travel websites.    |

## Tech Stack

    Python
    CrewAI – Multi-agent framework
    LangChain & OpenAI – LLM-powered reasoning
    LiteLLM – Model aliasing for efficient API usage
    Streamlit - For a easy front-end

## How It Works

1️⃣ The user provides travel preferences, destination, and constraints.

2️⃣ Agents work together to:

Research ideal destinations

Profile the traveler

Create an optimized itinerary

Suggest a cost-effective budget

3️⃣ The CrewAI system executes the tasks and returns a complete travel plan.

## Running the Project

1️⃣ Install Dependencies

    pip install -r requirements.txt

2️⃣ Set Environment Variables

Create a config.json or modify config.py with:

    {
        "OPENAI_API_KEY": "",
        "MODEL": "",
        "SERPER_API_KEY": ""
    }


3️⃣ Run the Script

    streamlit run front.py

## Roadmap

Multi-Agent System
Travel Research & Planning
Streamlit UI for User Interaction
More Advanced Budgeting & Real-Time Flight/Hotel Data

Lucas Larcher (lucas.o.larcher@gmail.com)
