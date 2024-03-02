from utils import Cmd, get_group, helplist, Module, Argument as Arg, Command, b, code, ModifyPyrogramClient as App
from pyrogram.types import Message as M, ChatPrivileges as CP, ChatPermissions as CP
from pyrogram.errors.exceptions.bad_request_400 import UsernameNotOccupied
from pyrogram.utils import zero_datetime
from datetime import datetime, timedelta
from pytimeparse.timeparse import timeparse

helplist.add_module(
    Module(
        "admin",
        description="Модуль для удобного администрирования чата",
        author="@RimMirK",
        version="1.0.0"
    ).add_command(
        Command('title', [Arg('Ответ на сообщение'), Arg('Ник')], "Установить ник (титулку)")
    )
)

cmd = Cmd(get_group())

@cmd(['title'])
async def _title(app: App, msg: M):
    if not msg.reply_to_message:
        return await msg.edit("Ответь на сообщение!")

    me = app.me
    try: me_member = await msg.chat.get_member(me.id)
    except: return await msg.edit("Тут нельзя устанавливать ники")

    user = msg.reply_to_message.from_user
    user_memeber = await msg.chat.get_member(user.id)


    if not me_member.privileges:
        return await msg.edit("Ты не админ")
    if not me_member.privileges.can_promote_members:
        return await msg.edit("Ты не можешь установливать ники")
    
    if user_memeber.promoted_by != app.me.id:
        await msg.chat.promote_member(user.id, CP())

    await app.set_administrator_title(
        msg.chat.id,
        user.id,
        msg.text.split(maxsplit=1)[1]
    )
    return await msg.edit("Готово")
    
    


@cmd(['mute', 'ro'])
async def _mute(app: App, msg: M):
    _, *args = msg.text.split()
    r = msg.reply_to_message
    if not r:
        try:
            u = await app.get_users(args[0])
        except (UsernameNotOccupied, IndexError):
            return await msg.edit(
                b("Ответь на сообщение или укажи юзернейм пользователя через ")
                + code('@') + b(' !')
            )
    else:
        u = r.from_user or r.sender_chat

    if u.id == app.me.id:
        return await msg.edit(
            b("Ты не можешь мутить самого себя!")
        )

    try: m = await app.get_chat_member(msg.chat.id, u.id)
    except ValueError as e:
        if str(e).startswith('The chat_id'):
            return await msg.edit(
                b("Это Личные Сообщения, тут нельзя никого замутить!")
            )
        else: raise e()
    

    t = None
    for arg in args:
        t = timeparse(arg)
        if t: break


    await app.restrict_chat_member(msg.chat.id, u.id,
        CP(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_polls=False,
            can_send_other_messages=False
        ),
        datetime.now() + timedelta(seconds=t) if t else zero_datetime()
    )


    
    