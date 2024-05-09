import streamlit as st
from streamlit_extras.let_it_rain import rain
import random

# Set page title and layout
st.set_page_config(page_title="Mother's Day Card", layout="centered")

def rose():
    rain(
        emoji="🌹",
        font_size=54,
        falling_speed=5,
        animation_length="infinite"
    )
def flower():
    rain(
        emoji="🌸",
        font_size=54,
        falling_speed=5,
        animation_length="infinite"
    )   

def sunflower():
    rain(
        emoji="🌼",
        font_size=54,
        falling_speed=5,
        animation_length="infinite"
    )    

# Random messages for Mother's Day
messages = [
    "Happy Mother's Day, Mommy!",
    "Wishing you a day filled with love and joy, Mommy!",
    "To the best mom ever, Happy Mother's Day!",
    "Thank you for always being there, Happy Mother's Day!",
    "Happy Mother's Day to the most amazing mommy!",
    "Sending you all my love on Mother's Day, Mommy!",
    "You are the heart of our family, Mommy. Happy Mother's Day!",
    "Your love is the fuel that keeps our family running. Happy Mother's Day, Mommy!",
    "Every day with you is a blessing. Happy Mother's Day, Mommy!",
    "Thank you for being my rock, my confidant, and my biggest supporter. Happy Mother's Day, Mommy!",
    "Your strength and resilience inspire me every day. Happy Mother's Day, Mommy!",
    "You are my guiding light, Mommy. Happy Mother's Day!",
    "No words can express how grateful I am to have you as my Mommy. Happy Mother's Day!",
    "You make the world a better place just by being you. Happy Mother's Day, Mommy!",
    "Your love knows no bounds, Mommy. Happy Mother's Day!",
    "You are more than a mother; you are my best friend. Happy Mother's Day, Mommy!",
    "You are the epitome of grace and kindness, Mommy. Happy Mother's Day!",
    "Your love is the greatest gift I've ever received. Happy Mother's Day, Mommy!",
    "You deserve all the love and happiness in the world. Happy Mother's Day, Mommy!",
    "You are the heart and soul of our family. Happy Mother's Day, Mommy!"
]

# Select a random message
random_message = random.choice(messages)

# Create a container to hold the card
card = st.container()

# Apply styles to the card
card.markdown(
    """
    <style>
        .card {
            border: 2px solid black;
            padding: 20px;
            border-radius: 15px;
            background-color: #FF6347; /* Red color */
            color: white;
            font-family: 'Arial';
            box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
            text-align: center;
            margin: 50px auto;
            width: 80%;
            max-width: 600px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the card with a random message
with card:
    st.markdown(f"""
    <div class='card'>
        <h2>🌷 Happy Mother's Day! 🌷</h2>
        <p>{random_message}</p>
    </div>
    """, unsafe_allow_html=True)
col = st.columns(5)
with col[1]:
    bf1= st.button("🌹", key="rose")
with col[2]:
    bf2 = st.button("🌸", key="flower")
with col[3]:
    bf3 = st.button("🌼", key="sunflower")

if bf1==True:
    rose()
if bf2 == True:
    flower()
if bf3 == True:
    sunflower()
# Let flowers rain
