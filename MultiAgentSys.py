import os
from dotenv import load_dotenv
from groq import Groq
from crewai import Agent, Task, Crew, Process
from tkinter import*
from tkinter import scrolledtext


load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")


client=Groq(api_key=groq_api_key)


def query_groq(prompt):
    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}],
        max_tokens=300,
    )
    return response.choices[0].message.content


researcher=Agent(
    role="AI Research Analyst",
    goal="Analyze and summarize the latest trends in AI.",
    backstory="Expert at condensing research papers and identifying key takeawys.",
    verbose=True,
    allow_delegation=False,
)
 
writer=Agent(
    role="Technical Writer",
    goal="Convert the researcher's insights into clear and engaging text.",
    backstory="Experienced writer specialized in AI and emerging technologies.",
    verbose=True,
    allow_delegation=False,
)

reviewer=Agent(
    role="Peer Reviewer",
    goal="Review and refine the final report for accuracy and coherence.",
    backstory="Senior reviewer ensuring logical flow and correctness in AI content.",
    verbose=True,
    allow_delegation=False,
)

task1=Task(description="Research latest AI trends in 2025.", agent=researcher, expected_output="A detailed summary")
task2=Task(description="Write a technical overview based on the research.", agent=writer, expected_output="A professional article.")
task3=Task(description="Review and finalize the article.", agent=reviewer, expected_output="Polished and approved report")

#Define Crew
crew=Crew(
    agents=[researcher, writer, reviewer],
    tasks=[task1, task2, task3],
    process=Process.sequential,
    verbose=True
)

#----------------------Tkinter GUI--------------------
root=Tk()
root.title("AI Multi-Agent System(CrewAI+Groq)")
root.geometry("800x600")

Label(root, text="Enter a Topic:", font=("Arial", 14)).pack(pady=10)
topic_entry=Entry(root, width=60, font=("Arial", 12))
topic_entry.pack(pady=10)


output_area=scrolledtext.ScrolledText(root, wrap=WORD, width=90, height=25, font=("Consolas", 10))
output_area.pack(padx=10, pady=10)

def run_agents():
    topic=topic_entry.get()
    if not topic:
        output_area.insert(END, "Please enter a topic first.\n")
        return
    

    output_area.insert(END, f"Starting multi-agent collaboration on: {topic}\n\n")


    #Run through Groq model as helper+CrewAI process
    ai_summary=query_groq(f"Summarize key research points on: {topic}")
    output_area.insert(END, f"Groq Summary:\n{ai_summary}\n\n")


    crew_result=crew.kickoff()
    output_area.insert(END, f"CrewAI Output:\n{crew_result}\n\n")
    output_area.insert(END, "Process Completed.\n\n")

Button(root, text="Run Agents", font=("Arial", 13), bg="green", fg="white", command=run_agents).pack(pady=10)
root.mainloop()