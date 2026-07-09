1. What is Pandas?
Ans: 
Pandas is an open-source Python Library used for Data Manipulation and Data Analysis. It provides powerful data structures such as Series and DataFrame, which help us read, transfor, filter, analyze, and prepare data for Mahine Leaning and AI applications.

2. Why do we use Pandas?
Ans: 
Pandas helps us to load, read, transform, analyze data and provides the structured data before building Machine learning or AI models.

3. What is the difference between a Series and a DataFrame?
Ans: 
A Series is a one-dimensional labeled data structure that contains a single column of data with an index.

A DataFrame is a two-dimensional labeled data structure consisting of rows and columns. It is similar to an Excel spreadsheet or a SQL table and is used to store, manipulate, and analyze structured data.

My Understanding(Rabbani)
Series will provide the rawdata index and values. DataFrame provide the complete data manipulation information like it has row number, column values, count, min, max, Quartiles information. Using DataFrame we can easily analyze the data by providing the predefined methods.

4. Can Machine Learning work directly with a Series?
Ans: 
Yes, a Series can be used when a model requires a single feature or a target variable. However, most Machine Learning models use a DataFrame because real-world datasets typically contain multiple features (columns).

5. What is the difference between loc[] and iloc[] in Pandas?
Ans:
iloc[] is used to access rows and columns by their integer positions, while loc[] is used to access rows and columns by their labels or names.

