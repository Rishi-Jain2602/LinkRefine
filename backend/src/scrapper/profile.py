import os
from dotenv import load_dotenv
from apify_client import ApifyClient
from ..routes.picture import profile_picture_optimizer
from ..routes.utils import work_suggestion
from ..routes.backgrd import backgrd_picture_optimizer
from ..Database.db import UserProfile_Suggestion_collection,UserData_collection
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

APIFY_TOKEN = os.environ['APIFY_TOKEN']
client = ApifyClient(APIFY_TOKEN)

def profile_optimizer(url, link_id):
    try:
        run_input = {"profileUrls": [url]}
        run = client.actor("2SyF0bVxmgGr8IVCZ").call(run_input=run_input)
        profiles = list(client.dataset(run["defaultDatasetId"]).iterate_items())
        if not profiles:
            logger.error("No profiles found for the provided URL.")
            return False
        profile_data = profiles[0]
    except Exception as e:
        logger.error(f"Apify API call failed: {str(e)}")
        return False

    UserData_collection.insert_one(profile_data)

    first_name = profile_data.get("firstName", "")
    last_name = profile_data.get("lastName", "")
    full_name = profile_data.get("fullName", f"{first_name} {last_name}")

    profile_picture_url = profile_data.get("profilePicHighQuality", profile_data.get("profilePic", ""))
    Profile_picture_sug = profile_picture_optimizer(profile_picture_url) if profile_picture_url else None

    headline = profile_data.get("headline", "")
    about = profile_data.get("about", "")

    Experience = profile_data.get("experiences", [])

    raw_skills = profile_data.get("skills", [])
    Skills = [skill.get("title", "") for skill in raw_skills]
    Projects = profile_data.get("projects")

    work_suggestion_result = work_suggestion(headline, about, Experience, Skills,Projects)
    if isinstance(work_suggestion_result, dict):
        work_exp_suggestion = work_suggestion_result.get('Work_exp', "")
        headline_suggestion = work_suggestion_result.get('headline', "")
        about_suggestion = work_suggestion_result.get('About', "")
        skills_suggestion = work_suggestion_result.get('Skills', "")
        Project_suggestion = work_suggestion_result.get('Projects',"")
    else:
        work_exp_suggestion = getattr(work_suggestion_result, 'Work_exp', "")
        headline_suggestion = getattr(work_suggestion_result, 'headline', "")
        about_suggestion = getattr(work_suggestion_result, 'About', "")
        skills_suggestion = getattr(work_suggestion_result, 'Skills', "")
        Project_suggestion = getattr(work_suggestion_result,'Projects',"")

    
    if Profile_picture_sug:
        if isinstance(Profile_picture_sug, dict):
            profile_pic_suggestion_content = Profile_picture_sug.get("content", "")
        else:
            profile_pic_suggestion_content = getattr(Profile_picture_sug, "content", "")
    else:
        profile_pic_suggestion_content = ""

    # Map additional fields (adjusted to match available Apify data)
    location = profile_data.get("addressWithCountry", "")
    open_to_work_status = profile_data.get("openConnection", False)
    follower_cnt = profile_data.get("followers", 0)
    education = profile_data.get("educations", [])
    language = profile_data.get("languages", [])
    # Build present company info from the available fields
    present_company_info = {
        "CompanyprofilePic": profile_data.get("profilePicHighQuality", ""),
        "email": profile_data.get("email", ""),
        "companyName": profile_data.get("companyName", ""),
        "companyIndustry": profile_data.get("companyIndustry", ""),
        "companyWebsite": profile_data.get("companyWebsite", ""),
        "companyLinkedin": profile_data.get("companyLinkedin", ""),
        "companyFoundedIn": profile_data.get("companyFoundedIn", None),
        "companySize": profile_data.get("companySize", "")
    }
    detailed_education = []
    for edu in profile_data.get("educations", []):
        activities = ""
        for comp in edu.get("subComponents", []):
            for d in comp.get("description", []):
                activities += d.get("text", "") + " "
        detailed_education.append({
            "institution": edu.get("title", ""),
            "degree": edu.get("subtitle", ""),
            "duration": edu.get("caption", ""),
            "activities": activities.strip()
        })

    try:
        UserProfile_Suggestion_collection.update_one(
            {"link_id": link_id},  # Filter condition
            {
                "$set": {  
                    "link_id": link_id,
                    "UserLinkedIN_URL": profile_data.get("linkedinUrl", url),
                    "UserInfo": {
                        "FullName": full_name,
                        "Location": location,
                        "open_to_work_status": open_to_work_status,
                        "Follower_cnt": follower_cnt,
                        "Education": education,
                        "Language": language,
                        "present_company_info": present_company_info,
                        "Education": detailed_education,
                    },
                    
                    "Profile_Pic": {
                        "url": profile_picture_url,
                        "ProfilePic_sug": profile_pic_suggestion_content
                    },
                    "HeadlineSection": {
                        "Headline": headline,
                        "Headline_Sug": headline_suggestion,
                    },
                    "AboutSection": {
                        "AboutSug": about_suggestion,
                        "About": about
                    },
                    "WorkSection": {
                        "Work_Exp_Sug": work_exp_suggestion,
                        "Work": Experience
                    },
                    "SkillSection": {
                        "Skill": Skills,
                        "Skills_Sug": skills_suggestion,
                    },
                    "ProjectSection": {
                        "Project": Projects,
                        "Project_Sug": Project_suggestion,
                    },
                }
            },
            upsert=True  # Insert the document if it does not exist
        )
        return True
    except Exception as e:
        logger.error(f"Database update failed: {str(e)}")
        return False
