import streamlit as st
import pandas as pd
import openai
import os

# create a stargate themed app in streamlit
st.title('Stargate Atlantis')
st.header('Vicky, you are now part of new Stargate Atlantis episodes')
st.subheader('Select a plot from the list to see what happens in the next exciting episode of Stargate Atlantis')

# add images side by side
col1, col2, col3 = st.columns(3)
with col1:
    st.image('https://ic.pics.livejournal.com/neevebrody/11550022/524545/524545_original.gif', width=200)
    #st.write('Stargate Atlantis')

with col2:
    st.image('https://ic.pics.livejournal.com/neevebrody/11550022/362682/original.gif', width=200)
    #st.write('Stargate Atlantis')

with col3:
    st.image('https://ic.pics.livejournal.com/neevebrody/11550022/591621/591621_original.gif', width=200)
    #st.write('Stargate Atlantis')

#summarise text
def summarise(text_input):
    openai.api_key = os.getenv("OPENAI_API_KEY") 
    
    #text_input = text_input

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=text_input,
        temperature=0.7,
        max_tokens=2000,
        top_p=5,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['text']
main = "Victoria Martin"

# create a multi select box
#st.subheader('Select characters')
#character = st.multiselect('Characters', ['Major John Sheppard','Dr. Elizabeth Weir', 'Ronon Dex', 'Colonel Steven Caldwell', 'Lt. Laura Cadman', 'Kavanagh', 'Lt. Colonel John Edwards', 'Woolsey', 'Lorne', 'Weir (Replicator)', 'Todd', 'Michael Kenmore', ' Hermiod', 'Dr. Rodney McKay', 'Teyla Emmagan', 'Lt. Aiden Ford', 'Dr. Carson Beckett', 'Sgt. Major Ronald Greer', 'Lt. Colonel Samantha Carter', 'Dr. Jennifer Keller'])
# concatenate the selected options into a comma separated string
#character = ', '.join(character)

plot_twist = st.multiselect('Plot Twists', ['The team discovers a Stargate on a planet that is about to be destroyed by a supernova.', 'The team discovers a planet that is inhabited by humans.', 'The team discovers a planet that is inhabited by aliens.', 'The team discovers a planet that is inhabited by both humans and aliens.', 'The team discovers a planet that is inhabited by Goauld.', 'The team discovers a planet that is inhabited by Wraith.', 'The team discovers a planet that is inhabited by Ancients.', 'The team discovers a planet that is uninhabitable.', 'The team is attacked by a Goauld ship.', 'The team is attacked by a Wraith ship.', 'The team is attacked by an Ancient ship.', 'The team is stranded on a planet with no Stargate.', ' The team is attacked by a human ship.', 'The team discovers a Goauld ship.', 'The team discovers a Zpm.', 'The team discovers an Ancient ship.', 'The team discovers a Wraith ship.', 'The team discovers a planet with a Stargate that is about to be destroyed by a supernova.', 'The team is stranded on a planet with no food or water.', 'The team is stranded on a planet with no way to contact Earth.'])
plot_twist = ', '.join(plot_twist)

#text_inputinlc = st.text_input('Enter additonal information about your story, for example: include a romantic scene.')

text_input = f"Generate a two-paragraph episode synopsis for Stargate Atlantis including Victoria Martin and John Sheppard as the main characters\ninclude a plot twist about:{plot_twist}\nJohn falls in love with Victoria.\n\n\n"
#display the prompt
#st.write(text_input)

# create a button
button = st.button('Generate Episode Synopsis')
# if the button is clicked
if button:
    # run the summarise function
    summary = summarise(text_input)
    st.write(summary)
