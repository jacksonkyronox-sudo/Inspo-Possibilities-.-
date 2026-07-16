# 🔮 Future Narrator

An AI-powered web application that generates personalized future narratives based on your age, dream profession, desired location, and target year. **100% FREE** - Uses Google Gemini's free tier!

## Features

✨ **AI-Powered Narratives** - Uses Google Gemini (FREE tier) to generate creative, inspiring stories about your potential future
🎯 **Personalized** - Customized narratives based on your inputs
🌍 **Location-Based** - Explores your dreams in your desired city/location
📅 **Year-Based** - Projects forward to a specific year you choose
🎨 **Beautiful UI** - Modern, gradient-based interface with smooth animations

## Prerequisites

- Python 3.8+
- Google Gemini API key (FREE - from https://aistudio.google.com/app/apikey)

## Setup Instructions

### 1. Clone/Download the Project
Navigate to the project directory:
```bash
cd future-narrator
```

### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
```

Activate it:
- **Windows**: `venv\Scripts\activate`
- **macOS/Linux**: `source venv/bin/activate`

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root (copy from `.env.example`):
```
GOOGLE_API_KEY=your_actual_api_key_here
```

Get your **FREE** API key from https://aistudio.google.com/app/apikey (No credit card required!)

### 5. Run the Application
```bash
python app.py
```

The app will start on `http://localhost:5000`

### 6. Open in Browser
Navigate to http://localhost:5000 in your web browser

## How to Use

1. **Enter Your Age** - Your current age (5-120 years)
2. **Enter Dream Profession** - What do you want to become? (e.g., Robotics Engineer, Artist, etc.)
3. **Enter Dream Location** - Where do you want to live? (e.g., Tokyo, Japan)
4. **Enter Target Year** - A future year to explore (e.g., 2038)
5. **Generate Story** - Click the button to generate your personalized future narrative

The AI will create a vivid, inspiring narrative about what your life could look like in that year and location, pursuing your dream profession.

## Example

**Input:**
- Age: 15
- Profession: Robotics Engineer
- Location: Tokyo, Japan
- Year: 2038

**Output:**
A narrative describing a day in your life as a robotics engineer in Tokyo in 2038, weaving in your current age, challenges, achievements, and inspiring possibilities.

## Project Structure

```
future-narrator/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .env                  # Your actual environment variables (create this)
└── templates/
    └── index.html        # Frontend HTML/CSS/JavaScript
```

## Technologies Used

- **Backend**: Flask (Python)
- **AI**: Google Gemini API (FREE tier)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Modern gradient-based design with animations
- **Cost**: 100% FREE - No charges, no credit card needed!

## Troubleshooting

### "ModuleNotFoundError: No module named 'flask'"
Solution: Run `pip install -r requirements.txt` in your activated virtual environment

### "APIError" or "Authentication failed"
Solution: Make sure your `.env` file contains a valid `GOOGLE_API_KEY`

### Port 5000 already in use
Solution: Change the port in `app.py` line 71 from `port=5000` to another port like `port=5001`

### Narrative takes too long to generate
The API might be experiencing high load. Give it 30-60 seconds. If it continues, check your API key and internet connection.

## Notes

- The app validates all inputs before making API calls
- Generated narratives are created in real-time and vary each time you generate
- The AI prompt is designed to create realistic, achievable futures, not fantasies
- Your API key is stored locally in the `.env` file and never sent anywhere except to Google
- **Google Gemini FREE tier**: 60 requests per minute - More than enough for this app!

## Future Enhancements

Potential features to add:
- Save/export generated narratives as PDF
- Compare multiple future scenarios
- Share narratives on social media
- History of generated narratives
- Multi-language support
- Mobile app version

## License

Open source - feel free to modify and use!

## Support

If you encounter any issues, check:
1. Your `.env` file is properly configured with `GOOGLE_API_KEY`
2. Python version is 3.8+
3. All dependencies are installed (`pip list`)
4. Your Google Gemini API key is valid (get it free at https://aistudio.google.com/app/apikey)

Enjoy exploring your future! 🚀
