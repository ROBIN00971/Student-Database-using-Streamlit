import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain.llms import HuggingFaceHub

def getPdfText(pdfDocs):
    texts=""
    for pdf in pdfDocs:
        pdfReader=PdfReader(pdf)
        for page in pdfReader.pages:
            texts+=page.extract_text()
    return texts

def getChunkText(rawText):
    textSplit=CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = textSplit.split_text(rawText)
    return chunks

def getVectorStorage(chunkText):
    #embed=OpenAIEmbeddings()
    embed=HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore=FAISS.from_texts(texts=chunkText,embedding=embed)
    return vectorstore

def getConversation(vectorStorage,pdfDocs):
    #llm=ChatOpenAI()
    llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})
    memory=ConversationBufferMemory(memory_key="chat_history",return_messages=True)
    conversationChain=ConversationalRetrievalChain(
        llm=llm,
        retriever=vectorStorage.as_retriever(),
        memory=memory,
        combine_docs_chain=pdfDocs,
        question_generator=llm,
        
    )
    return conversationChain
    
def handleQues(userQuestion):
    response = st.session_state.conversation({'question':userQuestion})
    st.session_state.chat_history=response['chat_history']
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with Pdfs", page_icon=":books:")
    st.write(css,unsafe_allow_html=True)
    if "conversation" not in st.session_state:
        st.session_state.conversation=None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.header("ChatpDf:books:")
    userQuestion=st.text_input("Ask a Question")
    if userQuestion:
        handleQues(userQuestion)
    st.write(bot_template.replace(
                "{{MSG}}", "Hello how can i help you?"), unsafe_allow_html=True)

    with st.sidebar:
        st.subheader("Your Documents")
        pdfDocs=st.file_uploader("Upload Your Pdfs and Click Process",accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                rawText=getPdfText(pdfDocs)
                chunkText=getChunkText(rawText)
                vectorStorage=getVectorStorage(chunkText)
                st.session_state.conversation=getConversation(vectorStorage,pdfDocs)
    #st.session_state.conversation()
if __name__ == '__main__':
        main()