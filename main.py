@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await member.send(f" you have unmuted from: - {ctx.guild.name}")
    embed = discord.Embed(
        title="Unmuted",
        description=f" Removed the sound proof glass from {member.mention}",
        colour=discord.Colour.orange())
    await ctx.send(embed=embed)
