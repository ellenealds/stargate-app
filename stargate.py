import streamlit as st
import pandas as pd
import openai

# create a stargate themed app in streamlit
st.title('Stargate Atlantis')
st.header('Vicky, you are now part of new Stargate Atlantis episodes')
st.subheader('Select a plot from the list to see what happens in the next exciting episode of Stargate Atlantis')

# add images side by side
col1, col2, col3 = st.columns(3)
with col1:
    st.image('https://i.pinimg.com/originals/f7/e0/66/f7e0669ea5c8755aa03c7372431e3e31.jpg', width=200)
    st.write('Stargate Atlantis')

with col2:
    st.image('https://66.media.tumblr.com/9ff21578ddb83bc27312f7d24c6ad39e/tumblr_mujglyw95t1rk6qyvo1_400.gifv', width=200)
    st.write('Stargate Atlantis')

with col3:
    st.image('https://i.pinimg.com/originals/24/6c/b4/246cb48668cda0c0f07ce22aacdf950f.jpg', width=200)
    st.write('Stargate Atlantis')

#summarise text
def summarise(text_input):
    openai.api_key = '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'

    #text_input = text_input

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=text_input,
        temperature=0.3,
        max_tokens=2000,
        top_p=1,
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

text_input = f"Generate a two-paragraph episode synopsis for Stargate Atlantis including Victoria Martin and John Sheppard as the main characters\ninclude a plot twist about:{plot_twist}\ninclude a romantic scene between Victoria and John and give a cliff hanger finish\n\n\n"
#display the prompt
#st.write(text_input)

# create a button
button = st.button('Generate Episode Synopsis')
# if the button is clicked
if button:
    # run the summarise function
    summary = summarise(text_input)
    st.write(summary)
