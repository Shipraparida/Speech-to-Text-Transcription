import speech_recognition as sr
import time

def callback(recognizer, audio):
    try:
        # Google recognizer (free, needs internet)
        text = recognizer.recognize_google(audio)
        print(" You said:", text)
    except sr.UnknownValueError:
        print(" Could not understand audio.")
    except sr.RequestError as e:
        print(f" API error: {e}")

def live_transcription():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Adjusting for background noise... Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print(" Start speaking! (Press Ctrl+C to stop)")

    # Run background listener
    stop_listening = recognizer.listen_in_background(mic, callback)

    try:
        while True:
            time.sleep(0.1)  # Keep the program alive
    except KeyboardInterrupt:
        stop_listening(wait_for_stop=False)
        print("\n Transcription stopped.")

if __name__ == "__main__":
    live_transcription()
