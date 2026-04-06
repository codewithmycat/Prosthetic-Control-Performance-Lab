import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Prosthetic Limb Virtual Lab", layout="wide")

st.title("🦾 Prosthetic Limb Virtual Lab")

# Sidebar Navigation
section = st.sidebar.radio("Go to", [
    "Aim",
    "Theory",
    "Experiment",
    "Simulation",
    "Observations",
    "Result",
    "Viva Questions"
])

# AIM
if section == "Aim":
    st.header("🎯 Aim")
    st.write("""
    To study the working of prosthetic limbs and analyze how grip strength 
    and control mechanisms affect performance.
    """)

# THEORY
elif section == "Theory":
    st.header("📘 Theory")
    st.write("""
    Prosthetic limbs are artificial devices used to replace missing body parts.

    Types:
    - Basic Mechanical: Operated manually
    - Myoelectric: Uses electrical signals from muscles

    Grip strength and control determine efficiency in handling objects.
    """)

# EXPERIMENT
elif section == "Experiment":
    st.header("🧪 Experiment Procedure")
    st.write("""
    1. Select the type of prosthetic limb  
    2. Adjust grip strength  
    3. Choose an object  
    4. Perform the simulation  
    5. Record observations  
    """)

# SIMULATION
elif section == "Simulation":
    st.header("🎮 Simulation")

    prosthetic_type = st.selectbox(
        "Select Prosthetic Type",
        ["Basic Mechanical", "Myoelectric"]
    )

    grip = st.slider("Grip Strength", 0, 100, 50)

    object_type = st.selectbox(
        "Select Object",
        ["Light Object (Cup)", "Heavy Object (Dumbbell)", "Fragile Object (Glass)"]
    )

    if st.button("Run Simulation"):
        result = ""

        if prosthetic_type == "Basic Mechanical":
            if grip > 70:
                result = "Object successfully picked"
            else:
                result = "Failed due to weak grip"
        else:
            if grip > 40:
                result = "Smooth grip using muscle signals"
            else:
                result = "Poor signal strength"

        if "Fragile" in object_type and grip > 80:
            result = "Object broke due to excess force"

        st.success(result)

# OBSERVATIONS
elif section == "Observations":
    st.header("📊 Observation Table")

    # Generate random data
    data = {
        "Trial": [1, 2, 3, 4, 5],
        "Grip Strength": [random.randint(30, 100) for _ in range(5)],
        "Prosthetic Type": [random.choice(["Mechanical", "Myoelectric"]) for _ in range(5)],
        "Object": [random.choice(["Cup", "Dumbbell", "Glass"]) for _ in range(5)],
        "Result": [random.choice(["Success", "Fail", "Object Broken"]) for _ in range(5)]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)

# RESULT
elif section == "Result":
    st.header("📈 Result")
    st.write("""
    It is observed that myoelectric prosthetic limbs require less grip strength 
    compared to mechanical limbs and provide better control. Excess grip strength 
    may damage fragile objects.
    """)

# VIVA QUESTIONS
elif section == "Viva Questions":
    st.header("❓ Viva Questions")

    questions = [
        "What is a prosthetic limb?",
        "Difference between mechanical and myoelectric prosthesis?",
        "What is grip strength?",
        "Why are myoelectric limbs more efficient?",
        "What happens when excessive force is applied?"
    ]

    for q in questions:
        st.write("• " + q)
