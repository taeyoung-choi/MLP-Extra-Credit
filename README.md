# MLP-Extra-Credit

A containerized tornado REST API that accepts a query for a GET request like ?user=username and returns "Hello, username" as the response.

``` bash
    >> docker build -t mlp_extra .
    >> sudo docker run -p 7777:7777 mlp_extra
```
Opening [http://localhost:7777/?user=John Doe](http://localhost:7777/?user=John%20Doe) in your web browser will print out Hello, John Doe.

