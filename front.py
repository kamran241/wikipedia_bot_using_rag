import streamlit as st

# Set the title of the app
st.title("Wikipedia Search")

# Function to load data from Wikipedia
def load_from_wikipedia(query, lang='en', load_max_docs=2):
    from langchain.document_loaders import WikipediaLoader
    loader = WikipediaLoader(query=query, lang=lang, load_max_docs=load_max_docs)
    data = loader.load()
    return data

# Sidebar for settings
st.sidebar.markdown("## Settings")
language = st.sidebar.selectbox("Select Language", ["en", "es", "fr", "de", "it","ar","hi","ur","fa","tr","pt","nl","ja","zh","ko","it","pl","ro","sv","no","da","fi","he","th","vi","ms","id","hi","ur","fa","tr","pt","nl","ja","zh","ko","it","pl","ro","sv","no","da","fi","he","th","vi","ms","id"])
max_docs = st.sidebar.slider("Max Documents to Load", 1, 10, 2)

# Input field for the topic
text = st.text_input("Enter a topic")

# Button to trigger the search
if st.button("Search"):
    if text:
        with st.spinner("Loading data from Wikipedia..."):
            data = load_from_wikipedia(text, lang=language, load_max_docs=max_docs)
            st.success("Data loaded successfully!")
            for doc in data:
                st.subheader(doc.metadata['title'])
                st.write(doc.page_content)
    else:
        st.warning("Please enter a topic to search.")

# Footer
st.markdown("---")
st.markdown("© 2025 Wikipedia Search App. All rights reserved.")
