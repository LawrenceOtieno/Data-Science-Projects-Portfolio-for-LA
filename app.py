from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    client_data = {
        "name": "Jane Doe",
        "title": "Full-Stack Developer & Designer",
        "email": "jane.doe@example.com",
        "socials": {
            "linkedin": "https://linkedin.com/in/username",
            "github": "https://github.com/username",
            "facebook": "https://facebook.com/username",
            "twitter": "https://twitter.com/username"
        },
        "skills": [
            "Python", 
            "Flask", 
            "HTML5 & CSS3", 
            "JavaScript", 
            "UI/UX Design", 
            "Git & GitHub"
        ],
        "projects": [
            {
                "title": "E-Commerce Experience", 
                "desc": "Custom web application with streamlined checkout flow.", 
                "tag": "Flask / Python",
                "url": "https://github.com/username/project-one"
            },
            {
                "title": "Brand Identity System", 
                "desc": "Comprehensive visual strategy and web architecture.", 
                "tag": "UI/UX Design",
                "url": "https://example.com/live-demo"
            },
            {
                "title": "Analytics Dashboard", 
                "desc": "Real-time data visualizer for client operations.", 
                "tag": "Frontend Development",
                "url": "https://github.com/username/project-three"
            }
        ],
        "timeline": [
            {
                "year": "2023 - Present", 
                "role": "Senior Frontend Developer", 
                "company": "Tech Solutions Inc.", 
                "details": "Leading web team and building scalable interfaces."
            },
            {
                "year": "2021 - 2023", 
                "role": "Web Developer", 
                "company": "Creative Agency", 
                "details": "Designed and deployed custom client websites."
            }
        ],
        "education": [
            {
                "degree": "B.S. in Computer Science", 
                "school": "State University", 
                "year": "2017 - 2021"
            },
            {
                "degree": "AWS Certified Cloud Practitioner", 
                "school": "Amazon Web Services", 
                "year": "2023"
            }
        ]
    }
    return render_template('index.html', data=client_data)

if __name__ == '__main__':
    app.run(debug=True)