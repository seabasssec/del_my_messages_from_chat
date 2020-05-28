# del_my_messages_from_chat
You can delete all messages from the telegram chat by specifying its ID

Before working with Telegram’s API, you need to get your own API ID and hash:<br>

&nbsp;&nbsp;&nbsp;&nbsp;1. Login to your Telegram account (https://my.telegram.org/) with the phone number of the developer account to use.<br>
&nbsp;&nbsp;&nbsp;&nbsp;2. Click under API Development tools.<br>
&nbsp;&nbsp;&nbsp;&nbsp;3. A Create new application window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.<br>
&nbsp;&nbsp;&nbsp;&nbsp;4. Click on Create application at the end. Remember that your API hash is secret and Telegram won’t let you revoke it. Don’t post it anywhere!<br>

requirements:<br>
&nbsp;&nbsp;&nbsp;&nbsp;telethone (pip3 install -U telethon --user)<br> 

It is also worth noting that telegram traffic is blocked in some countries. In this case, use a proxy.<br>
