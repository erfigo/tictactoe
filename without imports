player1 = ""
player2 = ""
turn = ""
gameover = True

board = []
winning = [
  [0,1,2],
  [3,4,5],
  [6,7,8],
  [8,3,6],
  [1,4,7],
  [2,5,8],
  [0,4,8],
  [2,4,6]]
  @bot.command()
async def ttt(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameover

    if gameover:
        global board
        board = [":purple_square:", ":purple_square:", ":purple_square:",
                 ":purple_square:", ":purple_square:", ":purple_square:",
                 ":purple_square:", ":purple_square:", ":purple_square:"]
        turn = ""
        gameover = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@bot.command()
async def p(ctx, pos :int):
  global turn
  global player1
  global player2
  global board
  global count

  
  if not gameover:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":purple_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winning, mark)
                print(count)
                if gameover:
                    await ctx.send(mark + " wins! :fire::fire:")
                elif count >= 9:
                    await ctx.send("TIE GAME")
                    return
                    

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Please choose $p 1 to $p 9 for selecting your tiles and only fill the unmarked tiles.")
        else:
            await ctx.send("It is not your turn.")
  else:
        await ctx.send("Please start a new game by inputting $ttt and by tagging yourself and your friend:fire::pray_tone1:")

def checkWinner(winning, mark):
  global gameover
  for condition in winning:
    if board[condition[0]]==mark and board[condition[1]]==mark and board[condition[2]]==mark:
      gameover = True
@ttt.error
async def ttt_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this game!.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention your friend!(ie. <@musicman @lo_phee>).")

@p.error
async def p_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter the position ($P 1 to $P 9) to fill the unmarked tiles!")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter a number.")
