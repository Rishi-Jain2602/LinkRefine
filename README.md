# LinkRefine: Polish Your LinkedIn Presence

**LinkRefine** is a web application that helps users refine and optimize their LinkedIn profiles. By simply providing a **LinkedIn profile URL**, the tool fetches and analyzes **profile data (such as the user’s headline, about section, work experience, skills, and more)**, and then offers **AI-driven suggestions** on how to improve each section. This makes it easier for professionals to present their expertise more effectively, attract recruiters, and stand out in their network.
****
## Local Environment Setup

1. Clone the Repository
   
``` bash
git clone https://github.com/Rishi-Jain2602/LinkRefine.git
```

2. Create Virtual Environment

```bash
cd backend
virtualenv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```

3. Install the Project dependencies

- 3.1 Navigate to the **Backend** Directory and install Python dependencies:

```bash
cd backend
pip install -r requirements.txt
```
- 3.2 Navigate to the **Frontend** Directory and install Node.js dependencies:
```bash
cd frontend
npm install
```

4. Run the React App

Start the React app with the following command:

```bash
cd frontend
npm start
```
- The server will be running at `http://localhost:3000`.

5. Run the Backend (FastAPI App)

Open a new terminal and run the backend:

```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
- The server will be running at `http://127.0.0.1:8000`.


****


### Usage Guide

1. **Uploading Your Profile URL:**  
   - Navigate to the Upload page where you will see an input field prompting you to enter your LinkedIn profile URL.
   - Enter your URL and click the "Upload" button.
   - The frontend sends a POST request to the `/linkrefine/upload` endpoint, which triggers the backend to process the URL.

2. **Processing and Redirect:**  
   - The backend processes the profile URL, generates a unique `link_id`, and returns it upon successful processing.
   - The frontend stores this `link_id` in localStorage and then automatically redirects you to the Review page.

3. **Reviewing AI Suggestions:**  
   - On the Review page, a GET request is made using the stored `link_id` to fetch your processed profile data.
   - The page displays your original profile information along with AI-generated suggestions for improving sections like your headline, about section, work experience, and more.
   - Each section includes detailed suggestions and improvements to help enhance your LinkedIn profile.

******

### Technology Stack

#### **Frontend:**  
  - **React:** For building a dynamic and responsive user interface.
  - **React Router:** To manage navigation between different pages (Upload and Review).
  - **Axios:** For handling API requests between the frontend and backend.
  - **CSS:** For custom styling and ensuring a consistent look and feel across the application.

#### **Backend:**  
 - **FastAPI:** A modern, high-performance Python framework used for building RESTful APIs.
- **uvicorn:** An ASGI server that runs the FastAPI application.
- **Python:** The main programming language used for backend development.
- **LangChain:** A framework for integrating large language models (LLMs) into applications. It orchestrates the interaction between your backend and the LLMs.
- **Mistral LLM:** Leveraged via LangChain to suggest projects, skills, work experience, and other profile enhancements.
- **LLAMA 3B (from GRQ):** Utilized for image-related tasks, such as analyzing profile images or generating image descriptions, to further enhance profile optimization.

*****


## Note
1. Make sure you have Python 3.x and npm 10.x installed
2. It is recommended to use a virtual environment for backend to avoid conflict with other projects.
3. If you encounter any issue during installation or usage please contact rishijainai262003@gmail.com or rj1016743@gmail.com
