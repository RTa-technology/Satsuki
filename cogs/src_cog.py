# !/usr/bin/env python3
# -*- coding: utf-8 -*-


import typing

import discord
from discord.ext import commands  # Bot Commands Frameworkのインポート

import libs as lib

SCP_JP = "http://ja.scp-wiki.net"
BRANCHS = ['jp', 'en', 'ru', 'ko', 'es', 'cn',
           'fr', 'pl', 'th', 'de', 'it', 'ua', 'pt', 'uo']


class Tachibana_Tale(commands.Cog):  # コグとして用いるクラスを定義

    def __init__(self, bot):  # TestCogクラスのコンストラクタBotを受取り、インスタンス変数として保持
        self.bot = bot
        self.URL = "http://ja.scp-wiki.net"

    @commands.command()
    async def tale(self, ctx, word: str):
        '''if brt not in BRANCHS:
            brt = "*"
        '''
        reply = lib.src_tale(word)

        if len(reply) > 10:
            await ctx.send(f"ヒット{len(reply)}件、多すぎます")
            return

        embed = discord.Embed(
            title="TALE検索結果",
            description=f"検索ワード'{word}'にヒットしたTaleは{len(reply)}件です",
            color=0xff8000)

        for line in reply.itertuples():
            embed.add_field(
                name=line[2],
                value=self.URL + line[1] + "\nAuthor : " + line[3],
                inline=False)

        embed.set_footer(text="タイトル、URL、著者名から検索しています")
        await ctx.send(embed=embed)

    @tale.error
    async def tale_error(self, ctx, error):
        if discord.ext.commands.errors.BadArgument:
            await ctx.send('入力値が不正です')
        else:
            admin_id = self.bot.json_data['admin']['id']  # なんで？？？？？
            await ctx.send(f'to <@{admin_id}> at {ctx.command.name} command\n{error}')

    @commands.command(aliases=['prop'])
    async def proposal(self, ctx, word: str):

        reply = lib.src_proposal(word)

        if len(reply) > 10:
            await ctx.send(f"ヒット{len(reply)}件、多すぎます")
            return

        embed = discord.Embed(
            title="提言検索結果",
            description=f"検索ワード'{word}'にヒットした提言は{len(reply)}件です",
            color=0x0080c0)

        for line in reply.itertuples():
            embed.add_field(
                name=line[2],
                value=f"{self.URL}{line[1]}",
                inline=False)

        embed.set_footer(text="タイトル、URLから検索しています")
        await ctx.send(embed=embed)

    @proposal.error
    async def proposal_error(self, ctx, error):
        if discord.ext.commands.errors.BadArgument:
            await ctx.send('入力値が不正です')
        else:
            admin_id = self.bot.json_data['admin']['id']  # なんで？？？？？
            await ctx.send(f'to <@{admin_id}> at {ctx.command.name} command\n{error}')

    @commands.command()
    async def joke(self, ctx, word: str):
        reply = lib.src_joke(word)

        if len(reply) > 10:
            await ctx.send(f"ヒット{len(reply)}件、多すぎます")
            return

        embed = discord.Embed(
            title="joke検索結果",
            description=f"検索ワード'{word}'にヒットしたjokeは{len(reply)}件です",
            color=0x800080)

        for line in reply.itertuples():
            embed.add_field(
                name=line[2],
                value=f"{self.URL}{line[1]}",
                inline=False)

        embed.set_footer(text="タイトル、URLから検索しています")
        await ctx.send(embed=embed)

    @joke.error
    async def joke_error(self, ctx, error):
        if discord.ext.commands.errors.BadArgument:
            await ctx.send('入力値が不正です')
        else:
            admin_id = self.bot.json_data['admin']['id']  # なんで？？？？？
            await ctx.send(f'to <@{admin_id}> at {ctx.command.name} command\n{error}')

    @commands.command(aliases=['gd'])
    async def guide(self, ctx, word: str):
        reply = lib.src_guide(word)

        if len(reply) > 10:
            await ctx.send(f"ヒット{len(reply)}件、多すぎます")
            return

        embed = discord.Embed(
            title="ガイド検索結果",
            description=f"検索ワード'{word}'にヒットしたガイドは{len(reply)}件です",
            color=0x800080)

        for line in reply.itertuples():
            embed.add_field(
                name=line[2],
                value=f"{self.URL}{line[1]}",
                inline=False)

        embed.set_footer(text="タイトル、URLから検索しています")
        await ctx.send(embed=embed)

    @guide.error
    async def guide_error(self, ctx, error):
        if discord.ext.commands.errors.BadArgument:
            await ctx.send('入力値が不正です')
        else:
            admin_id = self.bot.json_data['admin']['id']  # なんで？？？？？
            await ctx.send(f'to <@{admin_id}> at {ctx.command.name} command\n{error}')

    @commands.command(aliases=['auth'])
    async def author(self, ctx, word: str):
        reply = lib.src_author(word)

        if len(reply) > 10:
            await ctx.send(f"ヒット{len(reply)}件、多すぎます")
            return

        embed = discord.Embed(
            title="著者ページ検索結果",
            description=f"検索ワード'{word}'にヒットした著者ページは{len(reply)}件です",
            color=0x8000ff)

        for line in reply.itertuples():
            embed.add_field(
                name=line[2],
                value=f"{self.URL}{line[1]}",
                inline=False)

        embed.set_footer(text="著者名から検索しています")
        await ctx.send(embed=embed)

    @author.error
    async def author_error(self, ctx, error):
        if discord.ext.commands.errors.BadArgument:
            await ctx.send('入力値が不正です')
        else:
            admin_id = self.bot.json_data['admin']['id']  # なんで？？？？？
            await ctx.send(f'to <@{admin_id}> at {ctx.command.name} command\n{error}')

    @commands.command(aliases=['ex'])
    async def explained(self, ctx, word: str):
        reply = lib.src_explained(word)

        if len(reply) > 10:
            await ctx.send(f"ヒット{len(reply)}件、多すぎます")
            return

        embed = discord.Embed(
            title="explained検索結果",
            description=f"検索ワード'{word}'にヒットしたexplainedは{len(reply)}件です",
            color=0x000080)

        for line in reply.itertuples():
            embed.add_field(
                name=line[2],
                value=f"{self.URL}{line[1]}",
                inline=False)

        embed.set_footer(text="タイトル、URLから検索しています")
        await ctx.send(embed=embed)

    @explained.error
    async def explained_error(self, ctx, error):
        if discord.ext.commands.errors.BadArgument:
            await ctx.send('入力値が不正です')
        else:
            admin_id = self.bot.json_data['admin']['id']  # なんで？？？？？
            await ctx.send(f'to <@{admin_id}> at {ctx.command.name} command\n{error}')


def setup(bot):  # Bot本体側からコグを読み込む際に呼び出される関数
    bot.add_cog(Tachibana_Tale(bot))  # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する
