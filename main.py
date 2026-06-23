import json
import streamlit as st

st.set_page_config(
    page_title="German Dictionary",
    page_icon="🇩🇪",
    layout="centered"
)

@st.cache_data
def load_translations():
    with open("cleaned_german_words.json",encoding="utf-8")as f:
        data = json.load(f)

    return {
        item["word"].lower(): item
        for item in data
    }

translations = load_translations()

st.markdown("""
<div style="
height:18px;
background: linear-gradient(
90deg,
black 33%,
red 33%,
red 66%,
gold 66%
);
border-radius:10px;
margin-bottom:20px;
"></div>
""", unsafe_allow_html=True)


st.markdown("""
<h1 style='text-align: center;'>
🇩🇪 German Dictionary
</h1>
<p style='text-align: center; color: gray;'>
Search German words instantly
</p>
""", unsafe_allow_html=True)

word = st.text_input(
    "🔍 Enter a German word",
    placeholder="e.g. Haus, Hund, Meer"
)

if word:
    entry = translations.get(word.lower())

    if entry:
        st.markdown(
            f"""
            <div style="
                border-radius:15px;
                padding:20px;
                margin-top:20px;
                background-color:#1E293B;
                color:white;
                border:1px solid #ddd;
             ">
                <h2>{word.capitalize()}</h2>
                <h3>➡️ {entry['english_translation']}</h3>
                <h3>{entry['pos']}</h3>
                <h3>🇩🇪 : {entry['example_sentence_native']}</h3>
                <h3>🇬🇧 : {entry['example_sentence_english']}</h3>
                
             </div>
             """,
              unsafe_allow_html=True
         )
    else:
        # st.markdown(
        #     f"""
        #     <div style="
        #         border-radius:15px;
        #         padding:20px;
        #         margin-top:20px;
        #         background-color:#1E293B;
        #         color:white;
        #         border:1px solid #ddd;
        #      ">
        #         <h2> Oh oh! Word not Found 😭 </h2>
        #      </div>
        #     """,
        #     unsafe_allow_html=True
        # )
        col1,col2,col3 = st.columns([1,2,1])

        with col2:
            st.image("not-found.png")
            st.error("Ich kenne dieses Wort nicht!")

