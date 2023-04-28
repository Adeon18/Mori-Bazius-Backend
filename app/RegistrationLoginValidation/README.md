## Launch
```docker compose up --build```  
it launches PostgreSQL server, creates an empy table, launches PostgreSQL admin, register, validation, and login services  
login and register services may die immediately cause postgress takes time to start and they try to connect to it (idk how to fix, just relaunch them)  

## Register Service
it has 2 RestAPI endpoints: ```GET "/user/{uid}"``` and ```POST "/user"```  
uid for first one is int, and user for second one is class User  
```GET "/user/{uid}"``` returns instance of User class
```POST "/user"```  returns int which is user id

#### requests examples
```
POST localhost:8080/user
Content-Type: application/json

{
  "username": "dude",
  "password": "dude"
}
```

```
GET localhost:8080/user/1
```

## Login Service
connects to PostgreSQL server, has 1 RestAPI endpoint ```POST "/login/user/"```  
returns the token for the session of player

#### requests examples
```
POST localhost:8081/login/user
Content-Type: application/json

{
  "username": "dude",
  "password": "dude"
}
```
returns:
```
"432dfa36995306e1c47d5109d284187564e206a2"
```

## Validation Service
stores all the uids and their valid tokens in dictionary
has 2 RestAPI endpoints ```POST "/validate"``` and ```POST "/log/{uid}"```  
the second one should be ONLY used by the logging service, and the first one should ONLY be used by API Gateway  

#### Requests examples
```
POST localhost:8082/validate
Content-Type: application/json

{
  "uid": 1,
  "token": "432dfa36995306e1c47d5109d284187564e206a2"
}

```
returns ```true``` or ```false```


##### !!! IMPORTANT THIS ONE SHOULD BE USED AFTER CREDENTIALS ARE CHECKED !!!
```
POST http://validation-service:8080/log/1
```
returns
```
"432dfa36995306e1c47d5109d284187564e206a2"
```