Pillar Code Challenge.

Requirements:
Build a web service using Python with two endpoints:

```/vowel_count``` that receives a list of words and returns the count of vowel in each word.

Request example:
```{"words": ["batman", "robin", "coringa"]}```

Response expected:
 ```{"batman": 2, "robin": 2, "coringa": 3}```


```/sort``` that receives a list of words and an "order" and returns the list sorted.

Request example:
```{"words": ["batman", "robin", "coringa"], "order": "asc"}```

Response expected:
 ```["batman", "coringa", "robin"]```


Other requirements are create a pipeline that runs lint, test and deploy to a cloud provider.

I choose use FastApi to have auto generated documentation at ```/docs``` and a good error handling.


