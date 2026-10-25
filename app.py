import streamlit as st

st.set_page_config(
    page_title="Disha Career Assistant",
    page_icon="🎯",
    layout="wide"
)

CAREERS = {
    "AI Engineer": {
        "skills": ["python", "machine learning", "ai", "math"],
        "learn": [
            "Strengthen Python and data structures",
            "Learn NumPy, Pandas and machine learning",
            "Study LLMs, prompt engineering and RAG",
            "Build an AI application and deploy it"
        ],
        "projects": [
            "AI Document Assistant",
            "Career Guidance Chatbot",
            "Student Performance Predictor"
        ]
    },
    "Web Developer": {
        "skills": ["html", "css", "javascript", "web"],
        "learn": [
            "Learn HTML and CSS",
            "Practise JavaScript",
            "Learn APIs and responsive design",
            "Build and deploy a complete website"
        ],
        "projects": [
            "Portfolio Website",
            "Weather Web App",
            "Student Management System"
        ]
    },
    "Data Analyst": {
        "skills": ["python", "sql", "excel", "data", "statistics"],
        "learn": [
            "Practise Excel and SQL",
            "Learn Python with Pandas",
            "Study statistics and data visualisation",
            "Build a dashboard using real datasets"
        ],
        "projects": [
            "Student Marks Analysis",
            "Sales Dashboard",
            "Customer Data Analysis"
        ]
    },
    "Software Developer": {
        "skills": ["python", "java", "c++", "programming", "dsa"],
        "learn": [
            "Strengthen one programming language",
            "Learn object-oriented programming",
            "Practise data structures and algorithms",
            "Build and test a complete software project"
        ],
        "projects": [
            "Bank Management System",
            "Expense Tracker",
            "Library Management System"
        ]
    }
}


def recommend_careers(user_skills):
    skills = {
        item.strip().lower()
        for item in user_skills.split(",")
        if item.strip()
    }

    results = []

    for career, details in CAREERS.items():
        matched = [
            skill for skill in details["skills"]
            if any(
                skill == user_skill
                or skill in user_skill
                or user_skill in skill
                for user_skill in skills
            )
        ]

        score = len(matched)

        results.append({
            "career": career,
            "score": score,
            "matched": matched,
            "details": details
        })

    return sorted(
        results,
        key=lambda item: item["score"],
        reverse=True
    )


st.title("🎯 Disha AI Career Assistant")
st.write(
    "Explore career paths and create your personal learning roadmap."
)

st.info(
    "Prototype version: recommendations are based on "
    "matching your skills with predefined career profiles."
)

with st.form("career_form"):
    st.subheader("Tell us about yourself")

    name = st.text_input("Your first name (optional)")

    skills = st.text_input(
        "Your skills",
        placeholder="Python, HTML, CSS, machine learning"
    )

    interests = st.selectbox(
        "Your main interest",
        [
            "Artificial Intelligence",
            "Web Development",
            "Data Analysis",
            "Software Development"
        ]
    )

    level = st.selectbox(
        "Your current level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    submitted = st.form_submit_button(
        "Find My Career Path"
    )


if submitted:
    if not skills.strip():
        st.warning("Please enter at least one skill.")
    else:
        results = recommend_careers(skills)

        interest_map = {
            "Artificial Intelligence": "AI Engineer",
            "Web Development": "Web Developer",
            "Data Analysis": "Data Analyst",
            "Software Development": "Software Developer"
        }

        preferred = interest_map[interests]

        results.sort(
            key=lambda item: (
                item["score"],
                item["career"] == preferred
            ),
            reverse=True
        )

        st.success(
            f"Welcome{' ' + name if name.strip() else ''}! "
            "Here are your suggested career paths."
        )

        for item in results[:3]:
            career = item["career"]
            details = item["details"]

            with st.expander(
                f"{career} — {item['score']} skill matches",
                expanded=(career == results[0]["career"])
            ):
                st.write(
                    f"**Your current level:** {level}"
                )

                st.write("**Matched skills:**")

                if item["matched"]:
                    st.write(", ".join(item["matched"]))
                else:
                    st.write(
                        "No direct match. Explore the roadmap "
                        "to identify skills you can learn."
                    )

                st.subheader("Your learning roadmap")

                for number, step in enumerate(
                    details["learn"], start=1
                ):
                    st.write(f"{number}. {step}")

                st.subheader("Suggested projects")

                for project in details["projects"]:
                    st.write(f"- {project}")

        st.caption(
            "These suggestions are exploratory, not a guarantee "
            "of career suitability or employment."
        )

st.divider()

st.caption(
    "Disha Career Assistant | Built with Python and Streamlit"
)