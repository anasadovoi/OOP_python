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
