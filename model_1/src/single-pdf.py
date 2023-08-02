from langchain.vectorstores.chroma import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.schema import HumanMessage, AIMessage
from dotenv import load_dotenv
import time

def make_chain():
    model = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature="0",
        # verbose=True
    )
    embedding = OpenAIEmbeddings()

    vector_store = Chroma(
        collection_name="april-2023-economic",
        embedding_function=embedding,
        persist_directory="src/data/chroma",
    )

    return ConversationalRetrievalChain.from_llm(
        model,
        retriever=vector_store.as_retriever(),
        return_source_documents=True,
        # verbose=True,
    )

if __name__ == "__main__":
    load_dotenv()

    chain = make_chain()
    chat_history = []

    query = """
    I want to act as a resume parser. I want to do step by step below, each step will be a question and answer.
    Step 1: Extract candidate name, phone and email. Ask user to verify it. Then ask step 2.
    Step 2: Extract candidate previous company, title, working dates. Ask user to verify it. Then ask step 3.
    """
    response = chain({"question": query, "chat_history": chat_history})
    answer = response["answer"]
    chat_history.append(HumanMessage(content=query))
    chat_history.append(AIMessage(content=response["answer"]))
    print(f"Answer: {answer}")


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
        #     print(f"Page: {document.metadata['page_number']}")
        #     print(f"Text chunk: {document.page_content[:160]}...\n")
        print(f"Answer: {answer}")

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")