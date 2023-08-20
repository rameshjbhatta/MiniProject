This project has one app(taskbook) with  two models UserInfo and TaskInfo
I have used function based views in this project
Done basic CRUD(Create,Read,Update,Delete) Operations
Created signup operation
Done basic login/logout authentication
Done basic Search Operations
Used Sessions for retriving active users tasks from TaskInfo model
And it has simple frontend design using simple css and html
Steps for building API using REST FRAMEWORK
    1.Make Serializers which  allow you to convert complex data types like Django models into native    Python datatypes that can be easily rendered into JSON, XML, or other content types.
    2.DRF provides viewsets and generics for creating APIs. 
    3.So make generics and viewsets of the data you want to serialize  in views, using viewsets and generics .In general,-->> for a quick and efficient way to create endpoints, viewsets might be a better choice. On the other hand, if you need more control and customization over each operation, or if your API requirements are more complex, using generics could be more suitable.
    4.and set the path , in viewsets we register routers and include router.urls , which give all functions.
    5.In generics we can give urls as usual different path for different functions 