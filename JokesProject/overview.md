#The Project Joke/ Voting Meme
# Inheriance

Model  < ------------ abstract
  |
  +--id     __init__()  # delegation initialization
               ^------------------------------------+
---------------|-------------------                 |
  ^            |             ^                      |
  |            |             |                      |
 Meme          __init__()   User                 __init__()              
  |                 ^     |                         ^
  + -- title        |     + -- name                 |
  + -- image        |     + -- avatar               |
  + -- author       |     + -- email                |
  + -- published    |     + -- password             |
  + -- rating       |                               |
                    |                               |
                    |                               |
                Meme('Sport meme', user_1, 4.0)     User("johny", "j@yahoo.com", 'password1')




One user posts 2 memes

 +----- user 1
 |       |
 |      +--id '1'
 |      +--name 'John'
 |     +--memes[

                0 ----+
                1 ----|---+
            ]         |    |
 |                    |    |
 |       post 1  <----self |
 |      |                  |
 |      +--id '1'          |
 |      +--title 'Sport m' |
 |----- +-- author: user2  |
 |                         |
 |      post 2  <--------self
 |      |
 |      +--id '2'
 |       +--title 'Sport meme'
 | ----- +--author: user1


# python /advanced / design patterns

# singletone

Storage
   \
+---+-------------------+
|                       |
|     __init__()        |
|       save(user)      |
|                       |
+-----------------------+
          ^
          |
      instance of Storage class
          |
        fileStorage = Storage()

################################

Storage object lifecycle 

          __init__(...)                    __del__(...)
          (  ....  )
              +-------------------------------+
              ^                               |
              |                               v      
x-------------x-------------------------------x---->
        fileStorage = Storage()               del fileStorage
                                              fileStorage = None
                                              program end

                                              
Memory leak


# Proxy Pattern
                   |
[consumer] <------ |<proxy> --------> [provider]
                   |


lazy initialization (ex: chat app)
  traffic economy
  cache 
access control (protection proxy)
logging request (logging proxy)


Python

 User (object)
        \
 +----------------+
 |                |
 |                |
 |                |
 |   to JSON()    +----json string -----> Storge -------- save ---------> json, yaml, csv
 |                |
 |                |
 |                |
 +----------------+


'{"name":"John Doe"}'