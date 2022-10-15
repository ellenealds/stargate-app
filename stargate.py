import streamlit as st
import pandas as pd
import openai

# create a stargate themed app in streamlit
st.title('Stargate Atlantis')
st.header('Vicky, you are now part of new Stargate Atlantis episodes')
st.subheader('Select the character you want to be in the story and a plot twist, add some additonal text and see what happens in the next exciting episode of Stargate Atlantis')

#add an image from a url
st.image('https://wallup.net/wp-content/uploads/2019/09/06/347567-stargate-atlantis-adventure-television-series-action-drama-sci-fi-62.jpg')

#summarise text
def summarise(text_input):
    openai.api_key = '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'

    #text_input = text_input

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=text_input,
        temperature=0.7,
        max_tokens=1500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['text']
main = "Victoria Martin"

# create a multi select box
st.subheader('Select characters')
character = st.multiselect('Characters', ['Dr. Elizabeth Weir', 'Ronon Dex', 'Colonel Steven Caldwell', 'Lt. Laura Cadman', 'Kavanagh', 'Lt. Colonel John Edwards', 'Woolsey', 'Lorne', 'Weir (Replicator)', 'Todd', 'Michael Kenmore', 'Major John Sheppard', ' Hermiod', 'Dr. Rodney McKay', 'Teyla Emmagan', 'Lt. Aiden Ford', 'Dr. Carson Beckett', 'Sgt. Major Ronald Greer', 'Lt. Colonel Samantha Carter', 'Dr. Jennifer Keller'])
# concatenate the selected options into a comma separated string
character = ', '.join(character)

plot_twist = st.multiselect('Plot Twists', ['The team discovers a Stargate on a planet that is about to be destroyed by a supernova.', 'The team discovers a planet that is inhabited by humans.', 'The team discovers a planet that is inhabited by aliens.', 'The team discovers a planet that is inhabited by both humans and aliens.', 'The team discovers a planet that is inhabited by Goauld.', 'The team discovers a planet that is inhabited by Wraith.', 'The team discovers a planet that is inhabited by Ancients.', 'The team discovers a planet that is uninhabitable.', 'The team is attacked by a Goauld ship.', 'The team is attacked by a Wraith ship.', 'The team is attacked by an Ancient ship.', 'The team is stranded on a planet with no Stargate.', ' The team is attacked by a human ship.', 'The team discovers a Goauld ship.', 'The team discovers a Zpm.', 'The team discovers an Ancient ship.', 'The team discovers a Wraith ship.', 'The team discovers a planet with a Stargate that is about to be destroyed by a supernova.', 'The team is stranded on a planet with no food or water.', 'The team is stranded on a planet with no way to contact Earth.'])
plot_twist = ', '.join(plot_twist)

addtext_input = st.text_input('Enter additonal information about your story, for example: include a romantic scene.')

text_input = f"Topic: Stargate Atlantis\nGenerate a five paragraph story, this must engaging and exciting and must include the main character: \n\nmain character:{main}\nadditional characters:{character}\nplot twist:{plot_twist}\ntheme: {addtext_input}"
#display the prompt
#st.write(text_input)

# create a button
button = st.button('Generate Episode Synopsis')
# if the button is clicked
if button:
    # run the summarise function
    summary = summarise(text_input)
    summary1 = summarise(summary)
    summary2 = summarise(summary1)
    st.write(summary, summary1, summary2)
