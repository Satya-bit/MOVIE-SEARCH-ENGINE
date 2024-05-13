# MOVIE-SEARCH-ENGINE
A web page that can used to search movies based on description , director and movie name. IMDB Top 1000 movies is used as a dataset.

# Technologies, libraries and platforms used:-

-Huggingface ![image](https://github.com/Satya-bit/MOVIE-SEARCH-ENGINE/assets/70309925/b9f38852-8d35-4cbb-83ae-5695784807b7)

-Python ![image](https://github.com/Satya-bit/MOVIE-SEARCH-ENGINE/assets/70309925/6bf45869-aaca-454b-8129-0f862fbf7bff)

-Kaggle ![image](https://github.com/Satya-bit/MOVIE-SEARCH-ENGINE/assets/70309925/829f74f2-e51d-47e0-b829-c71e03249e86)


-Sentence Transformer(‘all-mpnet-base-v2’) ![image](https://github.com/Satya-bit/MOVIE-SEARCH-ENGINE/assets/70309925/b9968188-9ddd-4af9-af69-7f86a04216cb)

-Pandas ![image](https://github.com/Satya-bit/MOVIE-SEARCH-ENGINE/assets/70309925/b3d36b3a-0d5b-4e4d-a75d-5500b6d0a983)

-Elastic search ![image](https://github.com/Satya-bit/MOVIE-SEARCH-ENGINE/assets/70309925/b1fffd70-898b-461e-b523-f6c1755608fd)

-Base64 ![image](https://github.com/Satya-bit/MOVIE-SEARCH-ENGINE/assets/70309925/6befbcce-a978-4430-921e-c660085f7f9c)

-Streamlit ![image](https://github.com/Satya-bit/MOVIE-SEARCH-ENGINE/assets/70309925/9b25da5c-111f-4ba9-8d1a-094e0245db27)



# HOW THE CODE WORKS
-> Connect the elastic search server by writing ‘elasticsearch’ in the command prompt.
-> Connect to the elastoic search database using your credentials. After fetching the dataset from Kaggle I used the ‘all-mpnet-base-v2’ model from huggingface to get embeddings of our sentences.
->I made an index on the overview column and stored the word embeddings in indexnode=’satyashah’.
->We will call this index on the front end to fetch the data after writing a query. I have used l2_norm to get the similarity between the query and overview.
->By using the command python-m streamlit run app.py to connect the localhost.

# ON LOCALHOST
![image](https://github.com/Satya-bit/MOVIE-SEARCH-ENGINE/assets/70309925/0616d744-20b4-4c98-82a6-6463bf0dadb7)
When I wrote women in sports it showed relevant movies like Chak De India, Dangal along with movie's description, Director and overview.

![image](https://github.com/Satya-bit/MOVIE-SEARCH-ENGINE/assets/70309925/fde31318-6d8c-47bd-be21-0ece1a5cb058)
We can also search movies by writing the name of director. For instance I wrote 'Nolan' then it showed movies like 'Bataman Begins' and 'The Dark Night'
