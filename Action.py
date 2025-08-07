import datetime
import speak
import webbrowser
import weather
import os

def Action(send):   
    data_btn = send.lower()

    if "what is your name" in data_btn:
        speak.speak("my name is virtual Assistant")  
        return "my name is virtual Assistant"

    elif "hello" in data_btn or "hye" in data_btn or "hay" in data_btn: 
        speak.speak("Hey sir, How i can help you!")  
        return "Hey sir, How i can help you!" 

    elif "how are you" in data_btn:
        speak.speak("I am doing great these days sir") 
        return "I am doing great these days sir"   

    elif "thanku" in data_btn or "thank" in data_btn:
        speak.speak("its my pleasure sir to stay with you")
        return "its my pleasure sir to stay with you"      

    elif "good morning" in data_btn:
        speak.speak("Good morning sir, i think you might need some help")
        return "Good morning sir, i think you might need some help"   

    elif "time now" in data_btn:
        current_time = datetime.datetime.now()
        Time = (str)(current_time.hour) + " Hour : " + (str)(current_time.minute) + " Minute" 
        speak.speak(Time)
        return str(Time) 

    elif "shutdown" in data_btn or "quit" in data_btn:
        speak.speak("ok sir")
        return "ok sir"  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")   
        speak.speak("gaana.com is now ready for you, enjoy your music")                   
        return "gaana.com is now ready for you, enjoy your music"

    elif 'open google' in data_btn or 'google' in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")  
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open") 
        return "YouTube open"    
    
    elif 'weather' in data_btn or "open weather" in data_btn:
        ans = weather.Weather()
        speak.speak(ans) 
        return ans

    elif 'music from my laptop' in data_btn or "open song" in data_btn:
        # Updated path - change this to your music folder
        music_path = 'C:\\Users\\Public\\Music'  # Default Windows music folder
        try:
            if os.path.exists(music_path):
                songs = os.listdir(music_path)
                if songs:
                    # Filter for music files
                    music_files = [f for f in songs if f.lower().endswith(('.mp3', '.wav', '.flac', '.m4a', '.wma'))]
                    if music_files:
                        os.startfile(os.path.join(music_path, music_files[0]))
                        speak.speak("songs playing...")
                        return "songs playing..."
                    else:
                        speak.speak("No music files found in the music folder")
                        return "No music files found in the music folder"
                else:
                    speak.speak("Music folder is empty")
                    return "Music folder is empty"
            else:
                speak.speak("Music folder not found. Please check the path in Action.py")
                return "Music folder not found. Please update the music path in Action.py"
        except Exception as e:
            speak.speak("Error accessing music files")
            return f"Error accessing music files: {str(e)}"

    # Additional MITS Academy specific responses
    elif 'about mits' in data_btn or 'mits academy' in data_btn:
        response = "MITS Academy offers quality education in Computer Science, Engineering, and Business Studies with expert faculty and modern facilities"
        speak.speak(response)
        return response
    
    elif 'admission' in data_btn or 'enroll' in data_btn:
        response = "For admission inquiries, please contact our admissions office or visit our website for more details"
        speak.speak(response)
        return response
    
    elif 'courses' in data_btn:
        response = "We offer courses in Computer Science, Engineering, and Business Studies. Each program focuses on practical learning and industry skills"
        speak.speak(response)
        return response

    else:
        speak.speak("i'm unable to understand,will you please elaborate more!")
        return "i'm unable to understand,will you please elaborate more!"