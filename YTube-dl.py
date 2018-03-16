import requests,os,json
from colorama import init
from termcolor import colored
from urllib import urlopen, unquote
from urlparse import parse_qs, urlparse
from clint.textui import progress
defaultApiKey = "{Enter Your Api Key Here}"
def banner():
    global Id
    global video_id
    banner = colored("""                                                                              
@@@ @@@  @@@@@@@  @@@  @@@  @@@@@@@   @@@@@@@@             @@@@@@@   @@@@@@@  
@@@ @@@  @@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@             @@@@@@@@  @@@@@@@  
@@! !@@    @@!    @@!  @@@  @@!  @@@  @@!                  @@!  @@@    @@!    
!@! @!!    !@!    !@!  @!@  !@   @!@  !@!                  !@!  @!@    !@!    
 !@!@!     @!!    @!@  !@!  @!@!@!@   @!!!:!    @!@!@!@!@  @!@  !@!    @!!    
  @!!!     !!!    !@!  !!!  !!!@!!!!  !!!!!:    !!!@!@!!!  !@!  !!!    !!!    
  !!:      !!:    !!:  !!!  !!:  !!!  !!:                  !!:  !!!    !!:    
  :!:      :!:    :!:  !:!  :!:  !:!  :!:                  :!:  !:!    :!:    
   ::       ::    ::::: ::   :: ::::   :: ::::              :::: ::     ::    
   :        :      : :  :   :: : ::   : :: ::              :: :  :      :""","red",attrs={"bold"})     
    print banner
    print """            """+colored("Coded with <3 by Ijaz Ur Rahim a.k.a Muhammad Ibraheem","yellow")
    print """            """+colored("https://ijazurrahim.com/","blue",attrs={"bold","underline"})+"  "+colored("https://github.com/IJAZ9913/","blue",attrs={"bold","underline"})
    video_url = raw_input(colored("Enter the Video Url: ","green",attrs={"bold","underline"}))
    try:
        video_id = parse_qs(urlparse(video_url).query)['v'][0]
        Id = video_id
    except:
        print colored("[-] You Entered an Invalid Url!","red",attrs={"bold","blink","underline"})
        exit(0)
init()
if os.name=="nt":
    os.system("cls")
else:
    os.system("clear")
def bytes_2_human_readable(number_of_bytes):
    if number_of_bytes < 0:
        unit='--'

    step_to_greater_unit = 1024.

    number_of_bytes = float(number_of_bytes)
    unit = 'bytes'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'KB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'MB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'GB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'TB'

    precision = 1
    number_of_bytes = round(number_of_bytes, precision)

    return str(number_of_bytes) + ' ' + unit

def pros():
    try:
        if rData["error"]["errors"][0]["reason"]=="keyInvalid":
            apiKey = raw_input(colored("API expired, Please create your own and Enter Here: ","green"))
            req(apiKey)
    except:    
        if len(rData["items"])==0:
            exit(colored("Video id is incorrect","red"))
        for items in rData["items"]:
            print colored("id: ","red",attrs={"bold"})+colored(items["id"],"blue",attrs={"bold"})
            print colored("Title: ","red",attrs={"bold"})+colored(items["snippet"]["title"].encode('utf-8'),"blue",attrs={"bold"})
            print colored("Description (300 Chars): \n","red",attrs={"bold"})+colored(items["snippet"]["description"][:300].encode('utf-8'),"blue",attrs={"bold"})
            print colored("Thumbnail: ","red",attrs={"bold"})+colored(items["snippet"]["thumbnails"]["default"]["url"],"blue",attrs={"bold"})
            print colored("Publish Date: ","red",attrs={"bold"})+colored(items["snippet"]["publishedAt"][:10]+" "+items["snippet"]["publishedAt"][11:][:8],"blue",attrs={"bold"})
            print colored("Channel Id: ","red",attrs={"bold"})+colored(items["snippet"]["channelId"],"blue",attrs={"bold"})
            print colored("Channel Name: ","red",attrs={"bold"})+colored(items["snippet"]["channelTitle"].encode('utf-8'),"blue",attrs={"bold"})
            try:
                tags=""
                for tag in items["snippet"]["tags"].encode('utf-8'):
                    tags = tags + tag +","
                print colored("Tags: \n","red",attrs={"bold"})+colored(tags,"blue",attrs={"bold"})
            except:
                pass
            try:
                print colored("Language: ","red",attrs={"bold"})+colored(items["snippet"]["defaultLanguage"].encode('utf-8'),"blue",attrs={"bold"})
            except:
                pass
            try:
                print colored("Audio Language: ","red",attrs={"bold"})+colored(items["snippet"]["defaultAudioLanguage"].encode('utf-8'),"blue",attrs={"bold"})
            except:
                pass
            duration = ""
            time = items["contentDetails"]["duration"][2:]
            for char in time:
                if char =="M":
                    duration = duration + " Minute(s) "
                elif char == "S":
                    duration = duration + " Second(s)"
                elif char == "H":
                    duration = duration + " Hour(s) "
                else:
                    duration = duration + char
                
            print colored("Duration: ","red",attrs={"bold"})+colored(duration,"blue",attrs={"bold"})
            print colored("Quality: ","red",attrs={"bold"})+colored(items["contentDetails"]["definition"],"blue",attrs={"bold"})
            print colored("Caption: ","red",attrs={"bold"})+colored(items["contentDetails"]["caption"].encode('utf-8'),"blue",attrs={"bold"})
            print colored("Licensed to Owner: ","red",attrs={"bold"})+colored(items["contentDetails"]["licensedContent"],"blue",attrs={"bold"})
            print colored("Status: ","red",attrs={"bold"})+colored(items["status"]["uploadStatus"],"blue",attrs={"bold"})
            print colored("Privacy: ","red",attrs={"bold"})+colored(items["status"]["privacyStatus"],"blue",attrs={"bold"})
            try:
                print colored("Number of Views: ","red",attrs={"bold"})+colored(items["statistics"]["viewCount"],"blue",attrs={"bold"})
            except:
                pass
            try:
                print colored("Number of Likes: ","red",attrs={"bold"})+colored(items["statistics"]["likeCount"],"blue",attrs={"bold"})
            except: 
                pass    
            try:
                print colored("Number of Dislikes: ","red",attrs={"bold"})+colored(items["statistics"]["dislikeCount"],"blue",attrs={"bold"})
            except: 
                pass
            try:
                print colored("Saved as Favourite: ","red",attrs={"bold"})+colored(items["statistics"]["favoriteCount"],"blue",attrs={"bold"})
            except: 
                pass
            try:
                print colored("Numbers of Comments: ","red",attrs={"bold"})+colored(items["statistics"]["commentCount"],"blue",attrs={"bold"})
            except: 
                pass
            print colored("Related Articles:","red",attrs={"bold"})
            for article in items["topicDetails"]["topicCategories"]:
                print  "\t"+colored(article.encode('utf-8'),"blue",attrs={"bold"})
            video_info = urlopen('https://www.youtube.com/get_video_info?&video_id=' + video_id).read().decode('utf-8')
            try:
                try:
                    a = parse_qs(video_info)["adaptive_fmts"][0]
                except:
                    a = parse_qs(video_info)["url_encoded_fmt_stream_map"][0]
            except:
                video_info = urlopen('http://www.youtube.com/get_video_info?el=detailpage&eurl=&ps=default&video_id=' + video_id).read().decode('utf-8')
                try:
                    a = parse_qs(video_info)["adaptive_fmts"][0]
                except:
                    a = parse_qs(video_info)["url_encoded_fmt_stream_map"][0]
            videos = {"Type":{},"Size":{},"Extension":{},"Url":{},"Quality":{}}
            b=0
            for types in  parse_qs(a)["type"]:
                typess =types.split(";",1)
                videos["Type"][b],videos["Extension"][b]= typess[0].encode('utf-8').split("/",1)
                b = b + 1
            b=0
            for url in  parse_qs(a)["url"]:
                videos["Url"][b] = url.encode('utf-8')
                size = urlopen(url)
                if size.getcode()==403:
                    continue
                byte = bytes_2_human_readable(size.headers["Content-Length"])
                videos["Size"][b]= byte
                b = b + 1
            try:
                b=0
                for quality in  parse_qs(a)["quality_label"]:
                    quality = quality.split(",",1)
                    videos["Quality"][b] = quality[0].encode('utf-8')
                    b = b + 1
            except:
                for quality in  parse_qs(a)["quality"]:
                    quality = quality.split(",",1)
                    videos["Quality"][b] = quality[0].encode('utf-8')
                    b = b + 1
            if len(videos["Size"])<1:
                print colored("[-] No Link to Download","red",attrs={"bold"})
                exit = raw_input(colored("Press Enter/Return to exit","green"))
                break
            duration = int(parse_qs(video_info)["length_seconds"][0].encode('utf-8'))/60
            print "{0:<15}{1:<15}{2:<15}{3:<15}{4:15}".format("S.No","Type","Size","Extension","Quality")
            b=0
            while b<len(videos["Url"]):
                try:
                    print colored("{0:<15}{1:<15}{2:<15}{3:<15}{4:15}".format(b+1,videos["Type"][b],videos["Size"][b],videos["Extension"][b],videos["Quality"][b]),"green")
                except:
                    pass
                b = b + 1
            option = raw_input("Please Select from one of the above: ")
            try:
                file_name = parse_qs(video_info)["title"][0]+"."+videos["Extension"][int(option)-1]
                link = videos["Url"][int(option)-1]
            except:    
                print colored("[-] Invalid Selection","red",attrs={"bold"})
                exit = raw_input(colored("Press Enter/Return to exit","green"))
                break
            r = requests.get(link, stream=True)
            try:
                with open(file_name, 'wb') as f:
                    total_length = int(r.headers.get('content-length'))
                    for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                        if chunk:
                            f.write(chunk)
                            f.flush()
            except:
                try:
                    with open("File1."+videos["Extension"][int(option)-1], 'wb') as f:
                        total_length = int(r.headers.get('content-length'))
                        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                            if chunk:
                                f.write(chunk)
                                f.flush()
                except:
                    print colored("[-] Download Failed","red",attrs={"bold"})            
            exit = raw_input(colored("Press Enter/Return to exit","green"))


def req(apiKey = defaultApiKey):
    global rData
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "id":Id,
        "key":apiKey,
        "fields":"items",
        "part":"snippet,contentDetails,status,statistics,topicDetails"
    }
    req = requests.get(url,params)
    data = req.content
    rData = json.loads(data)
    pros()
banner()
req()