JSONStream
==========

JSONStream is python library that enables parsing distinct JSON objects from an input stream
 


Example Usage
=============
    ```python
    from StringIO import StringIO
     import JSONStream import JSONStream

     cities = StringIO('''
        {"name": "London"}
        {"name": "Milan"}
        {"name": "New york"}
        {"name": "Paris"}
    ''')

     for city in JSONStream(cities):
        print(city.name)
    ```

    If the above data is stored in a file.

    ```python
     import JSONStream import JSONStream

     with open('cities.json') as cities:
         for city in JSONStream(cities):
            print(city.name)
    ```


    
