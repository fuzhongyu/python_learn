#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' qqBot '
from qqbot import QQBotSlot as qqbotslot, RunBot

__author__ = 'fucai'


@qqbotslot
def onQQMessage(bot, contact, member, content):
    # if 'XXX' in contact.name:
    #     if '/Emoji128054' in content or '狗' in content or 'dog' in content:
    #         bot.SendTo(contact, 'message1')
    #     elif '娘' in content or 'niang' in content or '炮' in content or 'pao' in content:
    #         bot.SendTo(contact, 'message2')

    if '马' in contact.name:
        bot.SendTo(contact, '马威峰')

if __name__ == '__main__':
    RunBot()