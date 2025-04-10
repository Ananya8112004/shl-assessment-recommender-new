import streamlit as st
from recommender import load_shl_data, get_recommendations

st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")
st.title("🔍 SHL Assessment Recommendation System")

st.markdown("Type or paste your job requirement / description below:")

query = st.text_area("Job Description", height=200)

if st.button("Recommend Assessments"):
    if not query.strip():
        st.warning("Please enter a valid job description.")
    else:
        with st.spinner("Generating recommendations..."):
            df = load_shl_data()
            recommendations = get_recommendations(query, df)
        st.subheader("📋 Top Recommendations")
        st.markdown(recommendations)


