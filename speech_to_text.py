import speech_recognition as sr
import speak

def speech_to_text():
    """
    Convert speech to text using Google Speech Recognition
    """
    r = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            print("Listening... Please speak now.")
            speak.speak("I am listening")
            
            # Adjust for ambient noise
            r.adjust_for_ambient_noise(source, duration=1)
            
            # Listen for audio input
            audio = r.listen(source, timeout=10, phrase_time_limit=5)
            
            print("Processing speech...")
            
        # Use Google Speech Recognition
        voice_data = r.recognize_google(audio)
        print(f"You said: {voice_data}")
        return voice_data.lower()
        
    except sr.UnknownValueError:
        error_msg = "Sorry, I couldn't understand what you said"
        print(error_msg)
        speak.speak(error_msg)
        return ""
        
    except sr.RequestError as e:
        error_msg = "No internet connection. Please turn on your internet"
        print(f"Request error: {e}")
        speak.speak(error_msg)
        return ""
        
    except sr.WaitTimeoutError:
        error_msg = "No speech detected. Please try again"
        print(error_msg)
        speak.speak(error_msg)
        return ""
        
    except Exception as e:
        error_msg = f"An error occurred: {str(e)}"
        print(error_msg)
        speak.speak("An error occurred while processing speech")
        return ""

def continuous_speech_recognition():
    """
    Continuous speech recognition - keeps listening until user says "stop" or "quit"
    """
    r = sr.Recognizer()
    
    print("Starting continuous speech recognition...")
    print("Say 'stop listening' or 'quit' to end.")
    speak.speak("Starting continuous speech recognition. Say stop listening or quit to end.")
    
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=2, phrase_time_limit=5)
                
            voice_data = r.recognize_google(audio).lower()
            print(f"You said: {voice_data}")
            
            # Check for stop commands
            if "stop listening" in voice_data or "quit" in voice_data or "exit" in voice_data:
                speak.speak("Stopping speech recognition")
                break
                
            # Process the command (you can integrate with Action.py here)
            return voice_data
            
        except sr.UnknownValueError:
            print("Could not understand audio")
            continue
            
        except sr.RequestError as e:
            print(f"Request error: {e}")
            speak.speak("Internet connection error")
            break
            
        except sr.WaitTimeoutError:
            print("No speech detected, continuing to listen...")
            continue
            
        except KeyboardInterrupt:
            print("Speech recognition stopped by user")
            speak.speak("Speech recognition stopped")
            break
            
        except Exception as e:
            print(f"Error: {e}")
            continue

def test_microphone():
    """
    Test if microphone is working
    """
    r = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            print("Testing microphone... Say something!")
            speak.speak("Testing microphone, please say something")
            
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=5)
            
        text = r.recognize_google(audio)
        print(f"Microphone test successful! You said: {text}")
        speak.speak(f"Microphone working! You said {text}")
        return True
        
    except Exception as e:
        print(f"Microphone test failed: {e}")
        speak.speak("Microphone test failed")
        return False

def list_microphones():
    """
    List available microphones
    """
    print("Available microphones:")
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"Microphone {index}: {name}")

# Configuration settings
def configure_recognition_settings():
    """
    Configure speech recognition settings
    """
    r = sr.Recognizer()
    
    # Adjust recognition sensitivity
    r.energy_threshold = 4000  # Minimum audio energy to consider for recording
    r.dynamic_energy_threshold = True  # Automatically adjust energy threshold
    r.pause_threshold = 0.8  # Seconds of silence before considering phrase complete
    r.phrase_threshold = 0.3  # Minimum seconds of speaking audio before we consider the speaking audio a phrase
    r.non_speaking_duration = 0.8  # Seconds of silence to keep on both sides of the recording
    
    return r

# Main execution for testing
if __name__ == "__main__":
    print("Speech Recognition Test")
    print("1. Testing microphone...")
    
    if test_microphone():
        print("2. Testing single speech recognition...")
        result = speech_to_text()
        if result:
            print(f"Speech recognition successful: {result}")
        
        print("3. Available microphones:")
        list_microphones()
    else:
        print("Please check your microphone connection and try again.")