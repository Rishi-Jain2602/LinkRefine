from ..chain.llm import model
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from typing_extensions import Annotated, TypedDict

class Output(TypedDict):
    headline: Annotated[str, "Suggested headline for LinkedIn profile"]
    About: Annotated[str, "Suggested 'About' section for the user"]
    Work_exp: Annotated[str, "Suggested improvements for the work experience section"]
    Skills: Annotated[str, "Suggested skills to add"]
    Projects: Annotated[str, "Suggested improvements for projects section"]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
            You are provided with the LinkedIn user's headline, About section, work experience description,Projects and skills. Based on this information, suggest improvements to enhance their profile for better visibility and opportunities.

            If the user has multiple work experiences listed, offer suggestions for each one. If any sections are missing or incomplete, advise the user to fill them out for a stronger profile and give suggestions on what to add. 

            ### Response Format:
            - **headline**: Suggest an improved headline based on the user's work experience, projects, and skills.
            - **About**: Provide a stronger 'About' section based on the user's background and expertise.
            - **Work Experience**: Suggest ways the user can better present their work experience to attract recruiters.
            - **Skills**: Recommend additional skills the user should highlight to increase their opportunities.
            - **Projects**: Provide suggestions to better showcase technical projects and their impact
        """),
        ("human", "Headline:{headline}, About Section: {about}, Work Experience: {work_exp}, Projects: {projects} and Skills: {skills}. Please suggest me improvements to enhance my LinkedIn Profile")
    ]
)

def work_suggestion(headline, about, experiences, skills,projects):
    structured_llm = model.with_structured_output(Output)
    ExperienceDesc = ''
    # Iterate over the list of experiences from Apify
    for exp in experiences:
        title = exp.get("title", "")
        company = exp.get("subtitle", "")
        description_text = ""
        for comp in exp.get("subComponents", []):
            for d in comp.get("description", []):
                description_text += d.get("text", "") + " "
        ExperienceDesc += f"Title: {title}, Company Name: {company}, Description: {description_text} "
    
    projects_desc = ""
    for project in projects:
        title = project.get("title", "")
        description = ""
        for comp in project.get("subComponents", []):
            for d in comp.get("description", []):
                description += d.get("text", "") + " "
        projects_desc += f"Project: {title}, Details: {description.strip()} "
        

    response = structured_llm.invoke(prompt.format(
        headline=headline,
        about=about,
        work_exp=ExperienceDesc,
        skills=skills,
        projects=projects_desc
    ))
    return response
