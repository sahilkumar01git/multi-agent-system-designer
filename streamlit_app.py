import streamlit as st
from graph.workflow import run_workflow

st.set_page_config(page_title="AI System Designer", layout="wide")

st.title("AI Multi-Agent System Designer")

st.write(
"""
Generate complete system design using AI agents:

• Product requirements
• System architecture
• Backend structure
• Timeline
"""
)

if "output" not in st.session_state:
    st.session_state.output = ""

idea = st.text_input("Enter product idea")

if st.button("Generate"):
    if not idea.strip():
        st.warning("Please enter idea")
    else:
        with st.spinner("Agents are designing system..."):
            result = run_workflow(idea)

        st.session_state.output = result["output"]
        st.success("Design generated")

if st.session_state.output:
    st.subheader("System Design")
    st.markdown(st.session_state.output)

    st.download_button(
        "Download result",
        data=st.session_state.output,
        file_name="system_design.txt",
        mime="text/plain",
    )
