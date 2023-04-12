#What is meant by stateless nature in RestAPI?
#Ans:-The term "stateless" in the context of RESTful APIs refers to the lack of server-side state information being stored between 
#client requests.In other words, each request from the client to the server contains all the information necessary for the 
#server to understand and process the request,without relying on any information from previous requests or sessions.

#What does 403, 503, 301 Status Codes?
#Ans:-
#403 Forbidden: This status code means that the client does not have permission to access the requested resource. 
#This may be due to authentication issues or because the client does not have the necessary permissions to access the resource.

#503 Service Unavailable: This status code means that the server is currently unavailable or unable to handle the request. 
#This may be due to server overload, maintenance, or other temporary issues. The client should try again later.

#301 Moved Permanently: This status code means that the requested resource has been permanently moved to a new URL. 
#The client should update its bookmarks or links to the new URL.
#The server typically includes the new URL in the response body or header field to help the client redirect to the new location.

#Make an Public API and use POST,get,delete,update.
import requests
#Using GET request
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

print(response.status_code)  # 200
print(response.json())

#Using POST request
data = {
    "title": "New Post Title",
    "body": "This is the body of the new post.",
    "userId": 1
}
response = requests.post(url, data=data)

print(response.status_code)  # 201
print(response.json()) 

#Using PUT request
data = {
    "title": "Updated Post Title",
    "body": "This is the updated body of the post."
}
response = requests.put(url, data=data)

print(response.status_code)  # 200
print(response.json())  # the updated post in JSON format


#Using DELETE request
response = requests.delete(url)
print(response.status_code)  # 200
print(response.json())  # empty response body