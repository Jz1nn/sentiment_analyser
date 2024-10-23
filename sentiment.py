# %% [markdown]
# # Imports

# %%
import nltk
import streamlit as st

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# %% [markdown]
# # Creation of the system

# %%
# System Title

st.write( '# Customer Satisfaction Analysis' )

user_input = st.text_input( 'Please rate our service:' )

# %% [markdown]
# # Creation of the predictive customer satisfaction machine

# %%
nltk.download( 'vader_lexicon' )

s = SentimentIntensityAnalyzer()

if user_input:
    # Get the sentiment scores
    score = s.polarity_scores( user_input )

    # Analyze the compound score for overall sentiment
    if score['compound'] >= 0.05:
        st.write( '### Positive' )
    elif score['compound'] <= -0.05:
        st.write( '### Negative' )
    else:
        st.write( '### Neutral' )


