from langchain.vectorstores.chroma import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain, LLMChain
from langchain.schema import HumanMessage, AIMessage
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import time

def make_chain():
    model = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature="0",
        # verbose=True
    )
    template = (
        """
        This is a resume. I want you to extract the following information from the resume.
        Step 1: Extract candidate name, phone and email. Ask them if they are correct or not, if not ask them to input correct information. Or if you can't find the information in the resume, ask them to input.
        """
    )
    
    
#     (
#         """I want to act as a resume parser and headhunter to validate and ask screening question from candidate, and then suggest a job that match with candidate's expectation. 
#     At the beginning, wait for user upload their resume. Then you will extract and validate those information with user. Ask these step one by one, and wait for candidate's answer. I want you as the tone funny, and supportive.
#     Step 1: Extract candidate name, phone and email. Ask them if they are correct or not, if not ask them to input correct information. Or if you can't find the information in the resume, ask them to input.
#     Step 2: Extract candidate previous companies, roles, working date. Ask them if they are correct or not, if not ask them to input correct information. Or if you can't find the information in the resume, ask them to input.
#     Step 3: Extract candidate's college and major. Ask them if they are correct or not, if not ask them to input correct information. Or if you can't find the information in the resume, ask them to input.
#     Step 4: Extract candidate top 5 technical skills. Ask them if they are correct or not, if not ask them to input correct information. Or if you can't find the information in the resume, ask them to input.
#     Step 5: Ask them their expectation gross salary monthly in USD for better suggestion jobs purpose.
#     Step 6: Ask candidate their reason for leaving current company
#     Step 7:  Ask candidate their motivation for finding new opportunity.
#   """
#     )
    prompt = PromptTemplate.from_template(template)


    embedding = OpenAIEmbeddings()

    vector_store = Chroma(
        collection_name="april-2023-economic",
        embedding_function=embedding,
        persist_directory="src/data/chroma",
    )

    # chain = ConversationalRetrievalChain(
    #             combine_docs_chain=combine_docs_chain,
    #             retriever=vector_store.as_retriever(),
    #             question_generator=question_generator,
    #         )

    return ConversationalRetrievalChain.from_llm(
        model,
        retriever=vector_store.as_retriever(),
        condense_question_prompt= prompt,
        # return_source_documents=True,
        # verbose=True,
    )

if __name__ == "__main__":
    load_dotenv()

    chain = make_chain()
    chat_history = []

    while True:
        print()
        question = input("Question: ")

        start_time = time.time()

        # Generate answer
        response = chain({"question": question, "chat_history": chat_history})

        # Retrieve answer
        answer = response["answer"]
        # source = response["source_documents"]
        chat_history.append(HumanMessage(content=question))
        chat_history.append(AIMessage(content=answer))

        # Display answer
        # print("\n\nSources:\n")
        # for document in source:
            # print(f"Page: {document.metadata['page_number']}")
            # print(f"Text chunk: {document.page_content[:160]}...\n")
        print(f"Answer: {answer}")

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")