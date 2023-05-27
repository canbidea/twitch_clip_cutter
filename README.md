# twitch_clip_maker

This is my first project so it's a bit scuffed. Main purpose of this program is detecting the moments in a long stream when chat messages exceeds the average message in the total vod adn creating clips of these minutes. There must be a text file named suggested chat.log and also it requires the vod as the name suggested Video.mp4. These files can be obtain through TwitchDownloaderGUI

First open "chat_analysis", in this code it is possible to select which power do you want such as finding the minutes where chat wrote messages x1.5 or x2 times compared to the average. Then you will get the minute list.

Next, open "video_cutter" and write these minutes as input. You have the option to select the length of the clips. Also I thought that there is a little lag behind chat depending on the stream so it would be better idea to start the clip one minute before. For example: In the minute 5 there are more than x1.5 times messages in the average of the VOD. Default video cutter takes this and starts the clip from minute 4 and ends it in minute 6. 
As I said it all of the properties are arrangeble and since it is my first project there are tons of rooms for improvement. If you somewhat find this and if you have a opinion about it please do not hesitate to reach me. I do not expect anything I am uploading this to the Github just to make it a point in my data analysis journey.

Enjoy!
