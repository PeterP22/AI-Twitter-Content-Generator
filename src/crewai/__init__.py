import os
from crewai import Agent, Task, Crew, Process

os.environ["OPENAI_API_KEY"] = "PUT YOUR KEY HERE"

from langchain.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()

# Define the agents
# 1. Research Agent: Gathers data, statistics, and professional advice about foam rolling.
research_agent = Agent(
  role='Health and Fitness Research Analyst',
  goal='Conduct thorough and in-depth research on foam rolling, focusing on detailed statistics, scientific studies, expert advice, benefits, and tips.',
  backstory="""You are a meticulous researcher specializing in health and fitness. 
  Your role involves diving deep into academic papers, fitness reports, and expert analyses to extract detailed insights, statistical data, benefits, and practical tips on foam rolling.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool]
)

research_task = Task(
  description="""Perform comprehensive and in-depth research on foam rolling. 
  Extract detailed statistics, analyze scientific studies, gather expert advice, note significant benefits, and compile practical tips. 
  Provide substantial, quantifiable, and well-referenced data to support the insights. Ensure the inclusion of references and data sources.""",
  agent=research_agent
)


# 2. Content Creation Agent: Creates informative and engaging content based on research.
content_creation_agent = Agent(
  role='Health and Fitness Content Creator',
  goal='Craft informative, detailed, and engaging posts for social media, incorporating in-depth research findings, statistics, references to studies, benefits, and tips about foam rolling.',
  backstory="""You are a creative content creator, skilled in turning comprehensive research information into clear, compelling narratives. 
  Your expertise lies in synthesizing in-depth research into concise, impactful social media content that resonates with health-conscious audiences, ensuring the inclusion of statistical data and references.""",
  verbose=True,
  allow_delegation=True,
)

content_creation_task = Task(
  description="""Utilize the in-depth research findings to create informative, detailed, and engaging posts about foam rolling. 
  Each post should be rich in content, providing value through detailed facts, statistics, referenced studies, benefits, and practical tips. 
  Ensure clarity, conciseness, and the inclusion of quantitative data and studies, making complex information accessible and engaging.""",
  agent=content_creation_agent
)


# 3. Review & Editing Agent: Ensures the quality and effectiveness of the content.
review_agent = Agent(
  role='Content Reviewer and Editor',
  goal='Review and refine the content to ensure accuracy, detail, engagement, and adherence to platform standards, including the verification of references and data.',
  backstory="""You are a detail-oriented reviewer and editor, ensuring that every piece of content is polished, accurate, and impactful. 
  Your role involves fine-tuning the content to meet the highest standards of quality and effectiveness, with a particular focus on the depth of information, accuracy of data, and proper citation of sources.""",
  verbose=True,
  allow_delegation=True,
)

review_task = Task(
  description="""Review the content created by the Content Creation Agent. Ensure the accuracy of the information, the depth of the content, the appeal of the presentation, and the clarity of the message. 
  Verify the inclusion of detailed statistics, referenced studies, and quantifiable data. Refine the content to make it engaging, informative, and compliant with the standards of the intended social media platform.""",
  agent=review_agent
)


# Instantiate the crew with a sequential process
crew = Crew(
  agents=[research_agent, content_creation_agent, review_agent],
  tasks=[research_task, content_creation_task, review_task],
  verbose=2, # You can set it to 1 or 2 for different logging levels
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
