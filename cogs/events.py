from discord.ext import commands
import discord
import json


from modals.constants import tmw_id, event_map

class Event(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.myguild = self.bot.get_guild(tmw_id)

    @commands.Cog.listener()
    async def on_scheduled_event_create(self, event):
        event_role = await self.myguild.create_role(
            name=f'{event.name} by {event.creator.name}',
            reason=f'Event role for {event.name} by {event.creator}.',
            mentionable=True
        )
        event_creator = self.myguild.get_member(event.creator.id)
        events_path = event_map
        try:
            with open(events_path, "r") as file:
                events = json.load(file)
        except FileNotFoundError:
            events = {}
        
        events[str(event.id)] = event_role.id
        
        with open(events_path, "w") as file:
            json.dump(events, file)
        
        if event_creator:
            await event_creator.add_roles(event_role, reason=f'Event role for creating {event.name}.')
        
    @commands.Cog.listener()
    async def on_scheduled_event_user_add(self, event, user):
        events_path = event_map
        try:
            with open(events_path, "r") as file:
                events = json.load(file)
        except FileNotFoundError:
            events = {}
        
        user = self.myguild.get_member(user.id)
        role_id = events.get(str(event.id))
        if role_id:
            role = self.myguild.get_role(role_id)
            if role:
                await user.add_roles(role, reason=f'Interested in {event.name}, got its role.')
        
    @commands.Cog.listener()
    async def on_scheduled_event_user_remove(self, event, user):
        events_path = event_map
        try:
            with open(events_path, "r") as file:
                events = json.load(file)
        except FileNotFoundError:
            events = {}
            
        user = self.myguild.get_member(user.id)
        role_id = events.get(str(event.id))
        if role_id:
            role = self.myguild.get_role(role_id)
            if role:
                await user.remove_roles(role, reason=f'Uninterested in {event.name}, remove its role.')
        
    @commands.Cog.listener()
    async def on_scheduled_event_update(self, before, after):
        # Check if the event has ended
        if before.status != discord.EventStatus.completed and after.status == discord.EventStatus.completed:
            events_path = event_map
            try:
                with open(events_path, "r") as file:
                    events = json.load(file)
            except FileNotFoundError:
                events = {}

            role_id = events.pop(str(after.id), None)
            if role_id:
                role = self.myguild.get_role(role_id)
                if role:
                    await role.delete(reason=f'Event "{after.name}" has ended, removing its role.')

            with open(events_path, "w") as file:
                json.dump(events, file)

    @commands.Cog.listener()
    async def on_scheduled_event_delete(self, event):
        events_path = event_map
        try:
            with open(events_path, "r") as file:
                events = json.load(file)
        except FileNotFoundError:
            events = {}
        
        role_id = events.pop(str(event.id), None)
        if role_id:
            role = self.myguild.get_role(role_id)
            if role:
                await role.delete(reason=f'Event "{event.name}" got deleted, removing its role.')

        with open(events_path, "w") as file:
            json.dump(events, file)
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Event(bot))
