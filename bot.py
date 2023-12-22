try:
	import requests,re,random,wget,yt_dlp,os,datetime,time
	import telebot
	from user_agent import generate_user_agent
	from telebot import types
	from telebot.types import InlineKeyboardButton as btn
	from telebot.types import InlineKeyboardMarkup as km 
	from youtube_search import YoutubeSearch
	from yt_dlp import YoutubeDL
	from config import TOKEN
except:
	import os
	os.system("pip install requests re random wget yt_dlp pytelegrambotapi telebot user-agent youtube-search datetime")
	import requests,re,random,wget,yt_dlp,os,time
	import telebot
	from user_agent import generate_user_agent
	from telebot import types
	from telebot.types import InlineKeyboardButton as btn
	from telebot.types import InlineKeyboardMarkup as km 
	from youtube_search import YoutubeSearch
	from yt_dlp import YoutubeDL
	from config import TOKEN

def stm(seconds):
	return '{:02}:{:02}:{:02}'.format(seconds // 3600, seconds % 3600 // 60, seconds % 60)

def download_video(url, save_path,id):
	response = requests.get(url, stream=True)
	if response.status_code == 200:
		with open(save_path, "wb") as video_file:
			for chunk in response.iter_content(chunk_size=1024 * 1024):
				if chunk:
					video_file.write(chunk)
			return True

stats = btn(text="الاحصائيات",callback_data="stats")
adaa = btn(text="اذاعة",callback_data="adaa")
btns = km()
btns.add(stats,adaa)


what = {
	"adaa": False,
}
mis = {
}

token = TOKEN #توكنك
id_ch = int("-1001666751945") #ايدي قناتك
username = " @ibaghdady"  #يوزر قناك بعد @
dev = int("2010789056") #ggايدي حساب
in_msg = """
دخل شخص جديد للبوت الخاص بك.

اسمه: {}
ايديه: {}
معرفه: @{}

عدد اعضاء البوت الان {} عضو
"""

ch_msg = """
🚧┇عذراً، عليك الأشتراك في قنوات البوت أولاً،
🚧┇القناة الأولى: @iBaghdady،
🚧┇القناة الثانية: @JJGPP.
"""
name_ch1 = "أنا بغدادي🌿"
name_ch2 = "سـِلاح"

try:
	open("members.txt","r").read()
except Exception as error:
	print(error)
	open("members.txt","a").write("")

def is_member(user_id):
	one = False
	two = False
	get = requests.get(f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@iBaghdady&user_id={user_id}").text
	if user_id == "@iBaghdady" or "member" in get or "creator" in get or "administartor" in get:
		one = True
		
	get = requests.get(f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@jjgpp&user_id={user_id}").text
	if user_id == "@jjgpp" or "member" in get or "creator" in get or "administartor" in get:
		two = True
	
	if one == True and two == True:
		return True
	else:
		return False

bot = telebot.TeleBot(token)

print("@"+bot.get_me().username)
@bot.message_handler(commands=["start"])
def Welcome(message):
	name = message.from_user.first_name
	id = message.from_user.id
	#bot.forward_message(id_ch,message.chat.id,message.message_id)
	if message.from_user.id != dev:
		if is_member(id)==False:
			return bot.reply_to(
				message,
				ch_msg,
				reply_markup=km().add(
					btn(
						text=name_ch1,
						url="https://t.me/iBaghdady"
						)
					).add(btn(
						text=name_ch2,
						url="https://t.me/JJGPP"
						)
					)
				)
		members = open("members.txt","r")
		if str(message.from_user.id) not in str(members.read()):
			open("members.txt","a").write(f"{message.from_user.id}\n")
			number = 0
			for i in open("members.txt","r").readlines():
				if i != "\n":
					number += 1
			bot.send_message(dev,in_msg.format(message.from_user.first_name,message.from_user.id,message.from_user.username,number))
		else:
			pass
		bot.reply_to(message,f'''- [{name}](tg://settings)
 مرحباً  بك في بوت التحميل  👋🦇❤️‍🔥
يمكنك من خلالي تحميل الوسائط من اغلب مواقع التواصل الاجتماعي.
المواقع المدعومة ✨:
(يوتيوب، انستغرام،تيك توك، بنترست،ثريدز،تويتر،سناب جات،سبوتيفاي)
يمكنك التحميل من اليوتيوب من خلال البوت التالي 
@Youtube69bbot
	
	المالك @Rozs23bot
	.''',parse_mode="markdown",reply_markup=km([[btn("كيفية التحميل؟",callback_data="help")]]))
	else:
		bot.reply_to(message,"""
مرحبا بك سيدي في بوتك اختر ادناه...""",reply_markup=btns)
		bot.reply_to(message,f'''-  [{name}](tg://settings)
	-  مرحباً  بك في بوت التحميل  👋🦇❤️‍🔥
يمكنك من خلالي تحميل الوسائط من اغلب مواقع التواصل الاجتماعي.
المواقع المدعومة ✨:
(يوتيوب،انستغرام،تيك توك،ثريدز،بنترست،سناب جات،تويتر،سبوتيفاي)

يمكنك التحميل من اليوتيوب من خلال البوت التالي 
@Youtube69bbot

.''',parse_mode="markdown",reply_markup=km([[btn("كيفية التحميل؟",callback_data="help")]]))

@bot.message_handler(regexp="instagram.com")
def instadown(message):
	id = message.from_user.id
	if is_member(id)==False:
		return bot.reply_to(
			message,
			ch_msg,
			reply_markup=km().add(
				btn(
					text=name_ch1,
					url="https://t.me/iBaghdady"
					)
				).add(btn(
					text=name_ch2,
					url="https://t.me/JJGPP"
					)
				)
			)
	bot.forward_message(id_ch,message.chat.id,message.message_id)
	link = message.text
	print("post","reel")
	
	if what["adaa"] == "True" and message.from_user.id == dev:
		users = open("members.txt","r").readlines()
		done = 0
		for user in users:
			try:
				bot.copy_message(user,message.chat.id,message.id)
				done += 1
			except:
				continue
		bot.reply_to(message,f"تم ارسال الاذاعة الى {done} من الاعضاء")
		what["adaa"] = "False"
		return
		
	if "/p/" in link or "/reel/" in link:
		try:
			url = requests.get(f"https://apimedia.hussienalaraqe8.repl.co/instagram?url={link}").json()
			medias = []
			num_to_del =len(url["links"]["video"])
			for i in range(len(url["links"]["video"])):
				link = url["links"]["video"][i]
				if len(medias) >=10:
					bot.send_chat_action(message.chat.id,action='upload_video')
					bot.send_media_group(message.chat.id,media=medias)
					medias.clear()
					continue
						
				if "video" in link["q_text"]:
					if download_video(url["links"]["video"][i]["url"],f"video{message.chat.id}{i}.mp4",message.chat.id):
						medias.append(telebot.types.InputMediaVideo(open(f"video{message.chat.id}{i}.mp4","rb"),caption=f"{username}"))
				else:
					if download_video(url["links"]["video"][i]["url"],f"photo{message.chat.id}{i}.jpg",message.chat.id):
						medias.append(telebot.types.InputMediaPhoto(open(f"photo{message.chat.id}{i}.jpg","rb"),caption=f"{username}"))
			if len(medias) >=1:
				bot.send_chat_action(message.chat.id,action='upload_video')
				bot.send_media_group(message.chat.id,media=medias)
				for i in range(num_to_del):
					#i += 
					if "video" in url["links"]["video"][i]["q_text"]:
						os.remove(f"video{message.chat.id}{i}.mp4")
					else:
						os.remove(f"photo{message.chat.id}{i}.jpg")
		except Exception as error:
			print(error)
			bot.reply_to(message, '<i>خطأ تأكد من الرابط ..</i>', parse_mode="html")
			
	elif "/s/" in link:
		response = requests.get(f"https://apimedia.hussienalaraqe8.repl.co/highlights?url={link}").json()
		No = response['success']
		if No == False:
			bot.reply_to(message, '<i>خطأ تأكد من الرابط ..</i>', parse_mode="html")
		else:
			bot.send_chat_action(message.chat.id, action='upload_video')
			#user = response['data']['user']['username']
			media = []
			for video in response["data"]['medias']:
				if len(media) >= 10:
					bot.send_media_group(message.chat.id,media,reply_to_message_id=message.message_id)
					media.clear()
					continue
				video = video["src"]
				if ".mp4" in video:
					media.append(telebot.types.InputMediaVideo(video,caption=f"{username}"))
				else:
					media.append(telebot.types.InputMediaPhoto(video,caption=f"{username}"))
			if len(media) >=1:
				bot.send_media_group(message.chat.id,media,reply_to_message_id=message.message_id)
				media.clear()
	else:
		if "/stories/" in link:
			link = re.findall("/stories/(.*?)/",link)[0]
		else:
			link = link.split("instagram.com/")[1].split("/")[0].split("?")[0]
		print(link)
		try:
			response = requests.get(f"https://apimedia.hussienalaraqe8.repl.co/story?url={link}").json()
			bot.send_chat_action(message.chat.id, action='upload_video')
			media = []
			for video in response["result"]:
				if len(media) >= 10:
					bot.send_media_group(message.chat.id,media,reply_to_message_id=message.message_id)
					media.clear()
					continue
				if "video_versions" in video.keys():
					video = video["video_versions"][0]["url"]
					media.append(telebot.types.InputMediaVideo(video,caption=f"{username}"))
				else:
					video = video["image_versions2"]["candidates"][0]["url"]
					media.append(telebot.types.InputMediaPhoto(video,caption=f"{username}"))
			if len(media) > 1:
				bot.send_media_group(message.chat.id,media,reply_to_message_id=message.message_id)
				#bot.delete_message(message.chat.id,m.message_id)
				media.clear()
		except Exception as error:
			try:
				print(error)
				for video in response["result"]:
					if "video_versions" in video.keys():
						video = video["video_versions"][0]["url"]
						bot.send_video(message.chat.id,video)
					else:
						video = video["image_versions2"]["candidates"][0]["url"]
						bot.send_photo(message.chat.id,video)
				bot.reply_to(message,"عذرًا Sir. تم ارسالها بشكل متقطع لان الحساب يحتوي على صورة متحركة في الاستوري خاصته، وانت تدري بعمو تلكرام مايخليك تدز صورة متحركة بمجموعة صور كـAlbum واحد")
				#bot.delete_message(message.chat.id,m.message_id)
			except Exception as error:
				print(error)
				#return bot.edit_message_text( '<i>خطأ تأكد من الرابط ..</i>',message.chat.id,m.message_id,parse_mode="html")
				bot.send_message(dev,f"""
الرابط: {message.text}

رسالة الخطأ:
{error}
""")

@bot.message_handler(regexp="(youtu.be|youtube.com)")
def ytube(message):
	id = message.from_user.id
	if is_member(id)==False:
		return bot.reply_to(
			message,
			ch_msg,
			reply_markup=km().add(
				btn(
					text=name_ch1,
					url="https://t.me/iBaghdady"
					)
				).add(btn(
					text=name_ch2,
					url="https://t.me/JJGPP"
					)
				)
			)
	bot.forward_message(id_ch,message.chat.id,message.message_id)
	try:
		vid_id = message.text.split("watch?v=")[1]
	except:
		try:
			vid_id = message.text.split("youtu.be/")[1].split("?")[0]
		except:
			try:
				vid_id = message.text.split("shorts/")[1].split("?")[0]
			except:
				vid_id = message.text.split("youtu.be/")[1]
	try:
		print(vid_id)
		yt = YoutubeSearch(f'https://youtu.be/{vid_id}', max_results=1).to_dict()
		title = yt[0]['title']
		url = f'https://youtu.be/{vid_id}'
		reply_markup = km(
			[
			
				[
					btn("صوت 💿", callback_data=f'{id}AUDIO{vid_id}'),
					btn("فيديو 🎥", callback_data=f'{id}VIDEO{vid_id}'),
				]
			
			])
		bot.send_photo(
			message.chat.id,
			str(yt[0]["thumbnails"][0].split("?")[0]),
			f"**⤶ العنوان - [{title}]({url})**",
			reply_markup=reply_markup,
			parse_mode="markdown"
		)
	except Exception as error:
		bot.reply_to(message,'error );')
		bot.send_message(dev,f"""Error:

الرابط: {vid_id}

رسالة الخطأ: {str(error)}
""")
@bot.message_handler(regexp="tiktok")
def tiktokdown(message):
	bot.forward_message(id_ch,message.chat.id,message.message_id)
	msg = message.text
	id = message.from_user.id
	if is_member(id)==False:
		return bot.reply_to(
			message,
			ch_msg,
			reply_markup=km().add(
				btn(
					text=name_ch1,
					url="https://t.me/iBaghdady"
					)
				).add(btn(
					text=name_ch2,
					url="https://t.me/JJGPP"
					)
				)
			)
	msgg = bot.send_message(message.chat.id, "*جاري التحميل ...*",parse_mode="markdown")
	import wget
	try:
		url = requests.get(f'https://tikwm.com/api/?url={msg}').json()
		music = url['data']['music']
		region = url['data']['region']
		#tit = url['data']['title']
		if "images" in str(url["data"].keys()):
			vid = url["data"]["images"]
		else:
			vid = url['data']['play']
		ava = url['data']['author']['avatar']
		rand = str("".join(random.choice("qwertyuiopasdfghjklzxcvbnm")for i in range(5)))
		mis[rand] = music
		name = url['data']['music_info']['author']
		time = url['data']['duration']
		sh = url['data']['share_count']
		com = url['data']['comment_count']
		wat = url['data']['play_count']
		bot.delete_message(chat_id=message.chat.id, message_id=msgg.message_id)
		ava = wget.download(ava)
		bot.send_photo(message.chat.id,open(ava,"rb"),caption=f'- اسم الحساب : *{name}*\n - دوله الحساب : *{region}*\n\n- عدد مرات المشاهدة : *{wat}*\n- عدد التعليقات : *{com}*\n- عدد مرات المشاركة : *{sh}*\n- طول الفيديو : *{time}*',parse_mode="markdown")
		os.remove(ava)
		if "list" in str(type(vid)):
			photos = []
			btns = km().add(btn('تحميل الصوت',callback_data=rand))
			files = []
			for photo in vid:
				filename = wget.download(photo)
				files.append(filename)
				photos.append(telebot.types.InputMediaPhoto(open(filename,"rb"),caption=f"{username}"))
				if len(photos) ==10:
					bot.send_media_group(message.chat.id,media=photos,reply_to_message_id=message.message_id)
					photos.clear()
					continue
			if len(photos) >1:
				bot.send_media_group(message.chat.id,media=photos,reply_to_message_id=message.message_id)
				bot.send_message(message.chat.id,"هل تريد تحميل الصوت؟",reply_markup=btns)
				for file in files:
					os.remove(file)
			return
		btns = km().add(btn('تحميل الصوت',callback_data=rand))
		try:
			bot.send_video(message.chat.id,vid, caption=f"{username}",reply_markup=btns)
		except:
			filename = wget.download(vid)
			bot.send_video(message.chat.id,open(filename,"rb"), caption=f"{username}",reply_markup=btns)
	except Exception as error:
		print(error)
		
		url = requests.get(f"https://apimedia.hussienalaraqe8.repl.co/tiktokV2?url={message.text}").json()
		print(url)
		if url["type"] == "video":
			link = url["links"][0]
			bot.send_video(message.chat.id,link,caption=f"{username}")
		else:
			audio = url["audio"]
			links = url["links"][1:]
			media = []
			for link in links:
				media.append(telebot.types.InputMediaPhoto(link,caption=f"{username}"))
			rand = str("".join(random.choice("qwertyuiopasdfghjklzxcvbnm")for i in range(5)))
			mis[rand] = audio
			btns = km().add(btn('تحميل الصوت',callback_data=rand))
			bot.send_media_group(message.chat.id,media)
			bot.send_message(message.chat.id,"هل تريد تحميل الصوت؟",reply_markup=btns)
			bot.delete_message(chat_id=message.chat.id, message_id=msgg.message_id)
#		except Exception as erroe:
			#bot.reply_to(message,'error );')
#			bot.send_message(dev,f"""Error:
#	
#	الرابط: {msg}
#	
#	رسالة الخطأ: {str(error)}
#	""")
@bot.message_handler(regexp="^(http|https)://pin.it")
def pintrst(message):
	bot.forward_message(id_ch,message.chat.id,message.message_id)
	print("pint")
	id = message.from_user.id
	if is_member(id)==False:
		return bot.reply_to(
			message,
			ch_msg,
			reply_markup=km().add(
				btn(
					text=name_ch1,
					url="https://t.me/iBaghdady"
					)
				).add(btn(
					text=name_ch2,
					url="https://t.me/JJGPP"
					)
				)
			)
	#site = "home"
	msg = bot.reply_to(message,"__جاري التحميل__",parse_mode="markdown")
	try:
		url = requests.get(f"https://apimedia.hussienalaraqe8.repl.co/pinterest?url={message.text}").json()
		
		link = url["link"]
		#print(link)
		photo = url["thmub"]
			
		response= requests.get(photo)
		with open(f"{message.chat.id}.png", "wb") as file:
			file.write(response.content)
		#thumb = f"{message.chat.id}.png" 
		
		if download_video(link,f"video{message.chat.id}.mp4",message.chat.id):
			bot.send_chat_action(message.chat.id,action='upload_video')
			bot.send_video(
				message.chat.id,
				open(f"video{message.chat.id}.mp4","rb"),
				caption=f'{username}',
				thumb=open(f"{message.chat.id}.png","rb"))
			os.remove(f"video{message.chat.id}.mp4")
			os.remove(f"{message.chat.id}.png")
			bot.delete_message(message.chat.id,msg.message_id)
	except Exception as error:
		print(error)
		bot.edit_message_text("**حدث خطأ**",message.chat.id,msg.message_id,parse_mode="markdown")
		bot.send_message(dev,f"""
الرابط: {message.text}

رسالة الخطأ:
{error}
""")

@bot.message_handler(regexp="^(https|http)://(spotify|open.spotify)")
def spotyyify(message):
	id = message.from_user.id
	bot.forward_message(id_ch,message.chat.id,message.message_id)
	if is_member(id)==False:
		return bot.reply_to(
			message,
			ch_msg,
			reply_markup=km().add(
				btn(
					text=name_ch1,
					url="https://t.me/iBaghdady"
					)
				).add(btn(
					text=name_ch2,
					url="https://t.me/JJGPP"
					)
				)
			)
	msg = bot.reply_to(message,"__جاري التحميل__",parse_mode="markdown")
	song = requests.get(f"https://apimedia.hussienalaraqe8.repl.co/spotify?url={message.text}").json()
	title = song["title"]
	link = song["link"]
	ydl_ops = {"format": "bestaudio[ext=m4a]"}
	try:
		with yt_dlp.YoutubeDL(ydl_ops) as ydl:
			info_dict = ydl.extract_info(link, download=False)
			if int(info_dict['duration']) > 700:
				return bot.edit_message_text(
						chat_id=message.chat.id,
						text="**⚠️ حد التحميل ساعة ونص فقط**",
						message_id=msg.id,
						parse_mode="html",
				)
			file_name = ydl.prepare_filename(info_dict)
			ydl.process_info(info_dict)
			bot.send_audio(
				chat_id=message.chat.id,
				audio=open(file_name,"rb"),caption=f"{title}",
				performer=info_dict['channel'],
				title=info_dict['title'],
				reply_to_message_id=message.message_id)
			bot.delete_message(message.chat.id,msg.id)
			os.remove(file_name)
	except Exception as error:
		print(error)
		return bot.edit_message_text(
			chat_id=message.chat.id,
			text="**⚠️ صار خطأ**",
			message_id=msg.id,
			parse_mode="html",
		)

@bot.message_handler(regexp="^(https|http)://(twitter|x).com")
def twitter(message):
	id = message.from_user.id
	bot.forward_message(id_ch,message.chat.id,message.message_id)
	if is_member(id)==False:
		return bot.reply_to(
			message,
			ch_msg,
			reply_markup=km().add(
				btn(
					text=name_ch1,
					url="https://t.me/iBaghdady"
					)
				).add(btn(
					text=name_ch2,
					url="https://t.me/JJGPP"
					)
				)
			)
	m = bot.reply_to(message,"جاري التحميل...")
	try:
		response = requests.get(f"https://apimedia.hussienalaraqe8.repl.co/twitter?url={message.text}").json()
		link = response["link"]
		number = random.randint(1,100)
		download_video(link,f"{number}.mp4",id)
		vid = bot.send_video(
			chat_id=message.chat.id,
			video=open(f"{number}.mp4","rb"),
			caption=f"احفظ الفيديو عندك سيتم حذفه بعد 10 ثواني.\n{username}",
			reply_to_message_id=message.message_id
		)
		os.remove(f"{number}.mp4")
		bot.delete_message(message.chat.id,m.message_id)
		time.sleep(10)
		bot.delete_message(message.chat.id,vid.message_id)
	except Exception as error:
		print(error)
		bot.edit_message_text("حصل خطأ.",message.chat.id,m.message_id)
		bot.send_message(dev,f"""
الرابط: {message.text}

رسالة الخطأ:
{error}
""")

@bot.message_handler(regexp="^(https|http)://(snapchat.com|t.snapchat.com)")
def snapchatdef(message):
	id = message.from_user.id
	bot.forward_message(id_ch,message.chat.id,message.message_id)
	if is_member(id)==False:
		return bot.reply_to(
			message,
			ch_msg,
			reply_markup=km().add(
				btn(
					text=name_ch1,
					url="https://t.me/iBaghdady"
					)
				).add(btn(
					text=name_ch2,
					url="https://t.me/JJGPP"
					)
				)
			)
	m = bot.reply_to(message,"جاري التحميل.")
	msg = message.text
	#bot.edit_message_text("جاري التحميل..",message.chat.id,m.message_id)
	try:
		info = requests.get(f"https://apimedia.hussienalaraqe8.repl.co/snapchat?url={msg}").json()
		print(info)
		url = info["link"]
		title = info["title"]
		bot.edit_message_text("جاري التحميل...",message.chat.id,m.message_id)
		bot.send_chat_action(message.chat.id,action='upload_video')
		bot.send_video(message.chat.id,url,caption=f'{title}\n@ibaghdady')
		bot.delete_message(message.chat.id,m.message_id)
		#os.remove(f"video{message.chat.id}.mp4")
	except Exception as error:
		print(error)
		bot.edit_message_text("حصل خطأ.",message.chat.id,m.message_id)
		bot.send_message(dev,f"""
الرابط: {msg}

رسالة الخطأ:
{error}
""")

@bot.message_handler(regexp="^(https|http)://(story.snapchat.com|story.snapchat.com/)")
def snapchatdefstory(message):
	id = message.from_user.id
	bot.forward_message(id_ch,message.chat.id,message.message_id)
	if is_member(id)==False:
		return bot.reply_to(
			message,
			ch_msg,
			reply_markup=km().add(
				btn(
					text=name_ch1,
					url="https://t.me/iBaghdady"
					)
				).add(btn(
					text=name_ch2,
					url="https://t.me/JJGPP"
					)
				)
			)
	m = bot.reply_to(message,"جاري التحميل.")
	msg = message.text
	try:
		info = requests.get(f"https://apimedia.hussienalaraqe8.repl.co/snapStory?url={msg}").json()
		print(info)
		url = info["link"]
		title = info["title"]
		bot.edit_message_text("جاري الرفع...",message.chat.id,m.message_id)
		media = []
		for i in link:
			if len(media) >=10:
				bot.send_chat_action(message.chat.id,action='upload_video')
				bot.send_media_group(message.chat.id,media)
				media.clear()
				continue
			if i["snapMediaType"] == 1:
				media.append(telebot.types.InputMediaVideo(i))
			else:
				media.append(telebot.types.InputMediaPhoto(i))
		if len(media) >= 1:
			bot.send_chat_action(message.chat.id,action='upload_video')
			bot.send_media_group(message.chat.id,media)
			media.clear()
		bot.reply_to(message,f'تم تحميل الستوريات.\n{title}\n@ibaghdady')
		bot.delete_message(message.chat.id,m.message_id)
		#os.remove(f"video{message.chat.id}.mp4")
	except Exception as error:
		print(error)
		bot.edit_message_text("حصل خطأ.",message.chat.id,m.message_id)
		bot.send_message(dev,f"""
الرابط: {msg}

رسالة الخطأ:
{error}
""")

@bot.message_handler(regexp="^(https|http)://(threads.net|www.threads.net)")
def threds(message):
	id = message.from_user.id
	bot.forward_message(id_ch,message.chat.id,message.message_id)
	if is_member(id)==False:
		return bot.reply_to(
			message,
			ch_msg,
			reply_markup=km().add(
				btn(
					text=name_ch1,
					url="https://t.me/iBaghdady"
					)
				).add(btn(
					text=name_ch2,
					url="https://t.me/JJGPP"
					)
				)
			)
	m = bot.reply_to(message,"جاري التحميل...")
	msg =  message.text
	try:
		response = requests.get(f"https://apimedia.hussienalaraqe8.repl.co/threads?url={msg}").json()
		title = response['title']
		url = response["link"]
		bot.send_chat_action(message.chat.id,action='upload_video')
		bot.send_video(
			message.chat.id,
			url,
			caption=f"{title}\n{username}",
			reply_to_message_id=message.id)
		bot.delete_message(message.chat.id,m.message_id)
	except Exception as error:
		print(error)
		bot.send_message(dev,f"""
الرابط: {msg}

رسالة الخطأ:
{error}
""")
		bot.edit_message_text("حصل خطأ..",message.chat.id,m.message_id)

@bot.message_handler(regexp="^(https|http)://(fb.watch|facebook.com)")
def facbok(message):
	m = bot.reply_to(message,"جاري التحميل...")
	bot.forward_message(id_ch,message.chat.id,message.message_id)
	msg = message.text
	try:
		url = requests.get(f"https://apimedia.hussienalaraqe8.repl.co/facebook?url={msg}").json()
		if url["result"] == False:
			return bot.edit_message_text("لم أجد الفيديو حاول برابط اخر.",message.chat.id,m.message_id)
		link = url["links"][0]
		if not ".mp4" in link:
			link=url["links"][1]
		bot.send_chat_action(message.chat.id,action='upload_video')
		
		bot.send_video(
			message.chat.id,
			video=link,
			caption=f"{username}",
			reply_markup=km().add(btn(text="•الرابط•",url=message.text))
			)
		bot.delete_message(message.chat.id,m.message_id)
	except Exception as error:
		print(error)
		bot.edit_message_text("حدث خطأ ما.",message.chat.id,m.message_id)
		bot.send_message(dev,f"""
الرابط: {msg}

رسالة الخطأ:
{error}
""")

@bot.message_handler(commands=["search"])
def searchyout(message):
	name = message.from_user.first_name
	id = message.from_user.id
	if is_member(id)==False:
		return bot.reply_to(
			message,
			ch_msg,
			reply_markup=km().add(
				btn(
					text=name_ch1,
					url="https://t.me/iBaghdady"
					)
				).add(btn(
					text=name_ch2,
					url="https://t.me/JJGPP"
					)
				)
			)
	if len(message.text.split(None, 1)) < 2:
		return bot.reply_to(message,"اكتب شيء للبحث عنه.")
	#query = message.text.replace("/search ","")
	query = message.text.split(None, 1)[1]
	re = YoutubeSearch(query, max_results=5).to_dict()
	buttons = km()
	buttons.add(btn(re[0]["title"],callback_data=f"GET{re[0]['id']}"))
	buttons.add(btn(re[1]["title"],callback_data=f"GET{re[1]['id']}"))
	buttons.add(btn(re[2]["title"],callback_data=f"GET{re[2]['id']}"))
	buttons.add(btn(re[3]["title"],callback_data=f"GET{re[3]['id']}"))
	buttons.add(btn(re[4]["title"],callback_data=f"GET{re[4]['id']}"))
	#buttons.add(btn(re[5]["title"],callback_data=f"GET{re[5]['id']}"))
	
	bot.reply_to(message,"نتائج بحثك.",reply_markup=buttons)

@bot.message_handler(regexp="^(@|[a-zA-Z]|[0-9])")
def from_user(message):
	id = message.from_user.id
	bot.forward_message(id_ch,message.chat.id,message.message_id)
	if is_member(id)==False:
		return bot.reply_to(
			message,
			ch_msg,
			reply_markup=km().add(
				btn(
					text=name_ch1,
					url="https://t.me/iBaghdady"
					)
				).add(btn(
					text=name_ch2,
					url="https://t.me/JJGPP"
					)
				)
			)
	if what["adaa"] == "True" and message.from_user.id == dev:
		users = open("members.txt","r").readlines()
		done = 0
		for user in users:
			try:
				bot.copy_message(user,message.chat.id,message.id)
				done += 1
			except:
				continue
		bot.reply_to(message,f"تو ارسال الاذاعة الى {done} من الاعضاء")
		what["adaa"] = "False"
		return
	
	#print(message.text)
	msg = bot.reply_to(message,"جاري التحميل...")
	if "@" in message.text:
		link = message.text.split("@")[1]
	else:
		link = message.text
	print(link)
	try:
		response = requests.get(f"https://apimedia.hussienalaraqe8.repl.co/story?url={link}").json()
		bot.send_chat_action(message.chat.id, action='upload_video')
		media = []
		for video in response["result"]:
			if len(media) >= 10:
				bot.send_media_group(message.chat.id,media,reply_to_message_id=message.message_id)
				media.clear()
				continue
			if "video_versions" in video.keys():
				video = video["video_versions"][0]["url"]
				media.append(telebot.types.InputMediaVideo(video,caption=f"{username}"))
			else:
				video = video["image_versions2"]["candidates"][0]["url"]
				media.append(telebot.types.InputMediaPhoto(video,caption=f"{username}"))
				
		if len(media) > 1:
			bot.send_media_group(message.chat.id,media,reply_to_message_id=message.message_id)
			media.clear()
		bot.delete_message(message.chat.id,msg.message_id)
	except Exception as error:
		try:
			print(error)
			for video in response["result"]:
				if "video_versions" in video.keys():
					video = video["video_versions"][0]["url"]
					bot.send_video(message.chat.id,video)
				else:
					video = video["image_versions2"]["candidates"][0]["url"]
					bot.send_photo(message.chat.id,video)
			bot.reply_to(message,"عذرًا Sir. تم ارسالها بشكل متقطع لان الحساب يحتوي على صورة متحركة في الاستوري خاصته، وانت تدري بعمو تلكرام مايخليك تدز صورة متحركة بمجموعة صور كـAlbum واحد")
			bot.delete_message(message.chat.id,msg.message_id)
		except Exception as error:
			print(error)
			bot.edit_message_text("صار خطأ او لم يتم أيجاد ستوري في الحساب.",message.chat.id,msg.message_id)
				
			bot.send_message(dev,f"""
الرابط: {message.text}

رسالة الخطأ:
{error}
""")

@bot.message_handler(func = lambda message:True)
def sterad(message):
	id = message.from_user.id
	if is_member(id)==False:
		return bot.reply_to(
			message,
			ch_msg,
			reply_markup=km().add(
				btn(
					text=name_ch1,
					url="https://t.me/iBaghdady"
					)
				).add(btn(
					text=name_ch2,
					url="https://t.me/JJGPP"
					)
				)
			)
	if what["adaa"] == "True" and message.from_user.id == dev:
		users = open("members.txt","r").readlines()
		done = 0
		error = []
		for user in users:
			try:
				bot.copy_message(user,message.chat.id,message.id)
				done += 1
			except:
				error.append(user)
				print(user)
				continue
		print(error)
		what["adaa"] = "False"
		if len(error) >= 1:
			for user in error:
				users.remove(user)
			os.remove("members.txt")
			open("members.txt","a").write("")
			for i in users:
				open("members.txt","a").write(i+"\n")
			#for i in range(users):
#				open("members.txt","a").write(users)
		bot.reply_to(message,f"تم ارسال الاذاعة الى {done} من الاعضاء\n\n الاعضاء الذين حظروا البوت {len(error)}")
		return
	bot.forward_message(id_ch,message.chat.id,message.message_id)
@bot.callback_query_handler(func=lambda call: True)
def call(call):
	backk = btn(text = "رجوع",callback_data="back")
	back = km()
	back.add(backk)
	if call.data == "stats":
		#file = open("members.txt","r")
		users = 0
		for i in open("members.txt","r").readlines():
			if i != "\n":
				users += 1
		bot.edit_message_text(chat_id=call.message.chat.id,text=f"""
قائمة الاعضاء.

عدد الاعضاء: {users}
""",message_id=call.message.id,reply_markup=back)

	elif call.data == "adaa":
		bot.edit_message_text(chat_id=call.message.chat.id,text="تمام، دز اارسالة وراح ادزها للكل تدلل سيدي.",message_id=call.message.id,reply_markup=back)
		what["adaa"] = "True"
		
	elif call.data == "back":
		bot.edit_message_text(chat_id=call.message.chat.id,text="مرحبا بك سيدي في بوتك اختر ادناه...",message_id=call.message.id,reply_markup=btns)
		what["adaa"] = "False"
	
	elif "GET" in call.data:
		vid_id = call.data.split("GET")[1]
		url = f'https://youtu.be/{vid_id}'
		bot.delete_message(call.message.chat.id,call.message.message_id)
		try:
			print(vid_id)
			yt = YoutubeSearch(f'https://youtu.be/{vid_id}', max_results=1).to_dict()
			title = yt[0]['title']
			url = f'https://youtu.be/{vid_id}'
			reply_markup = km(
				[
				
					[
						btn("صوت 💿", callback_data=f'{id}AUDIO{vid_id}'),
						btn("فيديو 🎥", callback_data=f'{id}VIDEO{vid_id}'),
					]
				
				])
			bot.send_photo(
				call.message.chat.id,
				str(yt[0]["thumbnails"][0].split("?")[0]),
				f"**⤶ العنوان - [{title}]({url})**",
				reply_markup=reply_markup,
				parse_mode="markdown"
			)
		except Exception as error:
			bot.reply_to(call.message,'error );')
			bot.send_message(dev,f"""Error:

الرابط: {vid_id}

رسالة الخطأ: {str(error)}
""")
	
	elif "AUDIO" in call.data:
		vid_id = call.data.split("AUDIO")[1]
		url = f'https://youtu.be/{vid_id}'
		try:
			downloading = km([[btn(" أنا بغدادي🌿",url="https://t.me/iBaghdady ")]])
			uploading = km([[btn(" أنا بغدادي🌿",url="https://t.me/iBaghdady ")]])
			erroring = km([[btn("Error ⚠️",url="https://t.me/iBaghdady ")]])
			bot.edit_message_caption(
				chat_id=call.message.chat.id,
				caption="**جاري التحميل ..**",
				message_id=call.message.id,
				reply_markup=downloading,
				parse_mode="html"
			)
			url = f'https://youtu.be/{vid_id}'
			ydl_ops = {"format": "bestaudio[ext=m4a]"}
			with yt_dlp.YoutubeDL(ydl_ops) as ydl:
				info_dict = ydl.extract_info(url, download=False)
				if int(info_dict['duration']) > 5006:
					return bot.edit_message_caption(
						chat_id=call.message.chat.id,
						caption="**⚠️ حد التحميل ساعة ونص فقط**",
						message_id=call.message.id,
						reply_markup=erroring,
						parse_mode="html",
					)
				try:
					audio_file = ydl.prepare_filename(info_dict)
					ydl.process_info(info_dict)
					bot.edit_message_caption(
						chat_id=call.message.chat.id,
						caption="**جاري الارسال...**",
						message_id=call.message.id,
						reply_markup=uploading,
						parse_mode="html"
					)
					response= requests.get(info_dict['thumbnail'])
					with open(f"{vid_id}.png", "wb") as file:
						file.write(response.content)
					thumb = f"{vid_id}.png"
					bot.send_audio(
						chat_id=call.message.chat.id,
						audio=open(audio_file,"rb"),
						title=info_dict['title'],
						duration=int(info_dict['duration']),
						performer=info_dict['channel'],
						thumb=thumb,
						reply_markup=downloading
					)
					bot.edit_message_caption(
						chat_id=call.message.chat.id,
						caption="تم التحميل",
						message_id=call.message.id,
					)
					os.remove(audio_file)
					os.remove(thumb)
					return
				except Exception as error:
					bot.edit_message_caption(
						chat_id=call.message.chat.id,
						caption="**صار خطأ.**",
						message_id=call.message.id,
						parse_mode="html",
						reply_markup=erroring
					)
					bot.send_message(dev,f"""Error:

الرابط: {url}

رسالة الخطأ: {str(error)}
""")
					
		except Exception as error:
			bot.edit_message_caption(
				chat_id=call.message.chat.id,
				caption="**صار خطأ.**",
				message_id=call.message.id,
				parse_mode="html",
				reply_markup=erroring
			)
			bot.send_message(dev,f"""Error:

الرابط: {url}

رسالة الخطأ: {str(error)}
""")
	elif "VIDEO" in call.data:
		try:
			vid_id = call.data.split("VIDEO")[1]
			url = f'https://youtu.be/{vid_id}'
			downloading = km([[btn(" أنا بغدادي🌿",url="https://t.me/iBaghdady ")]])
			uploading = km([[btn(" أنا بغدادي🌿",url="https://t.me/iBaghdady ")]])
			erroring = km([[btn("Error ⚠️",url="https://t.me/iBaghdady ")]])
			bot.edit_message_caption(
				chat_id=call.message.chat.id,
				caption="**جاري التحميل ..**",
				message_id=call.message.id,
				reply_markup=downloading,
				parse_mode="markdown"
			)
			ydl_opts = {
				"format": "best",
				"keepvideo": True,
				"prefer_ffmpeg": False,
				"geo_bypass": True,
				"outtmpl": "%(title)s.%(ext)s",
				"quite": True,
			}
			with YoutubeDL(ydl_opts) as ytdl:
				ytdl_data = ytdl.extract_info(url, download=True)
				if int(ytdl_data['duration']) > 5006:
					return bot.edit_message_caption(
							chat_id=call.message.chat.id,
							caption="**⚠️ حد التحميل ساعة ونص فقط**",
							message_id=call.message.id,
							reply_markup=error,
							parse_mode="html",
						)
				try:
					file_name = ytdl.prepare_filename(ytdl_data)
					bot.edit_message_caption(
							chat_id=call.message.chat.id,
							caption="**جاري الارسال...**",
							message_id=call.message.id,
							reply_markup=uploading,
							parse_mode="html"
					)
					response= requests.get(ytdl_data['thumbnail'])
					with open(f"{vid_id}.png", "wb") as file:
						file.write(response.content)
					thumb = f"{vid_id}.png"
					bot.send_video(
						call.message.chat.id,
							video=open(file_name,"rb"),
							duration=int(ytdl_data['duration']),
							thumb=thumb,
							reply_markup=downloading
					)
					os.remove(file_name)
					os.remove(thumb)
					bot.edit_message_caption(
						chat_id=call.message.chat.id,
						caption="تم التحميل",
						message_id=call.message.id,
					)
				except Exception as err:
					bot.edit_message_caption(
						chat_id=call.message.chat.id,
						caption="**صار خطأ.**",
						message_id=call.message.id,
						parse_mode="html",
						reply_markup=erroring
					)
					bot.send_message(dev,f"""Error:	
	الرابط: {url}
	
	رسالة الخطأ: {str(err)}
	""")
		except Exception as err:
			bot.edit_message_caption(
				chat_id=call.message.chat.id,
				caption="**صار خطأ.**",
				message_id=call.message.id,
				parse_mode="html",
				reply_markup=erroring
			)
			bot.send_message(dev,f"""Error:	
الرابط: {url}

رسالة الخطأ: {str(err)}
""")
	elif call.data == "help":
		bot.edit_message_text("""
لمعرفة كيفية التحميل:

1. الانستكرام: ارسال الفيديو/المنشور او ارسال معرف الحساب لتحميل الستوريات.

2. التيك توك: ارسال الرابط فقط.

3. بينترست: ارسال رابط الفيديو فقط

4. يوتيوب: ارسال رابط الفيديو او اذا اردت البحث عليك وضع /search قبل كلمة البحث
او يمكنك التحميل من اليوتيوب من خلال البوت  التالي   
@Youtube69bbot

الباقي كلهم ارسال الرابط فقط.""",call.message.chat.id,call.message.message_id)
	else:
		if mis[call.data]:
			audio = mis[call.data]
			return bot.send_audio(call.message.chat.id,audio)

@bot.message_handler(content_types=['photo',"voice","sticker","video","animation","document"])
def ada(message):
	id = message.from_user.id
	if is_member(id)==False:
		return bot.reply_to(
			message,
			ch_msg,
			reply_markup=km().add(
				btn(
					text=name_ch1,
					url="https://t.me/iBaghdady"
					)
				).add(btn(
					text=name_ch2,
					url="https://t.me/JJGPP"
					)
				)
			)
	if what["adaa"] == "True" and message.from_user.id == dev:
		users = open("members.txt","r").readlines()
		done = 0
		error = []
		for user in users:
			print(user)
			try:
				bot.copy_message(user,message.chat.id,message.id)
				done += 1
			except:
				error.append(user)
				continue
		what["adaa"] = "False"
		print(users)
		if len(error) >= 1:
			for user in error:
				users.remove(user)
				
			os.remove("members.txt")
			open("members.txt","a").write("")
			for i in users:
				open("members.txt","a").write(i+"\n")
			#for i in range(users):
#				open("members.txt","a").write(users)
		bot.reply_to(message,f"تم ارسال الاذاعة الى {done} من الاعضاء\n\n الاعضاء الذين حظروا البوت {len(error)}")
		return
	bot.forward_message(id_ch,message.chat.id,message.message_id)

bot.infinity_polling()
