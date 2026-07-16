# 🔮 Share Future Narrator with Your Friends!

A complete guide to get your friends running the app on their own laptops.

---

## 📋 What to Send to Your Friend

Send them these 3 things:

1. **The project folder** - `future-narrator` folder
2. **This guide** - `SHARE_WITH_FRIENDS.md` (this file)
3. **The quick start** - `QUICKSTART.md`

**DO NOT send the `.env` file** (it has your API key!)

---

## 🎯 Instructions for Your Friend

### Step 1: Download/Copy the Project

Get the `future-narrator` folder on their laptop:

**Option A: USB Drive or Cloud (Easiest)**
- Copy entire `future-narrator` folder to a USB drive
- Insert USB on friend's laptop
- Copy folder to their Documents

**Option B: Cloud Storage**
- Zip the `future-narrator` folder
- Upload to Google Drive, Dropbox, or OneDrive
- Friend downloads it

**Option C: GitHub (If you're comfortable)**
- Create a public GitHub repo with the code
- Friend clones it
- (Don't include `.env` file in repo!)

---

## 🚀 Quick Setup for Your Friend (5 Minutes)

### Step 1: Check Python Installation
Open Command Prompt and type:
```bash
python --version
```

Should show: `Python 3.8` or higher

**If Python is not installed:**
- Go to https://www.python.org/downloads/
- Download Python 3.8+
- Install it (check "Add Python to PATH")

### Step 2: Install Dependencies (1 minute)
```bash
cd path\to\future-narrator
pip install -r requirements.txt
```

Example:
```bash
cd "C:\Users\YourFriendName\Documents\future-narrator"
pip install -r requirements.txt
```

### Step 3: Get FREE Google Gemini API Key (2 minutes)
1. Go to: **https://aistudio.google.com/app/apikey**
2. Sign in with their Google account
3. Click "Create API Key"
4. Copy the key

### Step 4: Create .env File (1 minute)
1. In same folder, create a file named `.env`
2. Open it with Notepad
3. Add this line:
   ```
   GOOGLE_API_KEY=their_api_key_here
   ```
4. Replace `their_api_key_here` with the key from Step 3
5. Save file

**OR run these commands:**
```bash
copy .env.example .env
notepad .env
```

### Step 5: Run the App (30 seconds)
```bash
python app.py
```

### Step 6: Open in Browser
Go to: **http://localhost:5000**

### Step 7: Generate Futures! 🎉
Fill in the form and create narratives!

---

## 📝 Simple Copy-Paste Instructions

You can just copy-paste this for your friend:

```
1. Copy future-narrator folder to your computer

2. Open Command Prompt in that folder:
   cd "path\to\future-narrator"

3. Install dependencies:
   pip install -r requirements.txt

4. Get FREE API key at:
   https://aistudio.google.com/app/apikey
   (Sign in with Google, click Create API Key, copy it)

5. Create .env file:
   - Copy .env.example to .env
   - Edit .env with Notepad
   - Replace the placeholder with your API key
   - Save

6. Run:
   python app.py

7. Open browser:
   http://localhost:5000

Done! Enjoy generating futures! 🔮
```

---

## 🎓 Important Things to Tell Your Friend

✅ **It's 100% Free**
- No credit card needed
- Google Gemini free tier is unlimited for this app

✅ **Each Person Needs Their Own API Key**
- They can't use your .env file
- They must get their own key at https://aistudio.google.com/app/apikey

✅ **Keep .env File Private**
- Don't share it with anyone
- It contains their API key
- Only they should use their .env

✅ **Internet Required**
- App needs internet to call Google Gemini API
- Must be connected while using it

✅ **No Installation**
- No special software except Python
- No registration needed (just Google account)
- Uninstall by deleting the folder

---

## ❓ If They Hit Issues

### "ModuleNotFoundError: No module named 'google'"
**Fix:** Make sure you ran `pip install -r requirements.txt`

### "AuthenticationError"
**Fix:** 
- Check .env file has correct API key
- No extra spaces or quotes
- Get new key at https://aistudio.google.com/app/apikey

### "Connection refused"
**Fix:** Make sure `python app.py` is still running

### "Address already in use"
**Fix:** Another app is using port 5000. Edit app.py line 71:
```python
app.run(debug=True, port=5001)  # Change to 5001 or another free port
```

### "Python not found"
**Fix:** Download Python from https://www.python.org/downloads/
Make sure to check "Add Python to PATH" during install

---

## 📞 Support

If your friend has questions:
1. Send them this file: `SHARE_WITH_FRIENDS.md`
2. Send them: `QUICKSTART.md` for quick reference
3. Send them: `README.md` for complete documentation
4. They can also check: `START_HERE.md`

All these files are in the `future-narrator` folder.

---

## 🎁 What Your Friend Gets

A beautiful app that:
- ✨ Creates personalized future narratives
- 🎯 Takes input (age, profession, location, year)
- 🤖 Uses AI to generate stories
- 🎨 Has a beautiful, modern UI
- 📱 Works on any browser
- 💰 Completely free!

---

## 🚀 They're Ready!

Once they follow these steps, they'll have the same app running on their laptop! 

They can:
- Generate as many futures as they want
- Share the app with more friends
- Customize the code (if they know programming)

Enjoy! 🔮✨

---

## 📋 Checklist for Your Friend

- [ ] Got the future-narrator folder
- [ ] Python installed (check: `python --version`)
- [ ] Ran: `pip install -r requirements.txt`
- [ ] Got free API key from https://aistudio.google.com/app/apikey
- [ ] Created .env file with their API key
- [ ] Ran: `python app.py`
- [ ] Opened: http://localhost:5000
- [ ] Generated their first future narrative! 🎉

---

**Questions? Read the files in the future-narrator folder:**
- `START_HERE.md` - Quick overview
- `QUICKSTART.md` - 5-minute setup
- `README.md` - Full documentation

Have fun! 🚀
