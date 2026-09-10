
# Vitiligo Assessment System

A comprehensive web-based application for vitiligo detection and risk assessment using machine learning, image analysis, and medical questionnaires.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [System Components](#system-components)
- [Key Features in Detail](#key-features-in-detail)
- [Technologies Used](#technologies-used)
- [Configuration](#configuration)
- [API & Services](#api--services)
- [Report Generation](#report-generation)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

The **Vitiligo Assessment System** is an intelligent diagnostic tool designed to assist in the early detection and assessment of vitiligo. It combines multiple diagnostic approaches including:

- **Medical Questionnaires**: Comprehensive patient history and lifestyle assessments
- **Image-Based Analysis**: AI-powered skin image analysis using deep learning
- **Risk Prediction**: Machine learning models to predict vitiligo risk levels
- **Automated Reporting**: PDF report generation with detailed analysis and visualizations
- **Email Delivery**: Secure report distribution via email

This system is built as a Streamlit web application, making it accessible and user-friendly for both healthcare professionals and patients.

## ✨ Features

### 1. **Multi-Dimensional Assessment**
   - Personal and family history evaluation
   - Diet and nutritional analysis
   - Lifestyle factor assessment
   - Psychological impact evaluation
   - Environmental exposure analysis
   - Vitiligo progression tracking

### 2. **AI-Powered Image Analysis**
   - ResNet-based deep learning model for skin lesion classification
   - Advanced image enhancement techniques:
     - Wood's Lamp effect simulation
     - Grayscale conversion for better lesion visibility
     - Heatmap generation for potential vitiligo regions
   - Real-time image processing and visualization

### 3. **Risk Prediction**
   - Machine learning-based risk level prediction
   - Multi-factor analysis combining all assessment dimensions
   - Confidence scoring for predictions

### 4. **Intelligent Reporting**
   - Automated PDF report generation
   - Visual pie charts showing assessment scores
   - Detailed patient information and analysis
   - Integration with enhanced image visualizations
   - Email delivery functionality

### 5. **Patient Management**
   - Patient information collection (name, age, gender, date)
   - Session state management for continuous workflow
   - Secure data handling

## 📁 Project Structure

```
vitiligo-assessment-system/
├── main.py                          # Main Streamlit application
├── requirements.txt                 # Python dependencies
├── config.py                        # Configuration settings
├── core/
│   ├── questionnaire/
│   │   ├── questions.py            # Question definitions and categories
│   │   ├── scoring.py              # Scoring algorithms for each section
│   │   ├── analysis.py             # Analysis and type determination
│   │   └── visualization.py        # Chart and visualization generation
│   ├── prediction/
│   │   └── risk_predictor.py       # ML-based risk prediction model
│   └── image_analysis/
│       ├── image_pipeline.py       # Image processing pipeline
│       ├── model_loader.py         # Deep learning model loading
│       └── enhancement.py          # Image enhancement techniques
├── services/
│   ├── pdf_service.py              # PDF report generation
│   └── email_service.py            # Email delivery service
└── temp/                           # Temporary storage for generated images
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/jmandar10k/vitiligo-assessment-system.git
   cd vitiligo-assessment-system
   ```

2. **Create Virtual Environment** (Optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Update `config.py` with your settings (email credentials, model paths, etc.)

5. **Run the Application**
   ```bash
   streamlit run main.py
   ```

The application will be available at `http://localhost:8501`

## 📖 Usage

### Step-by-Step Workflow

1. **Complete Personal & Family History Assessment**
   - Answer questions about your medical background
   - Provide family history information
   - Get family history risk score

2. **Diet Assessment**
   - Select food items consumed
   - Specify consumption frequency
   - Answer digestive questions
   - Receive diet-related risk score

3. **Lifestyle Factor Assessment**
   - Evaluate exercise, sleep, and stress levels
   - Answer lifestyle-related questions
   - Get lifestyle risk score

4. **Psychological Assessment**
   - Answer psychological impact questions
   - Evaluate mental health factors
   - Receive psychological risk score

5. **Environmental Factors Assessment**
   - Assess sun exposure and environmental risks
   - Evaluate occupational hazards
   - Get environmental risk score

6. **Vitiligo Lesion Questionnaire**
   - Select characteristics of white patches (if visible)
   - Click "Submit Lesion Assessment"
   - System determines vitiligo type (Generalized, Localized, etc.)

7. **Progression Assessment**
   - Answer questions about vitiligo progression
   - Provide insights on patch characteristics
   - Get detailed progression analysis

8. **Image-Based Analysis**
   - Upload a skin image (JPG, JPEG, PNG)
   - Enable/disable lesion enhancement
   - View AI prediction and confidence score
   - Examine enhanced visualizations:
     - Wood's Lamp effect
     - Grayscale analysis
     - Heatmap of potential vitiligo regions

9. **Risk Prediction**
   - Click "Prepare Report Data" to generate assessment charts
   - Click "Predict Risk Level" to get ML-based risk assessment
   - View predicted risk level (Low, Medium, High, etc.)

10. **Patient Information**
    - Enter patient name, age, gender, and date
    - Required for report generation

11. **Report Generation & Delivery**
    - Click "Download Report" to generate PDF
    - View comprehensive report with all assessments
    - Enter recipient email to send report
    - Click "Send Report" to email the PDF

## 🔧 System Components

### Core Questionnaire Module
Manages all patient assessment questionnaires with:
- Multiple question categories
- Dynamic scoring algorithms
- Type determination logic
- Visualization generation

**Key Files:**
- `core/questionnaire/questions.py` - Defines all questionnaire questions
- `core/questionnaire/scoring.py` - Scoring logic for each assessment
- `core/questionnaire/analysis.py` - Clinical analysis and type determination

### Image Analysis Module
Performs AI-powered skin analysis:
- **ResNet Model**: Pre-trained deep learning model for classification
- **Enhancement Pipeline**: Applies multiple visualization techniques
- **Prediction**: Provides confidence scores for positive/negative predictions

**Key Files:**
- `core/image_analysis/image_pipeline.py` - Main processing pipeline
- `core/image_analysis/model_loader.py` - Model initialization and loading

### Risk Prediction Module
Machine learning-based risk assessment:
- Combines all questionnaire scores
- Uses trained model for prediction
- Returns risk level classification

**Key File:**
- `core/prediction/risk_predictor.py` - Risk level prediction logic

### Services Module
Handles external operations:
- **PDF Service**: Generates comprehensive reports with visualizations
- **Email Service**: Sends reports via email with patient information

**Key Files:**
- `services/pdf_service.py` - PDF generation with fpdf
- `services/email_service.py` - Email delivery configuration

## 📊 Key Features in Detail

### Assessment Scoring System
Each section contributes a score (0-100) based on responses:
- **Family History Score**: Genetic predisposition assessment
- **Diet Score**: Nutritional risk factors
- **Lifestyle Score**: Activity and sleep-related factors
- **Psychological Score**: Mental health and stress impact
- **Environmental Score**: Sun exposure and environmental hazards

**Combined Score**: Weighted average of all section scores

### Vitiligo Type Classification
Based on lesion characteristics:
- **Generalized**: Widespread white patches across body
- **Localized**: Patches confined to specific areas
- **Acrofacial**: Patches on face and hands
- **Segmental**: Distribution on one side of body
- **Mucosal**: Affecting mucous membranes

### Enhanced Image Visualization
Three-layer enhancement for better lesion detection:
1. **Wood's Lamp Effect**: Simulates Wood's lamp examination
2. **Grayscale Conversion**: Improves contrast of white patches
3. **Heatmap**: Highlights regions of potential vitiligo

### PDF Report Generation
Comprehensive reports include:
- Patient demographics
- All assessment scores with pie charts
- Vitiligo type classification
- Image analysis results with visualizations
- Risk level prediction
- Clinical insights and recommendations
- Date and timestamp

### Email Integration
Secure report delivery with:
- Automated email sending
- Patient name personalization
- PDF attachment
- Error handling and notifications

## 🛠️ Technologies Used

### Backend & Framework
- **Streamlit**: Web application framework for rapid UI development
- **Python 3.8+**: Core programming language

### Data Processing & ML
- **NumPy**: Numerical computing and array operations
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning algorithms
- **TensorFlow**: Deep learning framework
- **Hugging Face Hub**: Pre-trained model management

### Image Processing
- **OpenCV**: Computer vision operations
- **Pillow (PIL)**: Image manipulation and format handling

### Visualization & Reporting
- **Matplotlib**: Chart and graph generation
- **FPDF**: PDF document creation

### External Services
- **SMTP Email**: Email delivery via SMTP protocol

## ⚙️ Configuration

### config.py
Configure the following in `config.py`:

```python
# Email Configuration
SMTP_SERVER = "your-smtp-server.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your-email@example.com"
EMAIL_PASSWORD = "your-app-password"

# Model Configuration
MODEL_NAME = "model-name"
MODEL_PATH = "./models/"
CONFIDENCE_THRESHOLD = 0.5

# Application Settings
TEMP_IMAGE_PATH = "./temp/"
REPORT_SAVE_PATH = "./reports/"
```

### Requirements
All dependencies are listed in `requirements.txt`:
- streamlit
- numpy
- pandas
- matplotlib
- fpdf
- opencv-python-headless
- pillow
- scikit-learn
- tensorflow
- huggingface_hub

## 📧 API & Services

### PDF Service
```python
from services.pdf_service import generate_vitiligo_report

report_data = {
    "patient_name": "John Doe",
    "age": 35,
    "gender": "Male",
    "date": "2024-03-10",
    "section_scores": {...},
    "combined_score": 72.5,
    "prediction": "High Risk",
    "vitiligo_type": "Generalized",
    "insights": [...],
    "chart_path": "path/to/chart.png",
    "image_paths": {...}
}

report_path = generate_vitiligo_report(report_data)
```

### Email Service
```python
from services.email_service import send_email

send_email(
    receiver_email="patient@example.com",
    pdf_file="path/to/report.pdf",
    patient_name="John Doe"
)
```

### Risk Predictor
```python
from core.prediction.risk_predictor import predict_vitiligo_risk

risk_level = predict_vitiligo_risk(
    diet_score=65.0,
    environmental_score=55.0,
    lifestyle_score=60.0,
    psychological_score=70.0,
    family_score=80.0,
    combined_score=66.0
)
# Returns: "Low Risk", "Medium Risk", "High Risk", etc.
```

### Image Analysis Pipeline
```python
from core.image_analysis.image_pipeline import run_image_pipeline
from core.image_analysis.model_loader import load_resnet_model

model = load_resnet_model()
result = run_image_pipeline(
    image=image_array,
    model=model,
    apply_enhancement=True
)

# result.prediction.label -> "Vitiligo" or "No Vitiligo"
# result.prediction.score -> Confidence score (0-1)
# result.enhancement -> Enhanced visualization images
```

## 📑 Report Generation

### Report Contents
The generated PDF report includes:

1. **Header Section**
   - Application title and date
   - Patient information (name, age, gender)

2. **Assessment Scores Section**
   - Visual pie chart of all section scores
   - Individual score breakdown:
     - Family History
     - Diet
     - Lifestyle
     - Psychological
     - Environmental
   - Combined Risk Score

3. **Vitiligo Type Classification**
   - Identified vitiligo type based on lesion assessment
   - Classification rationale

4. **Image Analysis Results** (if applicable)
   - Original uploaded image
   - AI prediction (Vitiligo/No Vitiligo)
   - Confidence score
   - Enhanced visualizations:
     - Wood's Lamp effect
     - Grayscale visualization
     - Heatmap

5. **Risk Level Prediction**
   - Overall predicted risk level
   - Risk factors summary

6. **Clinical Insights & Recommendations**
   - Progression insights
   - Clinical conclusions
   - Recommendations for follow-up

7. **Footer**
   - Report generation timestamp
   - Disclaimer

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test all new features
- Update documentation accordingly

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙋 Support & Contact

For questions, bug reports, or suggestions:
- Open an issue on GitHub
- Contact the project maintainer

## ⚠️ Disclaimer

**Important**: This system is designed as a diagnostic aid and should not be considered a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical decisions.

---

**Created with ❤️ for vitiligo awareness and early detection**

Last Updated: 2026
```

---

**Copy the entire content above and paste it directly into your README.md file on GitHub.** This comprehensive README covers:

✅ Project overview and purpose  
✅ Complete feature list  
✅ Installation instructions  
✅ Step-by-step usage guide  
✅ Project structure breakdown  
✅ Technology stack  
✅ API documentation  
✅ Configuration guide  
✅ Contributing guidelines  
✅ Support information  

The README is professional, well-organized, and provides all necessary information for users to understand and use your Vitiligo Assessment System!
