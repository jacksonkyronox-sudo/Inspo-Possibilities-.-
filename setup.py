#!/usr/bin/env python3
"""
Quick setup script for Future Narrator
This script helps you set up and run the application
"""

import os
import subprocess
import sys
import platform

def print_header(text):
    print("\n" + "="*50)
    print(f"  {text}")
    print("="*50 + "\n")

def check_python():
    """Check if Python 3.8+ is installed"""
    print_header("Checking Python Version")
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ is required")
        return False
    print("✓ Python version is compatible")
    return True

def install_dependencies():
    """Install required packages"""
    print_header("Installing Dependencies")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def setup_env():
    """Set up .env file"""
    print_header("Setting Up Environment Variables")
    
    if os.path.exists(".env"):
        print("✓ .env file already exists")
        return True
    
    if not os.path.exists(".env.example"):
        print("❌ .env.example not found")
        return False
    
    # Copy example to .env
    with open(".env.example", "r") as f:
        content = f.read()
    
    with open(".env", "w") as f:
        f.write(content)
    
    print("✓ Created .env file from template")
    print("\n📝 Please edit .env and add your Anthropic API key:")
    print("   ANTHROPIC_API_KEY=your_actual_key_here")
    print("\n   Get your key at: https://console.anthropic.com/")
    
    return True

def run_app():
    """Run the Flask application"""
    print_header("Starting Future Narrator App")
    print("🚀 App starting on http://localhost:5000")
    print("🌐 Open your browser and navigate to: http://localhost:5000")
    print("\nPress Ctrl+C to stop the server\n")
    
    try:
        subprocess.call([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n\n✓ App stopped")

def main():
    print("\n" + "🔮 "*10)
    print("   FUTURE NARRATOR - Quick Setup")
    print("🔮 "*10)
    
    # Check Python
    if not check_python():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Setup .env
    if not setup_env():
        print("⚠️  Warning: Could not set up .env file automatically")
        print("   Please create it manually before running the app")
    
    # Check if API key is set
    if not os.path.exists(".env") or "your_google_gemini_api_key_here" in open(".env").read():
        print("\n" + "!"*50)
        print("⚠️  IMPORTANT: You must add your Google Gemini API key to .env")
        print("!"*50)
        print("\nGet a FREE API key (no credit card required) at:")
        print("   https://aistudio.google.com/app/apikey")
        response = input("\nContinue without API key? (not recommended) [y/N]: ")
        if response.lower() != 'y':
            print("Please set up your API key and run the app again")
            sys.exit(1)
    
    # Run app
    run_app()

if __name__ == "__main__":
    main()
