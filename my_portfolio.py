import streamlit as st

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(page_title="Shubhangi Singh | Portfolio", layout="wide")

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.title("Shubhangi Singh")
st.sidebar.markdown("🎓 Aspiring Data Analyst | Mechanical Engineering Student")
st.sidebar.markdown("[📍 GitHub](https://github.com/shubhangi2124)")
st.sidebar.markdown("[📧 Email](mailto:singhshubhangi2124@gmail.com)")
st.sidebar.markdown("📞 +91 7523866637")
st.sidebar.markdown("🌐 [LinkedIn](https://www.linkedin.com/in/shubhangi-singh-228021228/)")

# ------------------------------
# About Me
# ------------------------------
st.title("👩‍💻 About Me")
st.write("""
Hi! I'm **Shubhangi Singh**, a third-year Mechanical Engineering student passionate about **Data Analysis** and **Machine Learning**.  
I love finding patterns in data and telling stories through visualizations.

I'm currently working on projects to analyze YouTube trends, financial patterns, and Instagram engagement, and I’m always eager to learn more.
""")

# ------------------------------
# Skills
# ------------------------------
st.subheader("🧰 Skills")
st.write("""
- **Languages**: Python, SQL, Excel  
- **Libraries**: Pandas, Numpy, Matplotlib, Seaborn, Scikit-learn  
- **Tools**: Jupyter Notebook, Streamlit, GitHub  
- **Concepts**: Data Cleaning, EDA, Regression, Visualization, Forecasting
""")

# ------------------------------
# Projects
# ------------------------------
st.subheader("📊 Projects")

with st.expander("1. 📈 YouTube Data Analysis"):
    st.write("""
    - Analyzed trends from YouTube video dataset  
    - Cleaned data, performed EDA, and visualized results  
    - Tools: Pandas, Seaborn, Matplotlib  
    - [🔗 View on GitHub](https://github.com/shubhangi2124/YouTube-Data-Analysis)
    """)

with st.expander("2. 📉 Insta Engagement & Reach Forecasting"):
    st.write("""
    - Predicted future engagement rates on Instagram using forecasting models  
    - Extracted trends from dataset and built visualizations  
    - [🔗 View on GitHub](https://github.com/shubhangi2124/Insta-Engagement-Forecasting)
    """)

with st.expander("3. 💸 Financial Analysis"):
    st.write("""
    - Conducted financial data analysis using Python  
    - Explored patterns in expense and income data  
    - [🔗 View on GitHub](https://github.com/shubhangi2124/Financial-Analysis-Using-Python)
    """)

with st.expander("4. 📱 Screen Time Analysis"):
    st.write("""
    - Analyzed screen time patterns from phone usage logs  
    - Delivered insights on habits and productivity  
    - [🔗 View on GitHub](https://github.com/shubhangi2124/Analyse-Screen-Time)
    """)

with st.expander("5. 📊 Stock Market Analysis"):
    st.write("""
    - Explored stock trends and volatility  
    - Created plots for price movement and volume  
    - [🔗 View on GitHub](https://github.com/shubhangi2124/Stock-Market-Analysis)
    """)

with st.expander("6. 🎓 Capstone Project - TikTok Model"):
    st.write("""
    - Final capstone project for Google Advanced Data Analytics Certification  
    - Focused on modeling TikTok data for growth analysis  
    - [🔗 View on GitHub](https://github.com/shubhangi2124/TikTok-Capstone)
    """)

# ------------------------------
# Contact
# ------------------------------
st.subheader("📬 Contact")
st.write("""
- **Email:** singhshubhangi2124@gmail.com  
- **Phone:** +91 7523866637  
- **GitHub:** [shubhangi2124](https://github.com/shubhangi2124)  
- **LinkedIn:** [Shubhangi Singh](https://www.linkedin.com/in/shubhangi-singh-228021228/)
""")
