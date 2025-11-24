Project Explanation: How the Multi-Agent System was Built and How It Works
This project is a Multi-Agent AI System created using the CrewAI framework and the Groq API.
It demonstrates how different intelligent agents can collaborate to perform a task — each agent has a specific role (like Researcher, Writer, and Editor), and they work together in sequence.
How the Project Was Built (Step-by-Step Explanation)
Environment Setup
Installed required libraries using pip:
pip install crewai crewai-tools python-dotenv
Created a .env file to securely store API keys:
GROQ_API_KEY=your_api_key_here
SERPER_API_KEY=your_api_key_here
Agent Design (Using CrewAI)
Imported Agent, Task, and Crew from the crewai library.
Created multiple agents with unique roles:
Researcher Agent → Searches for and gathers relevant data using the SerperDevTool.
Writer Agent → Takes the research results and writes a detailed, structured summary.
Editor Agent → Reviews and refines the final content for clarity and accuracy.
Task Assignment
Each agent was assigned a Task (what to do and what output to generate).
Tasks were connected together in a logical flow so that the output of one agent becomes the input for the next.
Crew Formation
Used the Crew class to combine all agents and their tasks into a single workflow.
The process mode was set to sequential, meaning each agent performs their part one after another.
Running the System
Created a main Python file, MultiAgentSys.py.
When the file runs, the Crew automatically executes all agents and shows the final result in the terminal.
How to Run the Project
Open the project folder in VS Code or any IDE.
Make sure Python 3.10+ is installed.
In the terminal, run:
pip install -r requirements.txt
(or manually install: pip install crewai crewai-tools python-dotenv)
Create a .env file and add your API keys:
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_serper_api_key_here
Finally, run the project with:
python MultiAgentSys.py
The system will:
Activate all agents one by one
Perform research
Write a report
Edit and finalize the output
Then display the final combined response in your terminal
In Summary
Component	Description
Framework	CrewAI (for multi-agent orchestration)
LLM API	Groq
Search Tool	SerperDevTool
Language	Python
Design Type	Object-oriented, Modular
Purpose	: Demonstrate multi-agent collaboration workflow
Key Learning Points
Practical use of multi-agent orchestration
Integration of external LLM APIs
Performance Evaluation
This section outlines how the system was tested and how its performance compares to baseline approaches.
1. Testing Methodology
Functional testing for each agent
End-to-end pipeline testing
Error-handling validation
Stress-testing with large inputs
2. Metrics Used
Response time (ms)
Accuracy of generated summaries
Relevance score (manual + automated)
System robustness under invalid inputs
3. Baseline Comparison
The system was evaluated against:
Standard single-agent summarizers
GPT-style single-output pipelines
Findings:
The multi-agent architecture showed:
Higher clarity
Better structured summaries
Reduced hallucination
More accurate contextual insights
4. Limitations & Future Work
Add automated evaluation scripts
Include more benchmarking datasets
Improve agent coordination
Add model performance dashboard
Implementation of a collaborative AI workflow
Secure management of API keys using the .env file

Understanding CrewAI process flow from task creation to final output
