print("""inkle twinkle little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle twinkle little star
How I wonder what you are
Twinkle twinkle little star
Shining brightly and afar
Twinkle star dust all around
From the sky right to the ground
Twinkle twinkle little star
Shining brightly and afar""")


import pyttsx3
engine = pyttsx3.init()
engine.say("I Love You")
engine.runAndWait()

import os
directory_path = '/'

contents = os.listdir(directory_path)

print(contents)