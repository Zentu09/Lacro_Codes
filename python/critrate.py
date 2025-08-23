def lion_strike(lion):
    base = 150
    crit = 30
def wolf_strike(wolf):
    base = 110
    crit = 45




while True:
    print("Lion's Pride (X)")
    print("Wolf fang (C)")
    skill = input("choose a skill: ")
 
    wolf_strike(skill) 

    match skill:
        case "X":
            lion_strike(skill)
    
        case "Y":
            wolf_strike(skill)

        case _:
            break
