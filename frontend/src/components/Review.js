import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './styles/Review.css';

function generateSessionId() {
  return Math.random().toString(36).substring(2, 10);
}

export default function Review() {
  const [profileData, setProfileData] = useState(null);
  const storedUrl = localStorage.getItem('link_id') || '';

  useEffect(() => {
    if (storedUrl) {
      axios
        .get("http://127.0.0.1:8000/linkrefine/review", {
          params: { "link_id": storedUrl },
        })
        .then((response) => {
          setProfileData(response.data.response);
        })
        .catch((error) => {
          console.error("Error fetching profile data:", error);
        });
    }
  }, [storedUrl]);

  const formatImprovementText = (text) => {
    return text.split('\n').map((line, index) => {
      const formattedLine = line.split('**').map((part, partIndex) =>
        partIndex % 2 === 1 ? <strong key={partIndex}>{part}</strong> : part
      );
      return <div key={index}>{formattedLine}</div>;
    });
  };

  if (!storedUrl) {
    return <div className="no-url-message">Please upload your LinkedIn Profile URL to view the result...</div>;
  }

  return (
    <div className="review-container">
      {profileData ? (
        <>
          <div className="card">
            <img src={profileData?.Profile_Pic?.url} className="card-img-left" alt="Profile Pic Not available" />
            <div className="card-body py-2">
              <h5 className="card-title">LinkedIn URL</h5>
              <p> {profileData.UserLinkedIN_URL }</p>
              <h5 className="card-title">User Information</h5>
              <p><strong>Full Name:</strong> {profileData.UserInfo.FullName}</p>
              <p><strong>Company:</strong> {profileData.UserInfo.present_company_info.
                companyName || 'Not Mentioned'}</p>
              <p><strong>Location:</strong> {profileData.UserInfo.Location || 'Not Mentioned'}</p>
              <p><strong>Open to Work:</strong> {profileData.UserInfo.open_to_work_status ? "Yes" : "No"}</p>
              <p><strong>Followers:</strong> {profileData.UserInfo.Follower_cnt}</p>


              <p><strong>Language:</strong></p>
              <ul>
                {profileData.UserInfo.Language && profileData.UserInfo.Language.length > 0 ? (
                  profileData.UserInfo.Language.map((lang, index) => (
                    <li key={index}>
                      {lang.title || 'Not Mentioned'} - {lang.caption || 'Not Mentioned'}
                    </li>
                  ))
                ) :
                  'Not Mentioned'
                }

              </ul>

            </div>
          </div>
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Education:</h5>
              <ul>
                {profileData.UserInfo.Education.map((edu, index) => (
                  <li key={index}>
                    <p><strong>Degree:</strong> {edu.degree || 'Not Mentioned'}</p>
                    <p><strong>Institution:</strong> {edu.institution}</p>
                    <p><strong>Duration: </strong>
                      {typeof edu.duration === 'object' ? JSON.stringify(edu.duration) : edu.duration}
                    </p>
                    <p><strong>Activities: </strong>
                      {Array.isArray(edu.activities)
                        ? edu.activities.join(', ')
                        : typeof edu.activities === 'object'
                          ? JSON.stringify(edu.activities)
                          : edu.activities || 'Not Mentioned'}
                    </p>
                  </li>
                ))}
              </ul>
            </div>
          </div>

          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Headline Suggestions</h5>
              <p><strong>Current Headline:</strong> {profileData.HeadlineSection.Headline || 'Not Mentioned'}</p>
              <p><strong>AI Suggestion:</strong>{formatImprovementText(profileData.HeadlineSection.Headline_Sug)}</p>
            </div>
          </div>

          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Profile Picture Suggestions</h5>
              <p>
                <strong>AI Suggestion: </strong>
                {profileData?.Profile_Pic?.ProfilePic_sug && formatImprovementText(profileData.Profile_Pic.ProfilePic_sug) ? (
                  formatImprovementText(profileData.Profile_Pic.ProfilePic_sug)
                ) : (
                  'Please consider adding a profile picture. A professional photo creates a strong first impression and builds trust with potential employers or connections, making your profile more approachable and credible.'
                )}
              </p>
            </div>
          </div>


          <div className="card">
            <div className="card-body">
              <h5 className="card-title">About Section Suggestions</h5>
              <p><strong>About:</strong> {profileData.AboutSection.About || 'Not Mentioned'}</p>
              <p><strong>AI Suggestion:</strong>{formatImprovementText(profileData.AboutSection.AboutSug)}</p>
            </div>
          </div>

          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Work Experience</h5>
              <p><strong>Work Experience Suggestions:</strong></p>
              <p><strong></strong>{formatImprovementText(profileData.WorkSection.Work_Exp_Sug)}</p>
            </div>
          </div>
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Projects</h5>
              <p><strong>Projects Suggestions:</strong></p>
              <p><strong></strong>{formatImprovementText(profileData.ProjectSection.Project_Sug)}</p>
            </div>
          </div>

          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Skills</h5>
              <p><strong>Skill Suggestions:</strong></p>
              <p><strong></strong>{formatImprovementText(profileData.SkillSection.Skills_Sug)}</p>
            </div>
          </div>
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Company</h5>
              <p><strong>Name:</strong> {profileData.UserInfo.present_company_info.companyName || 'Not Mentioned'}</p>
              <p><strong>Company LinkedIn:</strong> {profileData.UserInfo.present_company_info.companyLinkedin || 'Not available'}</p>
              <p><strong>Website:</strong> {profileData.UserInfo.present_company_info.companyWebsite || 'Not available'}</p>
              <p><strong>Industry:</strong> {profileData.UserInfo.present_company_info.companyIndustry || 'Not available'}</p>
              <p><strong>Company Size:</strong> {profileData.UserInfo.present_company_info.companySize || 'Not available'}</p>
              <p><strong>Founded in:</strong> {profileData.UserInfo.present_company_info.companyFoundedIn || 'Not available'}</p>
              <p><strong>Email:</strong> {profileData.UserInfo.present_company_info.email || 'Not available'}</p>
            </div>
          </div>
        </>

      ) : (
        <div className="loading">Loading profile data...</div>
      )}
    </div>
  );
}
