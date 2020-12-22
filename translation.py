class Translation(object):

    START_MSG = """[👋](https://i.imgur.com/wF1voFb.gif)  Hello **{}**

ALL IN ONE BOT HAHA :
○ Url Uploader ○ Renamer ○ YouTube DL
"""
    HELP_USER = """Hi **{}** 👋

● **For URL Uploader** :
    
○ Send Url. [ Link|New Name With Extension ] (Optional)
○ Send Custom Thumbnail. (Optional)
○ Select The Button :

🎞+📸 SVideo - Give File As Video With Screenshots
📁+📸 DFile  - Give File With Screenshots

🎞 Video  - Give File As Video Without Screenshots
📁 File  - Give File Without Screenshots

● **For Renamer** :

○ Send Me The File To Be Renamed.
○ Send Me A Thumbnail.
○ Reply To That Message With /rename New Name.extension. (📁 Upload As File)
○ Reply to that message with /renamevideo New Name.extension (🎞 Upload As Video)
"""

    ABOUT = """Hi {},

**📝 Language:** Python 3 

**🧰 Framework:** Pyrogram

**📮 Channel:** [@DamienSoukara](https://t.me/DamienSoukara)

**👥 Group:** [@DamienHelp](https://t.me/DamienHelp)

**👨‍💻 Developer:** [@AmineSoukara](t.me/AmineSoukara)

**©️ Source Code:** [Here](t.me/)

"""
    CURENT_PLAN_DETAILS = """ℹ **Current Plan Details :**
Telegram ID: <code>{}</code>
Plan Name: Free  User
Expires On: 01/01/2021"""

    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_START = "🔻 Trying To Download, Please Wait"
    UPLOAD_START = "🔺️ Trying To Upload, Please Wait"
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.5GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Please rate me if you find me useful. Join : @DamienSoukara"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \nJoin : @DamienSoukara \nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.dog/Aminesoukara'>@AmineSoukara</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."

    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /rename with custom thumbnail support"
    AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days.\n© @DamienRobot"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/RoBot"
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/damiensoukara>@DamienSoukara</a>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

    MOREHELP = """[💬](https://i.imgur.com/z0gaQ0Y.jpg)
Extra Help Haha 
"""

    YTDL = """● YouTube DL

○ Send Me A Tumbnail if required. It'll be saved permanently.💯
○ If Thumbnail Wasn't Set By You, It'll Be Auto Generated From The File.🥳
○ Send Me Youtube Link To Be Uploaded To Telegram.
○ Press /deletethumbnail To Delete Your Current Custom Thumbnail

NB : It is Recommended To Use A Custom Thubnail Because, Some Time Bot Wont Upload The File Without a Custom Thumbnail.
"""
    URLDL = """● For URL Uploader :
    
○ Send Url. [ Link|New Name With Extension ] (Optional)
○ Send Custom Thumbnail. (Optional)
○ Select The Button :

🎞+📸 SVideo - Give File As Video With Screenshots
📁+📸 DFile  - Give File With Screenshots

🎞 Video  - Give File As Video Without Screenshots
📁 File  - Give File Without Screenshots
"""
    RENAMERX = """● For Renamer :

○ Send Me The File To Be Renamed.
○ Send Me A Thumbnail.
○ Reply To That Message With /rename New Name.extension. (📁 Upload As File)
○ Reply to that message with /renamevideo New Name.extension (🎞 Upload As Video)
"""
