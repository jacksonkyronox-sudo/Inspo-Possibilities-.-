from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def build_image_urls(profession, location):
    """Build a small set of lifestyle image URLs based on the dream profession and place."""
    text_values = [
        f"{profession} lifestyle",
        f"{location} lifestyle",
        f"{profession} in {location}",
        f"modern life in {location}"
    ]

    def make_svg_data_url(text):
        svg = f'''
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#667eea" />
      <stop offset="100%" stop-color="#764ba2" />
    </linearGradient>
  </defs>
  <rect width="1200" height="800" fill="url(#grad)" />
  <rect x="40" y="40" width="1120" height="720" rx="40" fill="rgba(255,255,255,0.16)" />
  <text x="600" y="360" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="48" fill="#ffffff">{text}</text>
  <text x="600" y="440" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="28" fill="#f3f4f6">Dream life in {location}</text>
</svg>'''
        return f"data:image/svg+xml;charset=UTF-8,{quote(svg, safe='')}"

    return [make_svg_data_url(text) for text in text_values]


def generate_future_narrative(age, profession, location, year):
    """Generate an AI narrative about the user's potential future"""
    
    prompt = f"""You are a creative storyteller who generates inspiring future narratives. 
    
Based on the following information, create a vivid, detailed narrative about what this person's life might look like in the future. Make it personal, inspiring, and grounded in reality. 

User Information:
- Current Age: {age} years old
- Dream Profession: {profession}
- Dream Location to Live: {location}
- Target Year to Explore: {year}
- Years from Now: {int(year) - 2026} years

Please write a narrative in 2-3 paragraphs that:
1. Paints a vivid picture of what a typical day or moment looks like in {year} at the location {location}
2. Shows them working in or related to their dream profession ({profession})
3. Connects their current age ({age}) to their achievements in {year}
4. Includes sensory details, emotions, and realistic challenges
5. Ends with one memorable, inspiring closing line that resonates with their journey

Format: Write the narrative in an engaging, storybook style. Start with a scene-setting element like the date and location. Make it feel real and achievable. End with a single powerful sentence that captures the essence of making this future possible.

Possible memorable closing lines (use your own):
- "The future isn't written. But today's choices are."
- "You close the day with gratitude, knowing this life began with one small decision years ago."
- "And in this moment, you remember: this was always possible."

Remember: This should feel like a real glimpse into a possible future, not a fairy tale. Include small, authentic details that make the narrative believable."""
    
    model = genai.GenerativeModel("gemini-2.5-flash-lite")
    response = model.generate_content(prompt)
    
    return response.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        age = data.get('age')
        profession = data.get('profession')
        location = data.get('location')
        year = data.get('year')
        
        # Validation
        if not all([age, profession, location, year]):
            return jsonify({'error': 'All fields are required'}), 400
        
        try:
            age = int(age)
            year = int(year)
            
            if age < 5 or age > 120:
                return jsonify({'error': 'Please enter a valid age between 5 and 120'}), 400
            
            if year <= 2026:
                return jsonify({'error': 'Please enter a year in the future (after 2026)'}), 400
            
            # Calculate how old they would be in the target year
            future_age = age + (year - 2026)
            if future_age > 150:
                return jsonify({'error': f'You would be {future_age} years old in {year}. Please choose a more reasonable target year.'}), 400
                
        except ValueError:
            return jsonify({'error': 'Age and year must be valid numbers'}), 400
        
        # Generate narrative and visual inspiration
        narrative = generate_future_narrative(age, profession, location, year)
        image_urls = build_image_urls(profession, location)
        
        return jsonify({
            'success': True,
            'narrative': narrative,
            'images': image_urls,
            'metadata': {
                'age': age,
                'profession': profession,
                'location': location,
                'year': year
            }
        })
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
