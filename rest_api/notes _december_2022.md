# About API to read the barcode
##  REST API
* Also known as RESTful API 
* application programming interface that conforms contraint REST architectural style and allows for interaction with RESTfull web services
* REST stands for Representational State Transfer 
* Created by computer scientist Roy Fielding

## API
It stands for Application Programming Interface, it is a software intermediary that enables communication betwenn several applications. For example, you can use a mobile app to connect to the internet and sending data to a server. There data is processed and send again to your mobile. The app interprets the upload data and presents it in a readable way. 
In short, an API take arequest from an application and sends it to a server. The server then process the request and sends the data back to the applications. The application, interprets the data and presents it to the user.

FALTA UN DIBUJITO AQUI

Some API's characteristics are:
* Set of definitions and protocols for building and integrating application software.
* They make modular and decoupled applications; applications can be built quickly and easily allowing easier maintainance and update.
* sometimes refered to as a contact between an information provider and an information usrer (the call- contact- the response).
* helps to communicate what a user want to the comuter or system, so it can understand and fulfill the user's request .
* A way for an organization to share resources and information while maintaining security, control, and autenthication determining who get access to what.
* The user does not have to know the specifics of caching.
* They allow different applications to share data and work together, saving time and effort 

## REST 
* Is a set of architectural constraints, not a protocol or a standard. 
* Can be implemented in a variety of ways.
* It transfers a representation of the state of the resource to the requester or endpoint
* Delivers information in one of several formats via HTTP:
  
        1. JSON (Javascript Object Notation) -most common.
        2. HTML
        3. XLT
        4. Python
        5. PHP
        6. plain text
* Headers and parmeters are imortant in the HTTP methods of a REST API request. They contain important identifier information as to the request's metadata, authorization, uniform resource identifier (URI), caching, cookiesm, and more. There are request and response headers, each with their own HTTP connection information and status codes. 
  
# REST API
An REST API has:
* A client-server architecture made up of clients, servers, and resources, with requests manage trhough HTTP
* Stateless client-server communication, meaning  no client information is stored between get requests and each request is separate and unconnected.
* Cacheable data that streamlines client-server interactions.
* A uniform interface between components so that information is transferred in a standard form. This requires that:
        1. Resources requested are identifiable and separate from the representation sent to the client.
        2. resources can be manipulated by the client via the representation they recieve because the representation contains enough information to do so.
        3. Self-decriptive messages returned to the client have enough information to descrive how the client should process it.
        4. hypertext/hypermedia is available, meaning that the after accesing a resource the client should be able to use hyperlinks to find all other currently available actions they can take.
* A layered system that organizes each type of server (those responsible for security, load-balancing, etc.) involved the retrieval of requested information into hierarchies, invisible to the client.
* Code-on-demand (optional): the ability to send executable code from the server tothe client when requeted etending client functionality.
  
RSET API are cosidered easier to use than a prescribed protocol like SOAP - which has specific requirements.-

REST is a set of guidelines that can be implemented as needed, making REST APIs faster and more lightweight, with increased scalability - perfect for  IoT and movile app development.

####################################################

##  Creating an API
There are many frameworks to build an API in Python such as: 
* Django
* Flask
* FastAPI
### What is FastAPI
It is a web framework to create APIs quickly and efficiently with Python 3.7+ based on standard Python. FastAPI is build on top of Starlette web server and includes features that make building web application easier -authomatic data validation, error handling and interactive API docs.

### Using fastAPI
1. Install fastapi and uvicorn

## RESOURCES
https://www.redhat.com/en/topics/api/what-is-a-rest-api
https://www.datacamp.com/tutorial/introduction-fastapi-tutorial

