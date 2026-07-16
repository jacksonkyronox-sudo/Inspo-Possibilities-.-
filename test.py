#!/usr/bin/env python3
"""
Test script for Future Narrator
Validates that all components are working correctly
"""

import os
import sys

def test_imports():
    """Test if all required packages can be imported"""
    print("Testing imports...")
    
    try:
        import flask
        print("✓ Flask is installed")
    except ImportError:
        print("✗ Flask is not installed")
        return False
    
    try:
        import google.generativeai
        print("✓ Google Generative AI SDK is installed")
    except ImportError:
        print("✗ Google Generative AI SDK is not installed")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✓ python-dotenv is installed")
    except ImportError:
        print("✗ python-dotenv is not installed")
        return False
    
    return True

def test_env():
    """Test if .env file exists and API key is configured"""
    print("\nTesting environment configuration...")
    
    if not os.path.exists(".env"):
        print("✗ .env file not found")
        return False
    
    print("✓ .env file exists")
    
    with open(".env", "r") as f:
        content = f.read()
    
    if "your_google_gemini_api_key_here" in content or not "GOOGLE_API_KEY" in content:
        print("✗ API key not configured in .env")
        return False
    
    print("✓ API key appears to be configured")
    return True

def test_files():
    """Test if all required files exist"""
    print("\nTesting file structure...")
    
    required_files = [
        "app.py",
        "requirements.txt",
        ".env.example",
        "README.md",
        "templates/index.html"
    ]
    
    for file in required_files:
        if not os.path.exists(file):
            print(f"✗ Missing: {file}")
            return False
        print(f"✓ Found: {file}")
    
    return True

def main():
    print("="*50)
    print("  Future Narrator - Test Suite")
    print("="*50)
    print()
    
    results = []
    
    results.append(("File Structure", test_files()))
    results.append(("Dependencies", test_imports()))
    results.append(("Environment", test_env()))
    
    print("\n" + "="*50)
    print("Test Results:")
    print("="*50)
    
    all_passed = True
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{test_name}: {status}")
        if not result:
            all_passed = False
    
    print("\n" + "="*50)
    if all_passed:
        print("✓ All tests passed! Ready to run.")
        print("\nRun the app with: python app.py")
        print("Then open: http://localhost:5000")
    else:
        print("✗ Some tests failed. Please fix the issues above.")
        print("\nFor help, see README.md or QUICKSTART.md")
    
    print("="*50)
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
