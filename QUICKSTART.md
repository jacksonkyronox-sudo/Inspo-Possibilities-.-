# ⚡ Quick Start Guide - Future Narrator

Get up and running in 5 minutes with **FREE Google Gemini API!**

## Step 1: Get Your FREE API Key (2 minutes)

1. Go to https://aistudio.google.com/app/apikey
2. Click "Create API Key"
3. Copy the API key
4. **No credit card required!**

## Step 2: Set Up the App (2 minutes)

### Option A: Automatic Setup (Windows)
```bash
python setup.py
```
Then follow the prompts.

### Option B: Manual Setup
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create .env file
copy .env.example .env

# 3. Edit .env and add your API key
# GOOGLE_API_KEY=your_actual_key_here
```

## Step 3: Run the App (1 minute)

```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

## Step 4: Open in Browser

Go to: **http://localhost:5000**

## Done! 🎉

Now you can:
1. Enter your age
2. Enter your dream profession
3. Enter your dream location
4. Enter a target year
5. Click "Generate My Future Story"

Enjoy discovering your future! 🔮

---

## Troubleshooting

**"ModuleNotFoundError: No module named 'google'"**
→ Run: `pip install -r requirements.txt`

**"AuthenticationError"**
→ Check your API key in `.env` file (get a free one at https://aistudio.google.com/app/apikey)

**"Connection refused"**
→ Make sure the app is running with `python app.py`

**"Address already in use"**
→ The port 5000 is in use. Edit app.py line 71 to use a different port like 5001.

## Why Google Gemini?

✅ **Completely FREE** - No credit card needed
✅ **Fast** - Quick responses
✅ **Reliable** - Powered by Google
✅ **Generous limits** - 60 requests/minute is plenty for this app
