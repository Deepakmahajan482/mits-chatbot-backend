import pyttsx3

def speak(text):
    """
    Convert text to speech using pyttsx3
    """
    try:
        engine = pyttsx3.init()
        
        # Get current speech rate
        rate = engine.getProperty('rate')
        
        # Set speech rate (slower for better clarity)
        engine.setProperty('rate', rate - 70)
        
        # Optional: Set voice properties
        voices = engine.getProperty('voices')
        if voices:
            # Use first available voice, you can change index for different voices
            engine.setProperty('voice', voices[0].id)
        
        # Optional: Set volume (0.0 to 1.0)
        volume = engine.getProperty('volume')
        engine.setProperty('volume', volume)
        
        print(f"Speaking: {text}")  # Console output for debugging
        
        # Speak the text
        engine.say(text)
        engine.runAndWait()
        
    except Exception as e:
        print(f"Error in text-to-speech: {e}")
        # Fallback: at least print the text if speech fails
        print(f"TTS Failed - Text was: {text}")

def set_voice_properties(rate_offset=-70, voice_index=0, volume=0.9):
    """
    Set custom voice properties
    rate_offset: negative number makes speech slower
    voice_index: 0 for first voice, 1 for second, etc.
    volume: 0.0 to 1.0
    """
    try:
        engine = pyttsx3.init()
        
        # Set rate
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate + rate_offset)
        
        # Set voice
        voices = engine.getProperty('voices')
        if voices and voice_index < len(voices):
            engine.setProperty('voice', voices[voice_index].id)
        
        # Set volume
        engine.setProperty('volume', volume)
        
        return engine
    except Exception as e:
        print(f"Error setting voice properties: {e}")
        return None

# Test function
if __name__ == "__main__":
    speak("Hello! I am MITS Academy Virtual Assistant. Testing text to speech functionality.")