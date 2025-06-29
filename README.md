# picky-points
A short competition held for IITB Freshers '25

## The Game
There is an array of points in 3D space. Your and your opponent's bots take turns choosing a sphere of unit radius and an arbitrary center, with the goal of capturing as many points from the array as possible. A point is considered captured if it is inside the chosen sphere (_~~due to a mistake, points on the boundary are not considered~~. This has been fixed_). In each turn, the captured points are removed from the array.

## The Ranking
Bots with similar runtimes are clubbed to form a group, the exact details of how the groups will be made has not yet been decided since it would depend on the number of submissions recieved.

The bots within a group will play a round-robin tournament, and in the end will be ranked based on the total number of points captured.

## The Submissions
You have to edit and send the ```player_base.py``` file to the host, Snehil Jha (on WhatsApp). 

Multiple submissions per person is allowed, to encourage people to explore a variety of approches. Only the best bot of each person per runtime group will be considered for the final ranking.

Team formation is also allowed.

The deadline for submission is 6 o'clock in the morning of 5th July.

## The Participation
Download this repo as a zip file by clicking on ```Code > Download ZIP``` and extract it.

![Screenshot of the repo page showing where to download the code from](https://github.com/user-attachments/assets/f80e2231-60e1-41c7-97d6-5a3d213e4a9f)

The two most important files for participants are ```player_base.py``` and ```match.py```.

Within the ```player_base.py``` file is the ```Player.think()``` function. It recieves an array of points which have not yet been captured, and you need to write an algorithm to determine an appropriate center for the sphere you wish to choose.

Don't forget to give a name to each of your bots, be as creative as you wish

![Screenshot of player_base.py, showing the general structure](https://github.com/user-attachments/assets/fcb2ac7c-8f0c-43fd-a0f2-5fc8c34673a8)

The ```match.py``` file is what you would be running to test your bots. Choose any two bots you want to test, and run the program. You may also change the settings for that specific match

![Screenshot of match.py, showing the editable options](https://github.com/user-attachments/assets/69868efe-aa3a-48a4-9688-684fdb08f3bf)


Just as examples, I have attached two very simple bots. One just picks a point at random, and the other picks the mean of all the points.

___Good Luck!___
