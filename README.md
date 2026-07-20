🔮 Stardance

Type in your age, your dream job, the city you want to end up in, and a year to aim for — Stardance writes you a short story about that future. It's powered by Google Gemini, and it's free to run.

I built this because "picture your future self" always sounded like advice from a poster in a guidance counselor's office. Actually reading a few paragraphs about it hits differently.

What it does
Takes four inputs — age, profession, location, year — and turns them into a short narrative
Runs entirely on Gemini's free tier, so there's no billing to set up
Clean, minimal interface — built to get out of the way and let the story do the work
No two generations are identical — regenerate as many times as you want
Before you start

You'll need:

Python 3.8 or newer
A Gemini API key — grab one free at https://aistudio.google.com/app/apikey (no card required)
Getting it running

1. Get into the project folder

bash
cd stardance

2. (Optional) Set up a virtual environment

bash
python -m venv venv

Then activate it:

Windows: venv\Scripts\activate
macOS/Linux: source venv/bin/activate

3. Install the dependencies

bash
pip install -r requirements.txt

4. Add your API key

Copy .env.example to .env and drop your key in:

GOOGLE_API_KEY=your_actual_api_key_here

5. Start it up

bash
python app.py

6. Open it

Head to http://localhost:5000 in your browser and you're in.

Using it

Fill in:

Age — where you're starting from (5–120)
Dream profession — what you're aiming to become
Dream location — where you picture yourself doing it
Target year — how far out you're looking

Hit generate, and Stardance writes a short scene of that life — grounded enough to feel possible, not a fairy tale.

Example: Age 15, Robotics Engineer, Tokyo, 2038 → a narrative dropping you into a day of that future — the work, the city, the version of you who got there.

Project layout
stardance/
├── app.py                 # Flask backend
├── requirements.txt       # dependencies
├── .env.example            # template for your API key
├── .env                    # your actual key (you create this)
└── templates/
    └── index.html          # the frontend
Built with
Flask for the backend
Google Gemini (free tier) for the writing
HTML/CSS/vanilla JS for the frontend — no framework overhead
$0 — genuinely free, no hidden usage caps that matter for personal use
If something breaks

ModuleNotFoundError: No module named 'flask' → Activate your virtual environment, then pip install -r requirements.txt

Auth or API errors → Double check .env has a real GOOGLE_API_KEY in it, no quotes, no typos

Port 5000 already taken → In app.py, change port=5000 to something else, like 5001

Generation is slow → Give it up to a minute during high load. If it's still stuck, check your key and connection.

A couple of notes
Every input gets validated before it's sent off
Stories are generated fresh each time — regenerate for a different take on the same future
The prompt is tuned to write futures that feel earned, not sci-fi fantasy
Your key stays local in .env — it only ever talks to Google
Gemini's free tier gives you 60 requests/minute, which is more than you'll ever need here
Ideas for later
Export a narrative as a PDF to keep
Compare a few different future scenarios side by side
Share a story straight to social
Keep a running history of past generations
Support for more languages
A mobile version
License

Open source — take it, tweak it, make it yours.

Go see who you're becoming. 🚀
