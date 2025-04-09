import os
import streamlit as st
from langchain import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import CTransformers  # For local LLaMA model

# Streamlit App Title
st.title('Celebrity Search (Local Model)')

# Text Input for Celebrity Name
input_text = st.text_input("Search for a celebrity:")

# Initialize Local LLaMA Model (CTransformers)
local_llm = CTransformers(
    model="D:/Mov/models/mistral-7b-v0.1.Q5_K_M.gguf",  # ✅ Update to your actual LLaMA model path
    model_type="llama",
    config={
        "temperature": 0.8,
        "max_new_tokens": 200
    }
)

# Prompt Templates
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}."
)

second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="When was {person} born?"
)

third_input_prompt = PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major events that happened around {dob} in the world."
)

# Memory Buffers for context tracking
person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='chat_history')
descr_memory = ConversationBufferMemory(input_key='dob', memory_key='description_history')

# Chains for each stage
chain1 = LLMChain(
    llm=local_llm,
    prompt=first_input_prompt,
    verbose=True,
    output_key='person',
    memory=person_memory
)

chain2 = LLMChain(
    llm=local_llm,
    prompt=second_input_prompt,
    verbose=True,
    output_key='dob',
    memory=dob_memory
)

chain3 = LLMChain(
    llm=local_llm,
    prompt=third_input_prompt,
    verbose=True,
    output_key='description',
    memory=descr_memory
)

# Combine into a Sequential Chain
parent_chain = SequentialChain(
    chains=[chain1, chain2, chain3],
    input_variables=['name'],
    output_variables=['person', 'dob', 'description'],
    verbose=True
)

# If user inputs text, run the chain
if input_text:
    response = parent_chain({'name': input_text})
    
    st.subheader("Results")
    st.json(response)  # Displays the JSON structure

    with st.expander('Person Info'):
        st.info(person_memory.buffer)

    with st.expander('DOB Info'):
        st.info(dob_memory.buffer)

    with st.expander('Major Events Around DOB'):
        st.info(descr_memory.buffer)
