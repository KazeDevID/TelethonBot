from .. import KazeDevID

from telethon import events, Button

@KazeDevID.on(events.NewMessage(incoming=True, pattern="/start"))

async def start(event):

    await event.reply("Hello!",

                    buttons=[

                        [Button.url("ButtonUrl", url="https://t.me/KazeDevID")],

                        [Button.inline("Inline Button",data="example")]

                    ])

@KazeDevID.on(events.callbackquery.CallbackQuery(data="example"))

async def ex(event):

    await event.edit("klik button nya🗿!")
