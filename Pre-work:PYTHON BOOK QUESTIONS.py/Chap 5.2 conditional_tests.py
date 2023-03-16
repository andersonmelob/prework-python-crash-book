best_fighters = ['jon jones', 'anderson silva', 'gsp']
for fighter in best_fighters:
    if fighter == 'jon jones':
        print("The best fighter of the world is by far " + fighter.upper())
        print()
        print("And the are others very good ones such as:")
    else:
        print(fighter.title())
        if fighter == 'gsp':
            print()
            print("But " + fighter.lower() + " is the best strategist fighter the UFC have had!\n")
best_bjj_fighters = ['royce gracie', 'charles do bronx', 'werdum', 'demian maia']
for bjj in best_bjj_fighters:
    if bjj == 'charles do bronx':
        print("bjj.upper() + ' is the most skilled guy on the ground!\n")
  