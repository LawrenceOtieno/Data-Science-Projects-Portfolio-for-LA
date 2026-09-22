from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    client_data = {
        "name": "Lynn Ajema",
        "title": "Data Scientist & MEL Officer",
        "socials": {
            "linkedin": "https://www.linkedin.com/in/lynn-ajema-8331ba197",
            "github": "https://github.com/Lajema"
        },
        "skills": [
            "Data Analysis & Science", 
            "Monitoring, Evaluation & Learning (MEL)", 
            "Python & Flask", 
            "Statistical Modeling", 
            "Agile Project Management", 
            "Data Visualization"
        ],
        "projects": [
            {
                "title": "M-Pesa Performance Dashboard", 
                "tag": "Data Science",
                "icon": "fa-solid fa-mobile-screen-button",
                "color": "teal",
                "url": "https://github.com/Lajema/M-pesa_performace_dashboard"
            },
            {
                "title": "Kenya Economic Story", 
                "tag": "Python / Economics",
                "icon": "fa-solid fa-chart-line",
                "color": "orange",
                "url": "https://github.com/Lajema/Kenya-economic-story"
            },
            {
                "title": "Kenya Green Horizon Storyboard", 
                "tag": "Data Analytics",
                "icon": "fa-solid fa-leaf",
                "color": "sage",
                "url": "https://github.com/Lajema/kenya_green_horizon_storyboard"
            },
             {
                "title": "Churn Prediction", 
                "tag": "Data Science / Machine Learning",
                "icon": "fa-solid fa-chart-pie",
                "color": "teal",
                "url": "https://github.com/Lajema/churn_prediction"
            },
            {
                "title": "Kenyan Brand Sentiment Tracker", 
                "tag": "Data Science / Machine Learning",
                "icon": "fa-solid fa-comments",
                "color": "orange",
                "url": "https://github.com/Lajema/Kenyan_brand_sentiment_tracker"
            }
        ],
        "timeline": [
            {
                "year": "July 2022 - Present", 
                "role": "Data Analyst", 
                "company": "L-IFT", 
                "details": "Conducting core data analysis, streamlining field data collection pipelines, and contributing to project monitoring."
            },
            {
                "year": "September 2022 - Present", 
                "role": "Freelance Data Analyst", 
                "company": "Aesops Ke", 
                "details": "Providing custom analytics solutions, statistical modeling, and data reporting for diverse clients."
            },
            {
                "year": "July 2021 - July 2022", 
                "role": "Client Relations Officer", 
                "company": "DTE Consultancy", 
                "details": "Managed client engagements, gathering key operational feedback and supporting client success initiatives."
            }
        ],
        "education": [
            {
                "degree": "Master's Degree in Data Science", 
                "school": "KCA University", 
                "year": "Sep 2024 – Nov 2026"
            },
            {
                "degree": "Bachelor's Degree in Statistics", 
                "school": "Taita Taveta University", 
                "year": "August 2016 - May 2021"
            },
            {
                "degree": "Certification: Agile Project Management", 
                "school": "HP LIFE", 
                "year": "Apr 2026 – May 2026"
            }
        ]
    }
    return render_template('index.html', data=client_data)

if __name__ == '__main__':
    app.run(debug=True)
