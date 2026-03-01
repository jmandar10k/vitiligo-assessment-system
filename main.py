import streamlit as st
import numpy as np
from PIL import Image
import cv2
import os

# Questionnaire Imports
from core.questionnaire.questions import (
    FAMILY_HISTORY_QUESTIONS,
    FOOD_CATEGORIES,
    DAY_OPTIONS,
    LIFESTYLE_QUESTIONS,
    PSYCHOLOGICAL_QUESTIONS,
    ENVIRONMENTAL_QUESTIONS,
    PROGRESSION_QUESTIONS,
    PROGRESSION_INSIGHT_QUESTIONS
)

from core.questionnaire.scoring import (
    calculate_family_history_score,
    calculate_food_score,
    calculate_lifestyle_score,
    calculate_psychological_score,
    calculate_environmental_score,
    calculate_combined_score
)

from core.questionnaire.analysis import (
    determine_vitiligo_type,
    generate_insights_and_conclusion
)

from core.questionnaire.visualization import create_pie_chart
from core.prediction.risk_predictor import predict_vitiligo_risk
from core.image_analysis.image_pipeline import run_image_pipeline
from core.image_analysis.model_loader import load_resnet_model
from services.pdf_service import generate_vitiligo_report
from services.email_service import send_email

# -----------------------------------------
# Helper Functions
# -----------------------------------------

def save_temp_image(image_array, filename):
    path = os.path.join("temp", filename)
    os.makedirs("temp", exist_ok=True)
    cv2.imwrite(path, image_array)
    return path


# ==========================
# UI SECTION FUNCTIONS
# ==========================

def family_history_section_ui():

    st.header("Personal and Family History Assessment")

    responses = {}

    for key, data in FAMILY_HISTORY_QUESTIONS.items():

        selected_value = st.radio(
            data["question"],
            options=list(data["options"].keys()),
            format_func=lambda x: data["options"][x]
        )

        responses[key] = selected_value

    return calculate_family_history_score(responses)


def diet_section_ui():

    st.header("Diet Assessment")

    responses = {key: [] for key in FOOD_CATEGORIES.keys()}
    responses["meals_before_digestion"] = None

    for key, data in FOOD_CATEGORIES.items():

        selected_items = st.multiselect(
            f"Select {data['label']}",
            data["items"]
        )

        for item in selected_items:
            days = st.selectbox(
                f"Days consumed for {item}",
                DAY_OPTIONS,
                key=f"{key}_{item}"
            )

            responses[key].append({
                "name": item,
                "days": days
            })

    responses["meals_before_digestion"] = st.radio(
        "Have you consumed meals before digestion?",
        ("Yes", "No")
    )

    return calculate_food_score(responses)


def lifestyle_section_ui():

    st.header("Lifestyle Factor Assessment")

    responses = {}

    for key, data in LIFESTYLE_QUESTIONS.items():

        selected_value = st.radio(
            data["question"],
            options=list(data["options"].keys()),
            format_func=lambda x: data["options"][x],
            key=f"lifestyle_{key}"
        )

        responses[key] = selected_value

    return calculate_lifestyle_score(responses)


def psychological_section_ui():

    st.header("Psychological Assessment")

    responses = {}

    for key, data in PSYCHOLOGICAL_QUESTIONS.items():

        selected_value = st.radio(
            data["question"],
            options=list(data["options"].keys()),
            format_func=lambda x: data["options"][x],
            key=f"psychological_{key}"
        )

        responses[key] = selected_value

    return calculate_psychological_score(responses)

def environmental_section_ui():

    st.header("Environmental Factors Assessment")

    responses = {}

    for key, data in ENVIRONMENTAL_QUESTIONS.items():

        selected_value = st.radio(
            data["question"],
            options=list(data["options"].keys()),
            format_func=lambda x: data["options"][x],
            key=f"environment_{key}"
        )

        responses[key] = selected_value

    return calculate_environmental_score(responses)

#Type
def progression_section_ui():

    st.header("Vitiligo Lesion Questionnaire")

    responses = {}

    for key, data in PROGRESSION_QUESTIONS.items():

        responses[key] = st.multiselect(
            data["label"],
            data["options"],
            key=f"{key}_multiselect"
        )

    vitiligo_type = None

    if st.button("Submit Lesion Assessment", key="submit_button"):

        vitiligo_type = determine_vitiligo_type(responses)

        st.subheader(
            f"Based on your responses, the type of vitiligo is: {vitiligo_type}"
        )

        st.session_state.vitiligo_type = vitiligo_type

    return vitiligo_type

#insights
def progression_insight_section_ui():

    st.header("Vitiligo Progression Questionnaire")

    responses = {}

    white_patches = st.radio(
        PROGRESSION_INSIGHT_QUESTIONS["white_patches"]["label"],
        PROGRESSION_INSIGHT_QUESTIONS["white_patches"]["options"],
        key="white_patches"
    )

    responses["white_patches"] = white_patches

    if white_patches == "Yes":

        for key in list(PROGRESSION_INSIGHT_QUESTIONS.keys())[1:]:

            responses[key] = st.radio(
                PROGRESSION_INSIGHT_QUESTIONS[key]["label"],
                PROGRESSION_INSIGHT_QUESTIONS[key]["options"],
                key=f"insight_{key}"
            )

    if st.button("Submit Progression Assessment", key="progression_submit"):

        if white_patches == "Yes":

            insights, conclusion = generate_insights_and_conclusion(
                responses.get("white_patches"),
                responses.get("patch_shape"),
                responses.get("expanding_patches"),
                responses.get("patch_duration"),
                responses.get("sensations"),
                responses.get("color_change"),
                responses.get("new_patches"),
                responses.get("visibility_in_sunlight")
            )

            st.session_state.insights = insights
            st.session_state.conclusion = conclusion

        else:
            st.session_state.insights = []
            st.session_state.conclusion = "Vitiligo unlikely based on absence of white patches."

    return

#image 

def image_analysis_section():

    st.header("Vitiligo Image-Based Analysis")

    uploaded_file = st.file_uploader(
        "Upload a skin image",
        type=["jpg", "jpeg", "png"]
    )

    apply_enhancement = st.checkbox(
        "Apply lesion enhancement & visualization",
        value=True
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file).convert("RGB")
        image_np = np.array(image)

        st.subheader("Uploaded Image")
        st.image(image_np, channels="RGB")

        model = load_resnet_model()

        with st.spinner("Analyzing image..."):
            result = run_image_pipeline(
                image=image_np,
                model=model,
                apply_enhancement=apply_enhancement
            )

        prediction = result.prediction

        st.subheader("Image Prediction Result")
        st.success(f"{prediction.label}")
        st.write(f"Confidence Score: `{prediction.score:.4f}`")

        # -----------------------------
        # Save images for PDF
        # -----------------------------
        image_paths = {}

        # Save original image
        image_paths["Uploaded Image"] = save_temp_image(image_np, "original.png")

        # Save enhancement images if available
        if result.enhancement is not None:
            image_paths["Wood Lamp Effect"] = save_temp_image(
                result.enhancement.wood_lamp, "wood.png"
            )

            image_paths["Grayscale Image"] = save_temp_image(
                result.enhancement.grayscale, "gray.png"
            )

            image_paths["Heatmap"] = save_temp_image(
                result.enhancement.heatmap, "heatmap.png"
            )

        # Store clean dictionary in session state
        st.session_state.image_paths = image_paths

        # -----------------------------
        # UI Display Enhancement
        # -----------------------------
        if prediction.is_positive and result.enhancement is not None:

            st.subheader("Enhanced Visualization")

            st.image(
                result.enhancement.wood_lamp,
                caption="Wood's Lamp Effect",
                channels="BGR"
            )

            st.image(
                result.enhancement.grayscale,
                caption="Grayscale Image",
                channels="GRAY"
            )

            st.image(
                result.enhancement.heatmap,
                caption="Heatmap of Potential Vitiligo Regions",
                channels="BGR"
            )



# ==========================
# MAIN EXECUTION FLOW
# ==========================

def main():

    st.title("Vitiligo Detection System (Refactored Version)")

    # Run Sections
    family_score = family_history_section_ui()
    diet_score = diet_section_ui()
    lifestyle_score = lifestyle_section_ui()
    psychological_score = psychological_section_ui()
    environmental_score = environmental_section_ui()
    vitiligo_type = progression_section_ui()
    if vitiligo_type:
        st.write("Final Detected Vitiligo Type:", vitiligo_type)
    
    progression_insight_section_ui()
    section_scores = {
        "family": family_score,
        "diet": diet_score,
        "lifestyle": lifestyle_score,
        "psychological": psychological_score,
        "environmental": environmental_score
    }

    combined_score = calculate_combined_score(section_scores)

    #pie chart

    if "chart_path" not in st.session_state:
        st.session_state.chart_path = None

    if st.button("Prepare Report Data"):
        st.session_state.chart_path = create_pie_chart(section_scores)

    if "prediction" not in st.session_state:
        st.session_state.prediction = None

    #prediction

    if st.button("Predict Risk Level"):

        st.session_state.prediction = predict_vitiligo_risk(
        diet_score,
        environmental_score,
        lifestyle_score,
        psychological_score,
        family_score,
        combined_score
    )

    if st.session_state.prediction is not None:
        st.subheader("Predicted Vitiligo Risk Level")
        st.success(st.session_state.prediction)

    image_analysis_section()

    #personal info

    st.header("Patient Information")
    patient_name = st.text_input("Patient Name")
    age = st.number_input("Age", min_value=0, max_value=120, value=30)
    gender = st.selectbox("Gender", ("Male", "Female", "Other"))
    date = st.date_input("Date")

    #download report

    if st.button("Download Report"):

        # Require prediction first
        if "prediction" not in st.session_state or st.session_state.prediction is None:
            st.error("Please click 'Predict Risk Level' before downloading the report.")

        else:

            report_data = {
            "patient_name": patient_name,
            "age": age,
            "gender": gender,
            "date": date,

            "section_scores": section_scores,
            "combined_score": combined_score,
            "prediction": st.session_state.prediction,
            "vitiligo_type": st.session_state.get("vitiligo_type", "Not Assessed"),
            "insights": st.session_state.get("insights", []),
            "conclusion": st.session_state.get("conclusion", None),

            "chart_path": st.session_state.get("chart_path", None),

            # Image result optional
            "image_paths": st.session_state.get("image_paths", {})
        }

            report_path = generate_vitiligo_report(report_data)
            st.session_state.last_generated_report = report_path

            # ------------------------------------------------
# Show Download + Email section if report exists
# ------------------------------------------------

    if "last_generated_report" in st.session_state:

        report_path = st.session_state.last_generated_report

        with open(report_path, "rb") as file:
            st.download_button(
                label="Download Vitiligo Report",
                data=file.read(),
                file_name=report_path,
                mime="application/pdf"
            )

        st.success("Report generated successfully.")

        st.subheader("Send Report via Email")

        receiver_email = st.text_input("Enter recipient email", key="email_input")

        if st.button("Send Report"):

            if not receiver_email:
                st.error("Please enter recipient email.")
            else:
                try:
                    send_email(
                        receiver_email=receiver_email,
                        pdf_file=report_path,
                        patient_name=patient_name
                    )
                    st.success("Email sent successfully!")
                except Exception as e:
                    st.error(f"Email failed: {e}")



    # Display Section Scores
    st.subheader("Section Scores")
    st.write("Family History Score:", family_score)
    st.write("Diet Score:", diet_score)
    st.write("Lifestyle Score:", lifestyle_score)
    st.write("Psychological Score:", psychological_score)
    st.write("Environmental Score:", environmental_score)
    st.subheader("Overall Assessment")
    st.write("Combined Score:", combined_score)


if __name__ == "__main__":
    main()