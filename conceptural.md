### Conceptual Exercise

Answer the following questions below:

- What is RESTful routing?
    A RESTful route is a route that provides mapping from HTTP verbs such as get, post, put, delete, and patch so that you can control CRUD actions such as create, read, update, and delete. Instead of relying solely on the URL to indicate what site to visit, a RESTful route depends on the HTTP verb and the URL. 

- What is a resource?
    A resource is an object sent by the server that correspoinds to a specific format to the client.

- When building a JSON API why do you not include routes to render a form that when submitted creates a new user?
    The reason why you do not include routes to render a form is because the information would be resubmitted when the client refreshes the page on a form.  

- What does idempotent mean? Which HTTP verbs are idempotent?
    Idempotent is a property of some operation such that no matter how many times you execute them, you achieve the same results. Every HTTP verb is idempotent except for POST. So idempotent HTTP verbs are: get, put, patch, delete are some examples.


- What is the difference between PUT and PATCH?
    Put sends and updates the complete entity while PATCH focues only on the fields that were supplied and affects those alone.

- What is one way encryption?
    Encryption that is hard to reserve is called one way encryption. 

- What is the purpose of a `salt` when hashing a password?
    Salt is very important for hashing a password. `salt` is the random data used for input of a function that hashes data or passwords. It's very useful. 


- What is the purpose of the Bcrypt module?
    Bcrypt module is used for hashing data like passwords in Python on the server to ensure passwords in SECRET KEYS. 


- What is the difference between authorization and authentication?
    Authentication is identifying who the user is while authorization is establishing which rights and privilages a user has been granted. 