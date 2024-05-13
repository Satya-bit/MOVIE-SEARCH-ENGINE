#Satya Shah
#Assigment-2
#UTA ID-1002161494


import streamlit as st
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import base64

# Encoding the username and password and connecting to server
username = "satya2610"
password = "satya2610"
credentials = f"{username}:{password}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()
indexName = "satyashah"#fetching the index which was created in database

try:
    es = Elasticsearch(
        "http://localhost:9200",
        headers={"Authorization": f"Basic {encoded_credentials}"},
        request_timeout=300
    )

except ConnectionError as e:
    print("Connection Error:", e)


def search(user_input):
    model = SentenceTransformer('all-mpnet-base-v2')#using sentence transformer
    user_input_vector = model.encode(user_input)

    query = {
        "field": "OverviewVector",
        "query_vector": user_input_vector,
        "k": 5,
        "num_candidates": 1000
    }
    res = es.knn_search(index="satyashah",
                        knn=query,
                        source=["Series_Title","Director","Genre","Overview"])
    results = res["hits"]["hits"]

    return results


def main():
    st.title("Search Movies")

    # Applying custom CSS to set the background color
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            background-image : url("https://as2.ftcdn.net/v2/jpg/02/86/32/31/1000_F_286323187_mDk3N4nGDaPkUmhNcdBe3RjSOfKqx4nZ.jpg");
            background-size : cover;
            color:#000000;
            padding: 50px 50px 50px 500px;
        }
       
        
        </style>
        """,
        unsafe_allow_html=True
    )

    # Setting the label text color to black
    st.markdown("<h4 style='color: #333333;'>Enter the movie description</h3>", unsafe_allow_html=True)

    # Input: User enters search query
    search_query = st.text_input("", "")

    # Button: User triggers the search
    if st.button("Search"):
        if search_query:
            # Performing the search and get results
            results = search(search_query)

            # Displaying search results
            st.subheader("Search Results")
            for result in results:
                with st.container():
                    if '_source' in result:
                        try:
                            st.header(f"{result['_source']['Series_Title']}")
                        except Exception as e:
                            print(e)
                        try:
                            st.write(f"Director: {result['_source']['Director']}")
                        except Exception as e:
                            print(e)
                        try:
                            st.write(f"Genre: {result['_source']['Genre']}")
                        except Exception as e:
                            print(e)

                        try:
                            st.write(f"Overview: {result['_source']['Overview']}")
                        except Exception as e:
                            print(e)
                        st.divider()


if __name__ == "__main__":
    main()
