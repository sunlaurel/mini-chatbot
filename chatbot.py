import streamlit as st
from langchain_openai import ChatOpenAI
import openai, os
from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.environ['API_KEY']

def generate_text(prompt):
    response = openai.completions.create(
        model='gpt-3.5-turbo-instruct',
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response.choices[0].text

def main():
    st.title("Practicing with Generating LLM Responses")
    input = st.text_area("Enter your question")

    if st.button("Generate response"):
        generated_text = generate_text(input)

        st.write(generated_text)

if __name__=="__main__":
    main()
