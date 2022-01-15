    for user in list(ctx.guild.members):
            print(f"{Fore.RED}[-]BANNING > {Fore.RESET}Attempting to ban {user}")
            try:
                await user.ban()
                print(
                    f"{Fore.RED}[-]BANNING > {Fore.RESET}Successfully banned {user}"
                )
            except:
                print(f"{Fore.RED}[-]BANNING > {Fore.RESET}Failed to ban {user}")
