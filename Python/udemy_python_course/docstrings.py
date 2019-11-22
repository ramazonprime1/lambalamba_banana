def game_company(game_name='cricket', company_name='EA Sports'):
    print (f'the game name is {game_name} and the gaming studio is {company_name}')
    '''
    Info: this function will take names and company name and prints the output.
    '''
game_company('Red Dead Redemption 2', 'Rock Star Games')
                # function using default parameters, default parameters come into play when arguments are missing.

help(game_company)

print (game_company.__doc__)