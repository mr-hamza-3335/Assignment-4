import streamlit as st
from streamlit.components.v1 import html

# Custom CSS for styling and animations
st.markdown("""
<style>
    /* General Styling */
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f4f4f9;
        color: #333;
    }
    h1, h2, h3 {
        color: #4CAF50;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    /* Project Cards */
    .project-card {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 16px;
        margin: 16px 0;
        background-color: white;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .project-card img {
        width: 100%;
        border-radius: 8px;
    }
    .project-card h3 {
        margin-top: 0;
    }
    .project-card a {
        color: #4CAF50;
        text-decoration: none;
    }
    .project-card a:hover {
        text-decoration: underline;
    }
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .fadeIn {
        animation: fadeIn 1.5s ease-in-out;
    }
    /* Responsive Design */
    @media (max-width: 768px) {
        h1 {
            font-size: 24px;
        }
        h2 {
            font-size: 20px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "About", "Projects", "Contact", "Socials"))

# Home Page
if page == "Home":
    st.title("Welcome to Ameer Hamza's Portfolio 🚀")
    st.write("Hi, I'm **Ameer Hamza**, a Fullstack Developer with a passion for building amazing web applications.")
    st.write("Explore my portfolio to learn more about my skills, projects, and achievements.")

    # Animated Introduction
    st.markdown('<div class="fadeIn">', unsafe_allow_html=True)
    st.write("### Let's build something incredible together!")
    st.markdown('</div>', unsafe_allow_html=True)

    # Call to Action
    if st.button("View My Projects"):
        st.write("Redirecting to Projects...")

# About Page
elif page == "About":
    st.title("About Me")
    st.write("I'm a **Fullstack Developer** with expertise in building modern web applications.")
    st.write("### Education")
    st.write("- Intermediate (Currently pursuing higher education)")
    st.write("### Skills")
    st.write("- Frontend: HTML, CSS, JavaScript, React")
    st.write("- Backend: Node.js, Python, Django")
    st.write("- Databases: MongoDB, MySQL")
    st.write("- Tools: Git, Docker, Streamlit")

    # Download Resume
    st.write("### Download My Resume")
    with open("sample_resume.txt", "w") as f:
        f.write("Ameer Hamza - Fullstack Developer\n\nSkills: Python, JavaScript, React, Node.js, MongoDB")
    with open("sample_resume.txt", "rb") as f:
        st.download_button(
            label="Download Resume",
            data=f,
            file_name="Ameer_Hamza_Resume.txt",
            mime="text/plain"
        )

# Projects Page
elif page == "Projects":
    st.title("My Projects")
    st.write("Here are some of the projects I've worked on:")

    # Fetch and display projects from portfolio
    st.write("### Portfolio Projects")
    portfolio_projects = [
        {
            "title": "Portfolio Website",
            "description": "A fully responsive portfolio website built with React and deployed on Vercel.",
            "image": "https://via.placeholder.com/300x200?text=Portfolio+Website",
            "link": "https://ameer-hamza-com.vercel.app/"
        },
        {
            "title": "E-Commerce Website",
            "description": "An e-commerce platform built with React and Node.js.",
            "image": "https://via.placeholder.com/300x200?text=E-Commerce+Website",
            "link": "https://ameer-hamza-com.vercel.app/"
        }
    ]

    for project in portfolio_projects:
        st.markdown(f"""
        <div class="project-card fadeIn">
            <h3>{project['title']}</h3>
            <img src="{project['image']}" alt="{project['title']}">
            <p>{project['description']}</p>
            <a href="{project['link']}" target="_blank">View Project</a>
        </div>
        """, unsafe_allow_html=True)

    # Fetch and display Streamlit projects
    st.write("### Streamlit Projects")
    streamlit_projects = [
        {
            "title": "BMI Calculator",
            "description": "A dynamic BMI calculator built using Streamlit.",
            "image": "https://via.placeholder.com/300x200?text=BMI+Calculator",
            "link": "https://share.streamlit.io/"
        },
        {
            "title": "Data Visualization App",
            "description": "A data visualization app built with Streamlit and Python.",
            "image": "https://via.placeholder.com/300x200?text=Data+Viz+App",
            "link": "https://share.streamlit.io/"
        }
    ]

    for project in streamlit_projects:
        st.markdown(f"""
        <div class="project-card fadeIn">
            <h3>{project['title']}</h3>
            <img src="{project['image']}" alt="{project['title']}">
            <p>{project['description']}</p>
            <a href="{project['link']}" target="_blank">View Project</a>
        </div>
        """, unsafe_allow_html=True)

# Contact Page
elif page == "Contact":
    st.title("Contact Me")
    st.write("Feel free to reach out to me for collaborations or inquiries.")

    # Contact Form
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.success(f"Thank you, **{name}**! Your message has been sent.")
            st.write(f"**Email:** {email}")
            st.write(f"**Message:** {message}")

# Socials Page
elif page == "Socials":
    st.title("Connect With Me")
    st.write("Check out my work and connect with me on these platforms:")

    # Social Media Links
    st.write("### YouTube Channel")
    st.write("[Hamza On Air](https://www.youtube.com/@HamzaOnAir)")

    st.write("### Portfolio")
    st.write("[Ameer Hamza Portfolio](https://ameer-hamza-com.vercel.app/)")

    st.write("### GitHub")
    st.write("[GitHub Profile](https://github.com/mr-hamza-3335)")

    st.write("### Streamlit")
    st.write("[Streamlit Projects](https://share.streamlit.io/)")

# Footer
st.markdown("---")
st.write("Made with ❤️ by **Ameer Hamza**")

# JavaScript for additional animations
html("""
<script>
    // Add custom animations here
    document.addEventListener("DOMContentLoaded", function() {
        const elements = document.querySelectorAll('.fadeIn');
        elements.forEach(el => {
            el.style.opacity = 0;
            setTimeout(() => {
                el.style.opacity = 1;
            }, 500);
        });
    });
</script>
""")