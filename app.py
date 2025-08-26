import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from pymupdf import fitz  # PyMuPDF for better text extraction
import pytesseract
from PIL import Image
import io




load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_pdf_text(pdf_docs):
    text = ""
    
    for pdf in pdf_docs:
        try:
            # Try PyMuPDF first (better text extraction)
            pdf_document = fitz.open(stream=pdf.read(), filetype="pdf")
            
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)
                
                # Try to extract text
                page_text = page.get_text()
                
                # If no text found, try OCR
                if not page_text.strip():
                    # Get page as image
                    pix = page.get_pixmap()
                    img_data = pix.tobytes("png")
                    img = Image.open(io.BytesIO(img_data))
                    
                    # Use OCR to extract text
                    try:
                        page_text = pytesseract.image_to_string(img)
                        st.info(f"Used OCR for page {page_num + 1} of {pdf.name}")
                    except Exception as ocr_error:
                        st.warning(f"OCR failed for page {page_num + 1}: {str(ocr_error)}")
                        continue
                
                text += page_text + "\n"
            
            pdf_document.close()
            
        except Exception as e:
            st.error(f"Error processing {pdf.name}: {str(e)}")
            # Fallback to PyPDF2
            try:
                pdf.seek(0)  # Reset file pointer
                pdf_reader = PdfReader(pdf)
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
            except Exception as fallback_error:
                st.error(f"Fallback extraction also failed for {pdf.name}: {str(fallback_error)}")
    
    if not text.strip():
        st.warning("No text was extracted from the PDF files. Please check if the files contain readable text.")
    else:
        st.success(f"Successfully extracted {len(text)} characters of text")
    
    return text



def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    if not text_chunks:
        st.error("No text chunks to process. Please check if your PDF files contain text.")
        return
    
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
        vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
        vector_store.save_local("faiss_index")
        st.success("Vector store created successfully!")
    except Exception as e:
        st.error(f"Error creating vector store: {str(e)}")
        st.info("This might be due to API rate limits or empty text content.")


def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",
                             temperature=0.3)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain



def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    print(response)
    st.write("Reply: ", response["output_text"])




def main():
    st.set_page_config("Chat PDF")
    st.header("Chat with PDF using Gemini💁")

    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                if raw_text.strip():
                    text_chunks = get_text_chunks(raw_text)
                    st.info(f"Created {len(text_chunks)} text chunks")
                    get_vector_store(text_chunks)
                else:
                    st.error("No text could be extracted from the uploaded PDF files.")



if __name__ == "__main__":
    main()