import random
import time

#variabels
max_number = 21 
player_number = 0
dealer_number = 0 
turn = 0 
running = True

#eerste zet
while running:
    while turn < 1:
        playercard = random.randint(1,11)
        playercard2 = random.randint(1,11)
        print(f'je hebt een {playercard} en een {playercard2} samen is dat {playercard2 + playercard}')
        player_number = player_number + playercard +playercard2
        dealercard = random.randint(1,11)
        dealercard2 = random.randint(1,11)
        print(f'de dealer heeft {dealercard}')
        dealer_number = dealer_number + dealercard2 + dealercard
        turn = turn + 1
        if dealer_number == 21:
            print('de dealer heeft blackjack ! je hebt verloren\n')
            time.sleep(1)
            turn = 0
        if player_number == 21:
            print("blackjack ! je hebt gewonnen\n")
            time.sleep(1)
            turn = 0
            running = False
    #2de zet en verder
    while turn > 0:
        hit_of_stand = input('hit of stand ?')
        if hit_of_stand == 'hit':
            hit = random.randint(1,11)
            player_number = player_number + hit
            print(f"jij hebt {hit} gekregen dus je hebt nu in totaal heb je nu {player_number}")
            if dealer_number < 19:
                dealer_hit = random.randint(1,11)
        #stand    
        if hit_of_stand == 'stand':
            laststand = random.randint(1,11)
            if dealer_number < 17:
                while dealer_number < 15:
                    dealer_number = dealer_number + laststand
            print(f"jij hebt {player_number} en de dealer heeft {dealer_number}")
            if player_number > dealer_number:
                print("jij hebt gewonnen van de dealer !\n")
                time.sleep(1)
                running = False
                turn = 0
            else:
                print('je hebt verloren !\n')
                time.sleep(1)
                running = False
                turn = 0

        #checken of een iemand meer als 21 heeft
        if player_number > 21:
            print(f"je hebt verloren ! jij hebt {player_number} en de dealer heeft {dealer_number}\n")
            time.sleep(1)
            running = False
            turn = 0
        if dealer_number > 21:
            print(f'je hebt gewonnen ! jij hebt {player_number} en de dealer heeft {dealer_number}\n"')
            time.sleep(1)
            running = False
            turn = 0

        #kiezen om het spel op nieuw te spelen 
        if running == False:
            de_vraag = input("wil je verder spelen [y/n]\n")
        if de_vraag == "y":
            running = True
            player_number = 0
            dealer_number = 0
            turn = 0
        elif de_vraag == "n":
            pass
