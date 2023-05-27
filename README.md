# twitch_clip_maker

This is my first project, so it's a bit scuffed. The main purpose of this program is to detect the moments in a long stream when chat messages exceed the average message in the total VOD and create clips of these minutes. There must be a text file named suggested chat.log, and also it requires the VOD as the name suggested Video.mp4. These files can be obtained through TwitchDownloaderGUI.

First, open "chat_analysis" in this code; it is possible to select which multiplayer of the average you want, such as finding the minutes where the chat wrote messages x1.5 or x2 times compared to the average. Then you will get the minutes list.

Next, open "video_cutter" and write these minutes as input. You have the option to select the length of the clips. Also, I thought there was a little lag behind chat depending on the stream, so it would be better to start the clip one minute before. For example: In minute 5, there are more than x1.5 times messages in the average of the VOD. The default video cutter takes this and starts the clip from minute 4 and ends it in minute 6. 

As I said, all of the properties are arranged, and since it is my first project, there are tons of room for improvement. If you find this and have an opinion about it, please do not hesitate to reach me. I do not expect anything. I am uploading this to GitHub to make it a point in my data analysis journey.

Enjoy!
