# TITAN: Tech-based Interactive Task & Assistant Network

<p align="center">
  <img src="https://github.com/user-attachments/assets/83d9def8-6d93-480e-bba9-570faed3dc77">
</p>
  
TITAN is a voice assistant that can perform various tasks such as answering questions, providing weather updates, fetching news, and more. It utilizes speech recognition, NLP, and API integrations to enhance user interactions.

## Features
- **Speech Recognition**: Converts voice commands into text.
- **Text-to-Speech (TTS)**: Responds using synthesized speech.
- **AI Chat**: Uses Google's Gemini AI for conversational responses.
- **Weather Updates**: Fetches real-time weather data.
- **News Fetching**: Retrieves the latest news articles on various topics.

## Installation
### Prerequisites
Ensure you have Python installed (version 3.7 or later). Then, install the required dependencies:

```bash
pip install speechrecognition pyaudio pyttsx3 google-generativeai requests spacy
python -m spacy download en_core_web_sm
```

## Configuration
This project requires API keys for Google Gemini AI, OpenWeather, and NewsAPI. Replace the placeholders in `TITAN.py` with your actual API keys:

```python
client = genai.Client(api_key="YOUR_GEMINI_API_KEY")
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
API_KEY = "YOUR_WEATHER_API_KEY"
```

## Usage
Run the script to start the assistant:

```bash
python TITAN.py
```

TITAN will greet you and wait for voice commands. You can ask for weather updates, news, or general queries.

## Example Commands
- "What's the weather in New York?"
- "Give me the latest news on technology."
- "Who is the president of the United States?"
- "Exit" (to stop the assistant)

## License
This project is licensed under the MIT License.

## Acknowledgements
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [PyAudio](https://pypi.org/project/PyAudio/)
- [Google Generative AI](https://ai.google.dev/)
- [OpenWeather API](https://openweathermap.org/api)
- [NewsAPI](https://newsapi.org/)

