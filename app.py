from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    client_data = {
        "name": "Lynn Ajema",
        "title": "Data Scientist & MEL Officer",
        "email": "lynn.ajema@example.com",
        "socials": {
            "linkedin": "https://linkedin.com/in/lynn-ajema",
            "github": "https://github.com/lynn-ajema",
            "facebook": "https://facebook.com/lynn-ajema",
            "twitter": "https://twitter.com/lynn-ajema"
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
                "title": "Impact Evaluation Dashboard", 
                "desc": "Built a comprehensive MEL reporting system to track key project indicators and field metrics.", 
                "tag": "Data Science & MEL",
                "url": "https://github.com/lynn-ajema/project-one"
            },
            {
                "title": "Statistical Forecasting Model", 
                "desc": "Developed predictive models for client trend analysis using advanced statistical methods.", 
                "tag": "Python / Statistics",
                "url": "https://example.com/live-demo"
            },
            {
                "title": "Interactive Data Pipeline", 
                "desc": "Designed clean ETL pipelines to convert raw survey data into actionable visual insights.", 
                "tag": "Data Analytics",
                "url": "https://github.com/lynn-ajema/project-three"
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