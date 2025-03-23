# import pickle
# import pandas as pd
# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np

# # Load the trained model
# with open("teacher_burnout_model.pkl", "rb") as model_file:
#     model = pickle.load(model_file)

# # Load label encoders
# with open("label_encoders.pkl", "rb") as enc_file:
#     encoders = pickle.load(enc_file)

# # Load feature order
# with open("trained_feature_order.pkl", "rb") as feature_file:
#     trained_features = pickle.load(feature_file)

# # Burnout Level Mapping
# burnout_levels = {0: "Low Burnout", 1: "Moderate Burnout", 2: "High Burnout"}

# # Streamlit UI Design
# st.set_page_config(page_title="Teacher Burnout Predictor", page_icon="📊", layout="centered")

# # Sidebar Navigation
# st.sidebar.title("🧭 Navigation")
# page = st.sidebar.radio("Go to", ["Predict Burnout", "About Burnout"])
# # Sidebar Details
# st.sidebar.markdown("---")
# st.sidebar.subheader("📌 Model Details")
# st.sidebar.markdown("""
# - **Model Used:** XGBoost Classifier  
# - **Key Features Considered:** Psychological, Work, and Social Factors  
# """)

# st.sidebar.subheader("📊 Prediction Insights")
# st.sidebar.markdown("""
# - **Low Burnout:** Healthy work-life balance, manageable stress.  
# - **Moderate Burnout:** Increased stress, may need intervention.  
# - **High Burnout:** Critical state, requires urgent action.  
# """)


# if page == "Predict Burnout":
#     st.markdown("<h1 style='text-align: center; color: #ff6347;'>📊 Teacher Burnout Predictor</h1>", unsafe_allow_html=True)
#     st.markdown("<h4 style='text-align: center; color: black;'>Model: TeacherBurnoutPredictor_Xg</h4>", unsafe_allow_html=True)

#     # User Inputs
#     st.markdown("<h3 style='color: #4682B4;'>📝 Enter Teacher Data</h3>", unsafe_allow_html=True)

#     col1, col2 = st.columns(2)

#     with col1:
#         country = st.text_input("🌍 Country")
#         employment_type = st.text_input("🏫 Employment Type")
#         # occupation = st.text_input("👩‍🏫 Occupation")
#         occupation ="Teacher"
#         work_from_home = st.selectbox("🏠 Work From Home", ["Yes", "No"])

#     with col2:
#         partnership_status = st.text_input("💑 Partnership Status (Single/Married/Other)")
#         subjective_income = st.slider("💰 Subjective Income Level", 1, 5)
#         happiness = st.slider("😊 Happiness Level", 1, 5)

#     st.markdown("---")

#     # More Inputs
#     st.markdown("<h4 style='color: #FFA500;'>📊 Psychological Factors</h4>", unsafe_allow_html=True)

#     col3, col4 = st.columns(2)

#     with col3:
#         hard_concentrate_work = st.slider("🧠 Difficulty Concentrating on Work", 1, 5)
#         loneliness = st.slider("😔 Loneliness Level", 1, 5)

#     with col4:
#         feeling_rejected = st.slider("🚫 Feeling Rejected", 1, 5)

#     # Convert categorical inputs
#     input_data = {
#         "Country": country,
#         "EmploymentType": employment_type,
#         "Occupation": occupation,
#         "WorkFromHome": work_from_home,
#         "HardConcentrateWork": hard_concentrate_work,
#         "lonely3": loneliness,
#         "FeelingRejected": feeling_rejected,
#         "SubjectiveIncome": subjective_income,
#         "Happiness": happiness,
#         "PartnershipStatus": partnership_status,
#     }

#     # Encode categorical features
#     for col in encoders:
#         if col in input_data:
#             if input_data[col] in encoders[col].classes_:
#                 input_data[col] = encoders[col].transform([input_data[col]])[0]
#             else:
#                 input_data[col] = 0  # Assign unknown categories to 0

#     # Convert to DataFrame and ensure correct column order
#     input_df = pd.DataFrame([input_data])
#     input_df = input_df.reindex(columns=trained_features, fill_value=0)

#     # Prediction Button
#     if st.button("🔍 Predict Burnout Level"):
#         prediction = model.predict(input_df)
#         predicted_label = burnout_levels[prediction[0]]

#         # Display Result
#         if predicted_label == "Low Burnout":
#             st.success(f"✅ **Predicted Burnout Level: {predicted_label}** 🟢")
#         elif predicted_label == "Moderate Burnout":
#             st.warning(f"⚠️ **Predicted Burnout Level: {predicted_label}** 🟡")
#         else:
#             st.error(f"🚨 **Predicted Burnout Level: {predicted_label}** 🔴")

#         # Personalized Recommendations
#         st.markdown("### 🛠 Personalized Solutions to Reduce Burnout")
#         solutions = {
#             "Low Burnout": [
#                 "✅ Maintain a healthy work-life balance by setting boundaries.",
#                 "✅ Continue practicing stress-relief activities such as meditation or hobbies.",
#                 "✅ Engage in professional development to stay motivated and fulfilled."
#             ],
#             "Moderate Burnout": [
#                 "⚠️ Prioritize self-care and take regular breaks during work.",
#                 "⚠️ Seek support from colleagues or professional counseling if needed.",
#                 "⚠️ Practice time management techniques to reduce work overload."
#             ],
#             "High Burnout": [
#                 "🚨 Consider speaking to a mental health professional for guidance.",
#                 "🚨 Take time off if possible to recover from burnout symptoms.",
#                 "🚨 Reevaluate workload and discuss adjustments with administration."
#             ]
#         }
        
#         for solution in solutions[predicted_label]:
#             st.write(solution)

# elif page == "About Burnout":
#     st.markdown("<h1 style='text-align: center; color: #4682B4;'>📖 Understanding Teacher Burnout</h1>", unsafe_allow_html=True)
#     st.markdown("""
#     **Why is Teacher Burnout Important?**
#     - Teacher burnout affects job satisfaction, mental health, and student outcomes.
#     - High burnout leads to increased absenteeism and teacher turnover.
#     - Preventing burnout improves teaching quality and workplace well-being.
    
#     **Factors Considered in Prediction:**
#     - **Work Environment**: Employment type, work-from-home status, occupation.
#     - **Psychological Well-being**: Stress levels, happiness, difficulty concentrating.
#     - **Social & Financial Factors**: Income level, loneliness, feeling rejected, partnership status.
    
#     **How Does This Model Help?**
#     - Identifies high-risk teachers early.
#     - Provides actionable solutions based on prediction.
#     - Encourages schools to implement support measures.
#     """, unsafe_allow_html=True)

#     # Feature importance data
#     features = ["FeelingRejected", "Happiness", "Lonely3", "Country", "PartnershipStatus", "EmploymentType", "SubjectiveIncome", "HardConcentrateWork", "WorkFromHome", "Occupation"]
#     importance = [0.305, 0.141, 0.109, 0.084, 0.066, 0.064, 0.058, 0.058, 0.057, 0.050]

#     # Feature Importance Chart
#     st.subheader("Feature Importance in Burnout Prediction")
#     fig, ax = plt.subplots()
#     y_pos = np.arange(len(features))
#     ax.barh(y_pos, importance, align='center', color='skyblue')
#     ax.set_yticks(y_pos)
#     ax.set_yticklabels(features)
#     ax.invert_yaxis()
#     ax.set_xlabel("Importance Score")
#     ax.set_title("Feature Importance in XGBoost Model")
#     st.pyplot(fig)

#     # Observations
    
#     # Key Observations
#     st.subheader("Key Observations")
#     st.markdown("""
#     - **FeelingRejected (30.5%)** is the strongest predictor. Teachers who feel rejected are at the highest risk of burnout.
#       - ✅ **Actionable Insight:** Schools should focus on **inclusion, social support, and community-building** strategies.
#     - **Happiness (14.1%) & Loneliness (10.9%)** are highly influential.
#       - ✅ **Actionable Insight:** Encouraging **peer interactions, social events, and mental health support** could help mitigate burnout.
#     - **Country (8.4%)** suggests burnout differs across regions due to education policies and workloads.
#     - **Employment Type & Partnership Status (6.4%-6.6%)** indicate **personal and work stability** matter.
#     - **WorkFromHome (5.7%) & HardConcentrateWork (5.8%)** affect burnout, possibly due to isolation or work struggles.
#     """)

#     # What This Means
#     st.subheader("🤔 What Does This Mean?")
#     st.markdown(""" 
#     ✅ **Emotional & Social Factors** (FeelingRejected, Happiness, Loneliness) dominate. Addressing these is key.
#     ✅ **Systemic & Financial Factors** (Employment Type, Income, Country) also matter. Policy changes could help.
#     ✅ **Work Environment** (WorkFromHome, HardConcentrateWork) plays a role. Improving workplace conditions may help.
#     """)

#     # Recommendations
#     st.subheader("🛠 Recommendations")
#     st.markdown("""
#     ### **1. Individual-Level Strategies (Teacher Well-Being)**
#     - 🧠 **Mental Health Support:** Schools should provide **counseling services** and mental health resources.
#     - 👥 **Social Support Networks:** Encourage **peer support groups** to reduce loneliness and rejection.
#     - ⚖ **Work-Life Balance:** Promote **flexible work arrangements**, like hybrid teaching options.
#     - 🧘 **Stress Management Programs:** Offer **mindfulness and stress training** to improve resilience.

#     ### **2. Organizational & Policy-Level Strategies**
#     - 📚 **Better Work Policies:** Schools should **reduce excessive workloads** and offer mental health days.
#     - 💰 **Financial & Job Stability:** Improving **teacher salaries and employment security** can reduce burnout risk.
#     - 🏫 **Inclusive School Culture:** Schools should foster **collaboration, peer mentoring, and appreciation programs**.

#     """)


#earlier code with new changes


import pickle
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import webbrowser

# Load the trained model
with open("teacher_burnout_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load label encoders
with open("label_encoders.pkl", "rb") as enc_file:
    encoders = pickle.load(enc_file)

# Load feature order
with open("trained_feature_order.pkl", "rb") as feature_file:
    trained_features = pickle.load(feature_file)

# Burnout Level Mapping
burnout_levels = {0: "Low Burnout", 1: "Moderate Burnout", 2: "High Burnout"}

# Streamlit UI Design
st.set_page_config(page_title="Teacher Burnout Predictor", page_icon="📊", layout="centered")

# Sidebar Navigation
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Go to", ["Predict Burnout", "About Burnout","Community"])
# Sidebar Details
st.sidebar.markdown("---")
st.sidebar.subheader("📌 Model Details")
st.sidebar.markdown("""
- **Model Used:** XGBoost Classifier  
- **Key Features Considered:** Psychological, Work, and Social Factors  
""")

st.sidebar.subheader("📊 Prediction Insights")
st.sidebar.markdown("""
- **Low Burnout:** Healthy work-life balance, manageable stress.  
- **Moderate Burnout:** Increased stress, may need intervention.  
- **High Burnout:** Critical state, requires urgent action.  
""")


if page == "Predict Burnout":
    st.markdown("<h1 style='text-align: center; color: #ff6347;'>📊 Teacher Burnout Predictor</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: black;'>Model: TeacherBurnoutPredictor_Xg</h4>", unsafe_allow_html=True)

    # User Inputs
    st.markdown("<h3 style='color: #4682B4;'>📝 Enter Teacher Data</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        country = st.text_input("🌍 Country")
        employment_type = st.selectbox("🏫 Employment Type", ["Full-time", "Part-time"])
        # occupation = st.text_input("👩‍🏫 Occupation")
        occupation ="Teacher"
        work_from_home = st.selectbox("🏠 Work From Home", ["Yes", "No"])

    with col2:
        partnership_status = st.text_input("💑 Partnership Status (Single/Married/Other)")
        subjective_income = st.slider("💰 Subjective Income Level", 1, 5)
        happiness = st.slider("😊 Happiness Level", 1, 5)

    st.markdown("---")

    # More Inputs
    st.markdown("<h4 style='color: #FFA500;'>📊 Psychological Factors</h4>", unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        hard_concentrate_work = st.slider("🧠 Difficulty Concentrating on Work", 1, 5)
        loneliness = st.slider("😔 Loneliness Level", 1, 5)

    with col4:
        feeling_rejected = st.slider("🚫 Feeling Rejected", 1, 5)

    st.markdown("---")
    st.markdown("<h4 style='color: #FF4500;'>📊 Work & Performance Factors</h4>", unsafe_allow_html=True)

    col5, col6 = st.columns(2)

    with col5:
        travel_time = st.slider("🚗 Daily Travel Time (Minutes)", 0, 120, 30)
        workload = st.slider("📚 Weekly Workload (Hours)", 10, 80, 40)

    with col6:
        performance_pressure = st.slider("⚡ Performance Pressure Level", 1, 5, 3)


    # Convert categorical inputs
    input_data = {
        "Country": country,
        "EmploymentType": employment_type,
        "Occupation": occupation,
        "WorkFromHome": work_from_home,
        "HardConcentrateWork": hard_concentrate_work,
        "lonely3": loneliness,
        "FeelingRejected": feeling_rejected,
        "SubjectiveIncome": subjective_income,
        "Happiness": happiness,
        "PartnershipStatus": partnership_status,
    }
    input_data.update({
        "TravelTime": travel_time,
        "WorkLoad": workload,
        "PerformancePressure": performance_pressure
    })

    # Encode categorical features
    for col in encoders:
        if col in input_data:
            if input_data[col] in encoders[col].classes_:
                input_data[col] = encoders[col].transform([input_data[col]])[0]
            else:
                input_data[col] = 0  # Assign unknown categories to 0

    # Convert to DataFrame and ensure correct column order
    input_df = pd.DataFrame([input_data])
    input_df = input_df.reindex(columns=trained_features, fill_value=0)


   # Prediction Button
    if st.button("🔍 Predict Burnout Level"):
    # Get initial prediction probabilities
        burnout_prob = model.predict_proba(input_df)[0]  # Get class probabilities

        # Normalize Factors
        workload_factor = min(workload / 80, 1)  # Normalize to 0-1 scale
        travel_factor = min(travel_time / 120, 1)  # Normalize to 0-1 scale
        pressure_factor = performance_pressure / 5  # Already 0-1 scale

        # Weighted Stress Contribution
        stress_score = (workload_factor * 0.4) + (travel_factor * 0.25) + (pressure_factor * 0.35)  

        # Adjust the burnout probability dynamically
        burnout_prob[2] += stress_score * 0.3  # Increase High Burnout based on stress
        burnout_prob[1] += stress_score * 0.2  # Increase Moderate Burnout slightly

        # Normalize probabilities so they sum to 1
        burnout_prob /= burnout_prob.sum()

        # Get new predicted class
        predicted_label = burnout_levels[np.argmax(burnout_prob)]

    # Display Adjusted Burnout Level
        if predicted_label == "Low Burnout":
           st.success(f"✅ **Predicted Burnout Level: {predicted_label}** 🟢")

        elif predicted_label == "Moderate Burnout":
            st.warning(f"⚠️ **Predicted Burnout Level: {predicted_label}** 🟡")

        else:
            st.error(f"🚨 **Predicted Burnout Level: {predicted_label}** 🔴")

            # # If High Burnout, provide additional support resources
            # st.subheader("🚨 Urgent Support Resources Near You")
    
            # # Get user location
            # user_location = st.text_input("📍 Enter your City & Country for nearby resources:")

            
            # # Button to trigger the search
            # if st.button("🔍 Find Support Centers"):
            #     if user_location:
            #         search_query = f"https://www.google.com/search?q=Meditation+centers+Yoga+instructors+Psychiatrists+near+{user_location.replace(' ', '+')}"
        
           

            # #Display the Clickable Link
            #         st.markdown(f"🔍 [Find Nearby Support Centers]({search_query})", unsafe_allow_html=True)
            #     else:
            #         st.warning("⚠️ Please enter your city and country to find resources.")




        st.markdown("### 🛠 Personalized Solutions to Reduce Burnout")
        solutions = {
            "Low Burnout": [
            "✅ **Maintain Work-Life Balance:** Set clear boundaries between work and personal life to prevent burnout.",
            "✅ **Engage in Continuous Learning:** Explore new teaching strategies or take professional development courses.",
            "✅ **Incorporate Relaxation Techniques:** Practice mindfulness, deep breathing, or light exercise to stay energized.",
            "✅ **Build a Support Network:** Connect with fellow teachers to share experiences and best practices."
        ],
            "Moderate Burnout": [
            "⚠️ **Prioritize Self-Care:** Ensure you get enough rest, hydration, and nutritious meals to maintain energy levels.",
            "⚠️ **Delegate When Possible:** Reduce workload by collaborating with colleagues or using teaching assistants.",
            "⚠️ **Seek Support:** Reach out to mentors, teacher communities, or school counselors for guidance.",
            "⚠️ **Time Management Techniques:** Use scheduling tools or lesson planning templates to manage workload efficiently.",
            "⚠️ **Engage in Reflective Teaching:** Identify stressors and adjust teaching methods to improve well-being."
        ],
            "High Burnout": [
            "🚨 **Consider Professional Help:** Consult a therapist or counselor specializing in teacher burnout.",
            "🚨 **Take a Break:** If possible, use personal leave or mental health days to rest and recharge.",
            "🚨 **Communicate with Administration:** Discuss workload adjustments, flexible schedules, or additional support.",
            "🚨 **Reduce Non-Teaching Tasks:** Minimize excessive paperwork and administrative duties to focus on teaching.",
            "🚨 **Join a Teacher Support Group:** Engage with peer groups or online communities to share challenges and solutions."
        ]
    }
        
        for solution in solutions[predicted_label]:
            st.write(solution)

elif page == "About Burnout":
    st.markdown("<h1 style='text-align: center; color: #4682B4;'>📖 Understanding Teacher Burnout</h1>", unsafe_allow_html=True)
    st.markdown("""
    **Why is Teacher Burnout Important?**
    - Teacher burnout affects job satisfaction, mental health, and student outcomes.
    - High burnout leads to increased absenteeism and teacher turnover.
    - Preventing burnout improves teaching quality and workplace well-being.
    
    **Factors Considered in Prediction:**
    - **Work Environment**: Employment type, work-from-home status, occupation.
    - **Psychological Well-being**: Stress levels, happiness, difficulty concentrating.
    - **Social & Financial Factors**: Income level, loneliness, feeling rejected, partnership status.
    
    **How Does This Model Help?**
    - Identifies high-risk teachers early.
    - Provides actionable solutions based on prediction.
    - Encourages schools to implement support measures.
    """, unsafe_allow_html=True)

    # Feature importance data
    features = ["FeelingRejected", "Happiness", "Lonely3", "Country", "PartnershipStatus", "EmploymentType", "SubjectiveIncome", "HardConcentrateWork", "WorkFromHome", "Occupation"]
    importance = [0.305, 0.141, 0.109, 0.084, 0.066, 0.064, 0.058, 0.058, 0.057, 0.050]

    # Feature Importance Chart
    st.subheader("Feature Importance in Burnout Prediction")
    fig, ax = plt.subplots()
    y_pos = np.arange(len(features))
    ax.barh(y_pos, importance, align='center', color='skyblue')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(features)
    ax.invert_yaxis()
    ax.set_xlabel("Importance Score")
    ax.set_title("Feature Importance in XGBoost Model")
    st.pyplot(fig)

    # Observations
    
    # Key Observations
    st.subheader("Key Observations")
    st.markdown("""
    - **FeelingRejected (30.5%)** is the strongest predictor. Teachers who feel rejected are at the highest risk of burnout.
      - ✅ **Actionable Insight:** Schools should focus on **inclusion, social support, and community-building** strategies.
    - **Happiness (14.1%) & Loneliness (10.9%)** are highly influential.
      - ✅ **Actionable Insight:** Encouraging **peer interactions, social events, and mental health support** could help mitigate burnout.
    - **Country (8.4%)** suggests burnout differs across regions due to education policies and workloads.
    - **Employment Type & Partnership Status (6.4%-6.6%)** indicate **personal and work stability** matter.
    - **WorkFromHome (5.7%) & HardConcentrateWork (5.8%)** affect burnout, possibly due to isolation or work struggles.
    """)

    # What This Means
    st.subheader("🤔 What Does This Mean?")
    st.markdown(""" 
    ✅ **Emotional & Social Factors** (FeelingRejected, Happiness, Loneliness) dominate. Addressing these is key.
    ✅ **Systemic & Financial Factors** (Employment Type, Income, Country) also matter. Policy changes could help.
    ✅ **Work Environment** (WorkFromHome, HardConcentrateWork) plays a role. Improving workplace conditions may help.
    """)

    # Recommendations
    st.subheader("🛠 Recommendations")
    st.markdown("""
    ### **1. Individual-Level Strategies (Teacher Well-Being)**
    - 🧠 **Mental Health Support:** Schools should provide **counseling services** and mental health resources.
    - 👥 **Social Support Networks:** Encourage **peer support groups** to reduce loneliness and rejection.
    - ⚖ **Work-Life Balance:** Promote **flexible work arrangements**, like hybrid teaching options.
    - 🧘 **Stress Management Programs:** Offer **mindfulness and stress training** to improve resilience.

    ### **2. Organizational & Policy-Level Strategies**
    - 📚 **Better Work Policies:** Schools should **reduce excessive workloads** and offer mental health days.
    - 💰 **Financial & Job Stability:** Improving **teacher salaries and employment security** can reduce burnout risk.
    - 🏫 **Inclusive School Culture:** Schools should foster **collaboration, peer mentoring, and appreciation programs**.

    """)


elif page == "Community":

    # Custom CSS for styling cards
    st.markdown("""
        <style>
        .card {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }
        .card h4 {
            margin-bottom: 5px;
            color: #333;
        }
        .card p {
            margin: 5px 0;
            font-size: 14px;
        }
        .highlight {
            font-weight: bold;
            color: #d63384;
        }
        </style>
    """, unsafe_allow_html=True)

# Dummy Data - To be replaced later with FastAPI & MERN Stack
    community_data = [
    {"name": "👩‍🏫 Teena Trivedi", "burnout_level": "🟢 Low", "message": "Daily mindfulness and exercise help me stay balanced."},
    {"name": "👩‍🏫 Silviya Dmonte", "burnout_level": "🟠 Moderate", "message": "I talk to my colleagues and take short breaks."},
    {"name": "👨‍🏫 Shivam Shukla", "burnout_level": "🔴 High", "message": "I am seeking professional help and self-care."},
    {"name": "👨‍🏫 Rohan Mehta", "burnout_level": "🟢 Low", "message": "Maintaining a work-life balance and pursuing hobbies keeps me stress-free."},
    {"name": "👩‍🏫 Ananya Roy", "burnout_level": "🟠 Moderate", "message": "I practice deep breathing exercises and yoga for relaxation."},
    {"name": "👨‍🏫 Arvind Desai", "burnout_level": "🔴 High", "message": "Talking to a therapist and getting social support has helped me recover."}
]

    # 🌟 Community Support Section
    st.markdown("<h2 style='text-align: center;'>🏫 Teacher Community Support</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>A space where teachers share experiences and strategies to manage burnout.</p>", unsafe_allow_html=True)

    st.markdown("---")

    # Displaying teacher messages in an enhanced card UI
    for teacher in community_data:
        st.markdown(f"""
            <div class="card">
                <h4> {teacher['name']} - Burnout Level: <span class="highlight">{teacher['burnout_level']}</span></h4>
                <p>💬 {teacher['message']}</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # 🚀 Future Feature Section
    st.subheader("🚀 Upcoming Community Features")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("🔹 **Discussion Forum** - Connect with fellow teachers.")
        st.markdown("🔹 **Peer Network** - Personalized support from experienced educators.")
    with col2:
        st.markdown("🔹 **Live Webinars & Workshops** - Learn burnout management strategies.")
        st.markdown("🔹 **Resource Library** - Access guides and research on burnout.")

    st.info("These features will be implemented in the full version using FastAPI & MERN Stack. Stay tuned! 🎉")




