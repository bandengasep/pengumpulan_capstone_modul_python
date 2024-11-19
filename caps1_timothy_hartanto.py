import sys
from prettytable import PrettyTable
from pyfiglet import Figlet

def display_all_data():
    if not afc_player_stats: # check if player data is empty or not
        print("Player data is empty")
    else:
        afcTable = PrettyTable(["Player ID", "Player Name", "Position", "Age", "Goals", "Assists", "xG", "xAG"]) 
        afcTable.add_rows([
            [sub_dict.get(field, "") for field in afcTable.field_names] # flatten the list of dictionaries into a list of values
            for sub_dict in afc_player_stats
        ])
        print(f"Here is the data on all players: \n{afcTable}")

def display_data_based_on_player_id():
    global found
    global player_id_input
    found = False
    if not afc_player_stats:
        print("Player data is empty")
    else:
        # check if inputted player id is in nested dicts
        afcTable = PrettyTable(["Player ID", "Player Name", "Position", "Age", "Goals", "Assists", "xG", "xAG"]) 
        afcTable.add_rows([
            [sub_dict.get(field, "") for field in afcTable.field_names]
            for sub_dict in afc_player_stats
        ])
        print(f'The following Player IDs are available:\n{afcTable.get_string(fields = ['Player ID', 'Player Name'])}')
        
        player_id_input = input("Please input the player ID that you would like more info on.\n").upper()

        for sub_dict in afc_player_stats:
            if player_id_input == sub_dict['Player ID']:
                found = True
                filtered_afc_table = PrettyTable(["Player ID", "Player Name", "Position", "Age", "Goals", "Assists", "xG", "xAG"])
                filtered_afc_table.add_rows([
                    [sub_dict.get(field, "") for field in filtered_afc_table.field_names]
                ])
                print(f'The following player ID {player_id_input} has the following data:\n{filtered_afc_table}')
            
        if not found:
            print(f"The following {player_id_input} ID is not found on our player data.")

def quick_sort(data, key):
    """
    Quick sort function to sort a list of dictionaries based on a specified key.

    Args:
        data: A list of dictionaries to be sorted.
        key: The key to sort by.

    Returns:
        The sorted list of dictionaries.
    """

    if len(data) <= 1:
        return data

    pivot = data[len(data) // 2]
    left = [x for x in data if x[key] < pivot[key]]
    middle = [x for x in data if x[key] == pivot[key]]
    right = [x for x in data if x[key] > pivot[key]]

    sorted_data = quick_sort(left, key) + middle + quick_sort(right, key)
    return sorted_data

def sub_menu_read():
    while True:
        try:
            x = int(
                input(f"""
You have entered the read table sub-menu.
                
Please enter sub menu option:

1. Display all player data
2. Display specific data based on Player ID'
3. Sort the table based on available attribute
4. Return to Main Menu\n""")
            )
            if x == 1:
                display_all_data()
                continue
            elif x == 2:
                display_data_based_on_player_id()
                continue
            elif x == 3:
                afc_sorted_table = PrettyTable(["Player ID", "Player Name", "Position", "Age", "Goals", "Assists", "xG", "xAG"])
                inputted_key = input("""
Please input the player attributes that you would like to use as sorting: 
(Available attributes are player name, position, age, goals, assists, xg, xag)\n""").lower()
                if inputted_key in ['player name', 'position', 'age', 'goals', 'assists', 'xg', 'xag']:
                    if inputted_key == 'player name':
                        afc_sorted_table.add_rows([[sub_dict.get(field, "") for field in afc_sorted_table.field_names] for sub_dict in quick_sort(afc_player_stats, 'Player Name')])
                        print(afc_sorted_table)
                    elif inputted_key == 'position':
                        afc_sorted_table.add_rows([[sub_dict.get(field, "") for field in afc_sorted_table.field_names] for sub_dict in quick_sort(afc_player_stats, 'Position')])
                        print(afc_sorted_table)
                    elif inputted_key == 'age':
                        afc_sorted_table.add_rows([[sub_dict.get(field, "") for field in afc_sorted_table.field_names] for sub_dict in quick_sort(afc_player_stats, 'Age')])
                        print(afc_sorted_table)
                    elif inputted_key == 'goals':
                        afc_sorted_table.add_rows([[sub_dict.get(field, "") for field in afc_sorted_table.field_names] for sub_dict in quick_sort(afc_player_stats, 'Goals')])
                        print(afc_sorted_table)
                    elif inputted_key == 'assists':
                        afc_sorted_table.add_rows([[sub_dict.get(field, "") for field in afc_sorted_table.field_names] for sub_dict in quick_sort(afc_player_stats, 'Assists')])
                        print(afc_sorted_table)
                    elif inputted_key == 'xg':
                        afc_sorted_table.add_rows([[sub_dict.get(field, "") for field in afc_sorted_table.field_names] for sub_dict in quick_sort(afc_player_stats, 'xG')])
                        print(afc_sorted_table)
                    elif inputted_key == 'xag':
                        afc_sorted_table.add_rows([[sub_dict.get(field, "") for field in afc_sorted_table.field_names] for sub_dict in quick_sort(afc_player_stats, 'xAG')])
                        print(afc_sorted_table)
                else:
                    print("Inputted player attribute is invalid.")
                    continue
            elif x == 4:
                print("Returning to main menu....")
                main_menu() # replaced with function main menu
            else:
                print("Wrong number inputted. Please input the correct sub-menu number.")
        except ValueError:
            print("Incorrect input detected. Please try again.")

def sub_menu_create_new_player():
    global unique_id_counter
    while True:
        try:
            x = int(
                    input("""
You have entered the create table sub-menu.
                    
Please enter sub menu option:
                    
1. Create new player data
2. Return to main menu\n""")
                )
            if x == 1:
                unique_id_counter = len(afc_player_stats)
                current_player_name_list = [sub_dict['Player Name'] for sub_dict in afc_player_stats]
                new_player_table = PrettyTable(["Player ID", "Player Name", "Position", "Age", "Goals", "Assists", "xG", "xAG"])
                while True:
                    new_player_first_name = input("Please input the player's first name: ").replace(" ","").strip().capitalize()
                    if not new_player_first_name:  # Check if the input is empty
                        print("The name cannot be empty. Please try again.")
                    elif any(char.isdigit() for char in new_player_first_name):  # Check if the input contains a number
                        print("The name cannot contain numbers. Please try again.")
                    elif any(not char.isalpha() for char in new_player_first_name):  # Check if the input contains a special character
                        print("The name cannot contain special characters. Please try again.")
                    else:
                        break
                while True:
                    new_player_last_name = input("Please input the player's last name: ").replace(" ","").strip().capitalize()
                    if not new_player_last_name:  # Check if the input is empty
                        print("The name cannot be empty. Please try again.")
                    elif any(char.isdigit() for char in new_player_last_name):  # Check if the input contains a number
                        print("The name cannot contain numbers. Please try again.")
                    elif any(not char.isalpha() for char in new_player_last_name):  # Check if the input contains a special character
                        print("The name cannot contain special characters. Please try again.")
                    else:
                        break
                if new_player_first_name+" "+new_player_last_name in current_player_name_list:
                    print("There is already a similar player name on our database. Please input a different player name.")
                    continue
                else:
                    print("Name accepted.")
                while True:
                    new_player_position = input("""
Please input the player position (pick one): 
Accepted player position:
- GK - Goalkeepers
- DF - Defenders
- MF - Midfielders
- FW - Forwards\n""").upper()
                    if new_player_position in ["GK", "DF", "MF", "FW"]:
                        break
                    else:
                        print("Please input a valid player position.")
                while True:
                    try:
                        new_player_age = int(input("""Please input the player age: """))
                        new_player_goal = int(input("Please input the number of goals the player has scored in a season: "))
                        new_player_assist = int(input("Please input the number of assists the player has put up in a season: "))
                        new_player_xg = float(input("Please input the number of expected goals (xG) the player has put up in a season: "))
                        new_player_xag = float(input("Please input the number of expected assisted goals (xAG) the player has put up in a season: "))
                        break
                    except ValueError:
                        print("Invalid input detected. Please input a valid value")
                unique_id_counter += 1
                new_player_stats = []
                new_player_stats.append({
                        "Player ID": f"AFC_{unique_id_counter:04d}",
                        "Player Name" : new_player_first_name+' '+new_player_last_name,
                        'Position' : new_player_position,
                        'Age' : new_player_age,
                        'Goals': new_player_goal,
                        'Assists': new_player_assist,
                        'xG': new_player_xg,
                        'xAG': new_player_xag
                })
                new_player_table.add_rows([
                        [sub_dict.get(field, "") for field in new_player_table.field_names]
                        for sub_dict in new_player_stats
                ])
                print(f"This is the new data for new player:\n{new_player_table}")
                validate_data_creation = int(input("Please validate your newly created player stats.\nPress 1 to validate.\nPress 2 to cancel.\n"))
                if validate_data_creation == 1:
                    afc_player_stats.append(new_player_stats[0])
                    print("Data have been succesfully added.")
                    afcTable = PrettyTable(["Player ID", "Player Name", "Position", "Age", "Goals", "Assists", "xG", "xAG"]) 
                    afcTable.add_rows([
                        [sub_dict.get(field, "") for field in afcTable.field_names] # flatten the list of dictionaries into a list of values
                        for sub_dict in afc_player_stats
                    ])
                    print(afcTable)
                elif validate_data_creation == 2:
                    new_player_stats.clear()
                    print("New data have been cleared.")
                else:
                    print("Please input number 1 or 2.")
            elif x == 2:
                print("Returning to main menu....")
                main_menu() # Replace this with main menu function
            else:
                print("Please input a valid number.")
        except ValueError:
            print("Invalid input detected. Please try again.")

def sub_menu_update_player_data():
    while True:
        try:
            x = int(
                input(f"""
You have entered the update player table sub-menu.
                
Please enter sub menu option:

1. Update player data using player ID
2. Return to main menu\n""")
            )
            if x == 1:
                display_data_based_on_player_id()
                if found == True:
                    updated_player_list = []
                    updated_player_table = PrettyTable(["Player ID", "Player Name", "Position", "Age", "Goals", "Assists", "xG", "xAG"])
                    validate_data_update_1 = int(input("""
Would you like to continue the update?
1. Yes, continue with the update.
2. No, cancel the update.\n"""))
                    if validate_data_update_1 == 1:
                        list_index_to_update = next((index for (index, d) in enumerate(afc_player_stats) if d["Player ID"] == player_id_input), None)
                        column_to_update = input("Please input the name of the field that you would like to update for the player data: ").lower()
                        if column_to_update in ['player name', 'position', 'age', 'goals', 'assists', 'xg', 'xag']:
                            if column_to_update == 'player name':
                                while True:
                                    current_player_name_list = [sub_dict['Player Name'] for sub_dict in afc_player_stats]
                                    updated_player_first_name = input("Please input the updated player's first name: ").replace(" ","").strip().capitalize()
                                    if not updated_player_first_name:  # Check if the input is empty
                                        print("The name cannot be empty. Please try again.")
                                        continue
                                    elif any(char.isdigit() for char in updated_player_first_name):  # Check if the input contains a number
                                        print("The name cannot contain numbers. Please try again.")
                                        continue
                                    elif any(not char.isalpha() for char in updated_player_first_name):  # Check if the input contains a special character
                                        print("The name cannot contain special characters. Please try again.")
                                        continue
                                    else:
                                        pass
                                    updated_player_last_name = input("Please input the updated player's last name: ").replace(" ","").strip().capitalize()
                                    if not updated_player_last_name:  # Check if the input is empty
                                        print("The name cannot be empty. Please try again.")
                                        continue
                                    elif any(char.isdigit() for char in updated_player_last_name):  # Check if the input contains a number
                                        print("The name cannot contain numbers. Please try again.")
                                        continue
                                    elif any(not char.isalpha() for char in updated_player_first_name):  # Check if the input contains a special character
                                        print("The name cannot contain special characters. Please try again.")
                                        continue
                                    else:
                                        pass
                                    if updated_player_first_name + ' '+ updated_player_last_name in current_player_name_list:
                                        print("Inputted name has already existed. Please input a new name.")
                                        continue
                                    else:
                                        print("Name accepted.")
                                    updated_player_list.append({
                                        "Player ID": afc_player_stats[list_index_to_update]["Player ID"],
                                        "Player Name" : updated_player_first_name+' '+updated_player_last_name,
                                        'Position' : afc_player_stats[list_index_to_update]["Position"],
                                        'Age' : afc_player_stats[list_index_to_update]["Age"],
                                        'Goals': afc_player_stats[list_index_to_update]["Goals"],
                                        'Assists': afc_player_stats[list_index_to_update]["Assists"],
                                        'xG': afc_player_stats[list_index_to_update]["xG"],
                                        'xAG': afc_player_stats[list_index_to_update]["xAG"]
                                })
                                    updated_player_table.add_rows([sub_dict.get(field, "") for field in updated_player_table.field_names] # flatten the list of dictionaries into a list of values
                                        for sub_dict in updated_player_list)
                                    print(f"The following data will be updated:\n{updated_player_table.get_string(fields = ["Player ID", "Player Name"])}")
                                    
                                    final_data_update_validation = int(input("Enter ""1"" to confirm data update.\nEnter ""2"" to cancel data update.\nPlease enter your choice: "))
                                    if final_data_update_validation == 1:
                                        afc_player_stats[list_index_to_update]['Player Name'] = updated_player_first_name+' '+updated_player_last_name
                                        print("Data has been successfully updated.")
                                        break
                                    elif final_data_update_validation == 2:
                                        updated_player_list.clear()
                                        print("Updated player data has been cleared.")
                                        break
                                    else:
                                        print("Please input the correct number.")
                            elif column_to_update == 'position':
                                while True:
                                    updated_player_position = input("""
Please input the updated player position (pick one): 
Accepted player position:
- GK - Goalkeepers
- DF - Defenders
- MF - Midfielders
- FW - Forwards\n""").upper()
                                    if updated_player_position in ["GK", "DF", "MF", "FW"]:
                                        break
                                    else:
                                        print("Please input a valid player position.")
                                updated_player_list.append({
                                    "Player ID": afc_player_stats[list_index_to_update]["Player ID"],
                                    "Player Name" : afc_player_stats[list_index_to_update]["Player Name"],
                                    'Position' : updated_player_position,
                                    'Age' : afc_player_stats[list_index_to_update]["Age"],
                                    'Goals': afc_player_stats[list_index_to_update]["Goals"],
                                    'Assists': afc_player_stats[list_index_to_update]["Assists"],
                                    'xG': afc_player_stats[list_index_to_update]["xG"],
                                    'xAG': afc_player_stats[list_index_to_update]["xAG"]
                            })
                                updated_player_table.add_rows([sub_dict.get(field, "") for field in updated_player_table.field_names] # flatten the list of dictionaries into a list of values
                                    for sub_dict in updated_player_list)
                                print(f"The following data will be updated:\n{updated_player_table.get_string(fields = ["Player ID", "Position"])}")
                                
                                final_data_update_validation = int(input("Enter ""1"" to confirm data update.\nEnter ""2"" to cancel data update.\nPlease enter your choice: "))
                                if final_data_update_validation == 1:
                                    afc_player_stats[list_index_to_update]['Position'] = updated_player_position
                                    print("Data has been successfully updated.")
                                elif final_data_update_validation == 2:
                                    updated_player_list.clear()
                                    print("Updated player data has been cleared.")
                                else:
                                    print("Please input the correct number.")
                            elif column_to_update == 'age':
                                while True:
                                    try:
                                        updated_player_age = int(input("""Please input the updated player age: """))
                                        updated_player_list.append({
                                        "Player ID": afc_player_stats[list_index_to_update]["Player ID"],
                                        "Player Name" : afc_player_stats[list_index_to_update]["Player Name"],
                                        'Position' : afc_player_stats[list_index_to_update]["Position"],
                                        'Age' : updated_player_age,
                                        'Goals': afc_player_stats[list_index_to_update]["Goals"],
                                        'Assists': afc_player_stats[list_index_to_update]["Assists"],
                                        'xG': afc_player_stats[list_index_to_update]["xG"],
                                        'xAG': afc_player_stats[list_index_to_update]["xAG"]
                                })
                                        updated_player_table.add_rows([sub_dict.get(field, "") for field in updated_player_table.field_names] # flatten the list of dictionaries into a list of values
                                            for sub_dict in updated_player_list)
                                        print(f"The following data will be updated:\n{updated_player_table.get_string(fields = ["Player ID", "Age"])}")
                                        
                                        final_data_update_validation = int(input("Enter ""1"" to confirm data update.\nEnter ""2"" to cancel data update.\nPlease enter your choice: "))
                                        if final_data_update_validation == 1:
                                            afc_player_stats[list_index_to_update]['Age'] = updated_player_age
                                            print("Data has been successfully updated.")
                                            break
                                        elif final_data_update_validation == 2:
                                            updated_player_list.clear()
                                            print("Updated player data has been cleared.")
                                            break
                                        else:
                                            print("Please input the correct number.")
                                    except ValueError:
                                        print("Invalid input detected. Please input a valid value")
                            elif column_to_update == 'goals':
                                while True:
                                    try:
                                        updated_player_goal = int(input("Please input the updated number of goals the player has scored in a season: "))
                                        updated_player_list.append({
                                        "Player ID": afc_player_stats[list_index_to_update]["Player ID"],
                                        "Player Name" : afc_player_stats[list_index_to_update]["Player Name"],
                                        'Position' : afc_player_stats[list_index_to_update]["Position"],
                                        'Age' : afc_player_stats[list_index_to_update]["Age"],
                                        'Goals': updated_player_goal,
                                        'Assists': afc_player_stats[list_index_to_update]["Assists"],
                                        'xG': afc_player_stats[list_index_to_update]["xG"],
                                        'xAG': afc_player_stats[list_index_to_update]["xAG"]
                                })
                                        updated_player_table.add_rows([sub_dict.get(field, "") for field in updated_player_table.field_names] # flatten the list of dictionaries into a list of values
                                            for sub_dict in updated_player_list)
                                        print(f"The following data will be updated:\n{updated_player_table.get_string(fields = ["Player ID", "Goals"])}")
                                        
                                        final_data_update_validation = int(input("Enter ""1"" to confirm data update.\nEnter ""2"" to cancel data update.\nPlease enter your choice: "))
                                        if final_data_update_validation == 1:
                                            afc_player_stats[list_index_to_update]['Goals'] = updated_player_goal
                                            print("Data has been successfully updated.")
                                            break
                                        elif final_data_update_validation == 2:
                                            updated_player_list.clear()
                                            print("Updated player data has been cleared.")
                                            break
                                        else:
                                            print("Please input the correct number.")
                                    except ValueError:
                                        print("Invalid input detected. Please input a valid value")
                            elif column_to_update == 'assists':
                                while True:
                                    try:
                                        updated_player_assist = int(input("Please input the updated number of assists the player has put up in a season: "))
                                        updated_player_list.append({
                                        "Player ID": afc_player_stats[list_index_to_update]["Player ID"],
                                        "Player Name" : afc_player_stats[list_index_to_update]["Player Name"],
                                        'Position' : afc_player_stats[list_index_to_update]["Position"],
                                        'Age' : afc_player_stats[list_index_to_update]["Age"],
                                        'Goals': afc_player_stats[list_index_to_update]["Goals"],
                                        'Assists': updated_player_assist,
                                        'xG': afc_player_stats[list_index_to_update]["xG"],
                                        'xAG': afc_player_stats[list_index_to_update]["xAG"]
                                })
                                        updated_player_table.add_rows([sub_dict.get(field, "") for field in updated_player_table.field_names] # flatten the list of dictionaries into a list of values
                                            for sub_dict in updated_player_list)
                                        print(f"The following data will be updated:\n{updated_player_table.get_string(fields = ["Player ID", "Assists"])}")
                                        
                                        final_data_update_validation = int(input("Enter ""1"" to confirm data update.\nEnter ""2"" to cancel data update.\nPlease enter your choice: "))
                                        if final_data_update_validation == 1:
                                            afc_player_stats[list_index_to_update]['Assists'] = updated_player_assist
                                            print("Data has been successfully updated.")
                                            break
                                        elif final_data_update_validation == 2:
                                            updated_player_list.clear()
                                            print("Updated player data has been cleared.")
                                            break
                                        else:
                                            print("Please input the correct number.")
                                    except ValueError:
                                        print("Invalid input detected. Please input a valid value")
                            elif column_to_update == 'xg':
                                while True:
                                    try:
                                        updated_player_xg = float(input("Please input the updated number of expected goals (xG) the player has put up in a season: "))
                                        updated_player_list.append({
                                        "Player ID": afc_player_stats[list_index_to_update]["Player ID"],
                                        "Player Name" : afc_player_stats[list_index_to_update]["Player Name"],
                                        'Position' : afc_player_stats[list_index_to_update]["Position"],
                                        'Age' : afc_player_stats[list_index_to_update]["Age"],
                                        'Goals': afc_player_stats[list_index_to_update]["Goals"],
                                        'Assists': afc_player_stats[list_index_to_update]["Assists"],
                                        'xG': updated_player_xg,
                                        'xAG': afc_player_stats[list_index_to_update]["xAG"]
                                })
                                        updated_player_table.add_rows([sub_dict.get(field, "") for field in updated_player_table.field_names] # flatten the list of dictionaries into a list of values
                                            for sub_dict in updated_player_list)
                                        print(f"The following data will be updated:\n{updated_player_table.get_string(fields = ["Player ID", "xG"])}")
                                        
                                        final_data_update_validation = int(input("Enter ""1"" to confirm data update.\nEnter ""2"" to cancel data update.\nPlease enter your choice: "))
                                        if final_data_update_validation == 1:
                                            afc_player_stats[list_index_to_update]['xG'] = updated_player_xg
                                            print("Data has been successfully updated.")
                                            break
                                        elif final_data_update_validation == 2:
                                            updated_player_list.clear()
                                            print("Updated player data has been cleared.")
                                            break
                                        else:
                                            print("Please input the correct number.")
                                    except ValueError:
                                        print("Invalid input detected. Please input a valid value")
                            elif column_to_update == 'xag':
                                while True:
                                    try:
                                        updated_player_xag = float(input("Please input the updated number of expected assisted goals (xAG) the player has put up in a season: "))
                                        updated_player_list.append({
                                        "Player ID": afc_player_stats[list_index_to_update]["Player ID"],
                                        "Player Name" : afc_player_stats[list_index_to_update]["Player Name"],
                                        'Position' : afc_player_stats[list_index_to_update]["Position"],
                                        'Age' : afc_player_stats[list_index_to_update]["Age"],
                                        'Goals': afc_player_stats[list_index_to_update]["Goals"],
                                        'Assists': afc_player_stats[list_index_to_update]["Assists"],
                                        'xG': afc_player_stats[list_index_to_update]["Assists"],
                                        'xAG': updated_player_xag
                                })
                                        updated_player_table.add_rows([sub_dict.get(field, "") for field in updated_player_table.field_names] # flatten the list of dictionaries into a list of values
                                            for sub_dict in updated_player_list)
                                        print(f"The following data will be updated:\n{updated_player_table.get_string(fields = ["Player ID", "xAG"])}")
                                        
                                        final_data_update_validation = int(input("Enter ""1"" to confirm data update.\nEnter ""2"" to cancel data update.\nPlease enter your choice: "))
                                        if final_data_update_validation == 1:
                                            afc_player_stats[list_index_to_update]['xAG'] = updated_player_xag
                                            print("Data has been successfully updated.")
                                            break
                                        elif final_data_update_validation == 2:
                                            updated_player_list.clear()
                                            print("Updated player data has been cleared.")
                                            break
                                        else:
                                            print("Please input the correct number.")
                                    except ValueError:
                                            print("Invalid input detected. Please input a valid value")
                        else:
                            print("Inputted field is not available to be updated. Please try again.")
                            continue
                    elif validate_data_update_1 == 2:
                        print("Returning to update sub menu...")
                        continue
                    else:
                        print("Please input the correct number")
                elif found == False:
                    continue
            elif x== 2:
                print("Returning to main menu....")
                main_menu() # replaced with function main menu
            else:
                print("Wrong number inputted. Please input the correct sub-menu number.")
        except ValueError:
            print("Invalid input detected. Please try again.")

def sub_menu_delete_player_data():
    while True:
        try:
            x = int(
                input(f"""
You have entered the delete player table sub-menu.
                
Please enter sub menu option:

1. Delete player data using player ID
2. Return to main menu\n""")
            )
            if x == 1:
                display_data_based_on_player_id()
                if found == True:
                    validate_data_deletion = int(input("Would like to delete this data?\n1. Delete this data\n2. Cancel deleting this data\n"))
                    if validate_data_deletion == 1:
                        for index, player in enumerate(afc_player_stats):
                            if player['Player ID'] == player_id_input:
                                afc_player_stats.pop(index)
                            else:
                                pass
                        print("Data has been deleted.")
                elif found ==False:
                    print("The data you are looking for does not exist.")
                    continue
            elif x == 2:
                print("Returning to main menu....")
                main_menu() # replace this with main menu function
            else:
                print("Please input a valid option.")
        except ValueError:
            print("Invalid input detected. Please try again.")

def main_menu():
    while True:
        try:
            f = Figlet(font='slant')
            print(f.renderText('Arsenal Football Club Player Database'))
            x = int(input(
        """"Please pick the option below to interact with the database:
        1. Read sub-menu
        2. Create sub-menu
        3. Update sub-menu
        4. Delete sub-menu
        5. Exit the program\n"""))
            if x == 1:
                sub_menu_read()
            elif x == 2:
                sub_menu_create_new_player()
            elif x == 3:
                sub_menu_update_player_data()
            elif x == 4:
                sub_menu_delete_player_data()
            elif x == 5:
                print("Exiting the program....")
                sys.exit()
            else:
                print("Please input the provided option.")
        except ValueError:
            print("Invalid input detected. Please input a valid option.")

# instatiate a list of dictionaries filled with the Arsenal Football Club player stats
afc_player_stats = [
    {"Player ID": "AFC_0001", "Player Name": "William Saliba", "Position": "DF", "Age": 22, "Goals": 2, "Assists": 1, "xG": 1.6, "xAG": 0.2},
    {"Player ID": "AFC_0002", "Player Name": "Declan Rice", "Position": "MF", "Age": 24, "Goals": 7, "Assists": 8, "xG": 3.3,  "xAG": 3.3},
    {"Player ID": "AFC_0003", "Player Name": "Martin Odegaard", "Position": "MF", "Age": 24, "Goals": 8,  "Assists": 10, "xG": 7.4, "xAG": 5.8}
]

main_menu()
