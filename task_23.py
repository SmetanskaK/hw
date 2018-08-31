def chess_reward():
    corns = 1
    total_corns = 1
    cell_number = 1
    while total_corns < 1000000:
        cell_number = cell_number + 1
        corns = corns * 2
        total_corns = total_corns + corns
    return cell_number, total_corns


print("Cell number is %d, total corns is %d" % chess_reward())

