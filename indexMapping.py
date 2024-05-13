#Satya Shah
#Assigment-2
#UTA ID-1002161494

indexMapping = {
    "properties": {
        "Series_Title": {
            "type": "text"
        },
        "Director":{
            "type":"text"
        },
        "Genre":{
            "type":"text"
        },

        "Overview": {
            "type": "text"
        },
        "OverviewVector": {
            "type": "dense_vector",
            "dims": 768,
            "index": True,
            "similarity": "l2_norm"
        }
    }
}
