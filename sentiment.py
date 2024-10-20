# %% [markdown]
# # Imports

# %%
import os
import nltk
import streamlit as st

from nltk.sentiment.vader import SentimentIntensityAnalyzer

os.system('pip install --upgrade pip')

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

score = s.polarity_scores( user_input )

if score == 0:
    st.write( '### Neutral' )

elif score[ 'neg' ] != 0:
    st.write( '### Negative' )

elif score[ 'pos' ] != 0:
    st.write( '### Positive' )



