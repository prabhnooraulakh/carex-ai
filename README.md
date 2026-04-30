<<<<<<< HEAD
# CareX AI 🩺

AI-Powered Healthcare Assistant built with Streamlit and OpenAI.

## Features
- **AI-Powered Responses**: Uses OpenAI GPT to provide health guidance
- **Simple Interface**: Easy-to-use Streamlit web app
- **Quick Feedback**: Real-time symptom analysis

## Setup

### Local Development
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set your OpenAI API key:
   ```bash
   setx OPENAI_API_KEY "your-api-key-here"
   ```
5. Run the app:
   ```bash
   streamlit run app.py
   ```

## Deployment to Streamlit Cloud

1. Push this repository to GitHub
2. Visit https://share.streamlit.io
3. Click "New app"
4. Connect your GitHub repository
5. Select the repository, branch, and `app.py` as the main file
6. In App settings, add the secret:
   - Key: `OPENAI_API_KEY`
   - Value: Your actual OpenAI API key
7. Click "Deploy"

## Disclaimer
⚠️ This is not a substitute for professional medical advice. Always consult a healthcare provider for serious conditions.

## Technologies
- **Streamlit**: Web framework
- **OpenAI**: AI model for responses
- **Python**: Programming language
=======
# carex-ai
>>>>>>> 23e47436e37f23504dbe44f5aec67eca34c83de5
