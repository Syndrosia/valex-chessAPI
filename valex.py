board = [
   ["a1", "w_r_1"], ["a2", "w_p_1"], ["a3", ""], ["a4", ""], ["a5", ""], ["a6", ""], ["a7", "b_p_1"], ["a8", "b_r_1"], 
   ["b1", "w_kn_1"], ["b2", "w_p_2"], ["b3", ""], ["b4", ""], ["b5", ""], ["b6", ""], ["b7", "b_p_2"], ["b8", "b_kn_1"], 
   ["c1", "w_b_1"], ["c2", "w_p_3"], ["c3", ""], ["c4", ""], ["c5", ""], ["c6", ""], ["c7", "b_p_3"], ["c8", "b_b_1"], 
   ["d1", "w_kg"], ["d2", "w_p_4"], ["d3", ""], ["d4", ""], ["d5", ""], ["d6", ""], ["d7", "b_p_4"], ["d8", "b_q_1"], 
   ["e1", "w_q_1"], ["e2", "w_p_5"], ["e3", ""], ["e4", ""], ["e5", ""], ["e6", ""], ["e7", "b_p_5"], ["e8", "b_kg"], 
   ["f1", "w_b_2"], ["f2", "w_p_6"], ["f3", ""], ["f4", ""], ["f5", ""], ["f6", ""], ["f7", "b_p_6"], ["f8", "b_b_2"], 
   ["g1", "w_kn_2"], ["g2", "w_p_7"], ["g3", ""], ["g4", ""], ["g5", ""], ["g6", ""], ["g7", "b_p_7"], ["g8", "b_kn_2"], 
   ["h1", "w_r_2"], ["h2", "w_p_8"], ["h3", ""], ["h4", ""], ["h5", ""], ["h6", ""], ["h7", "b_p_8"], ["h8", "b_r_2"]
   ]
print("Input your moves in the format: \"w_p_1>a2\". This entry would move your white pawn 1 to position \"a2\"")
turn = "white" #prerequisitories 

for i in range(99):
   if turn == "white":
      piece, position, sep = "null", "null", 0
      turn = "black" # turn switcher
      wmove = input("where and what do you want to move: ")
      # extractor     
      for k in range(len(wmove)):
         if wmove[k] == ">":
            sep = k; break
      piece, position = wmove[0:sep], wmove[sep + 1:len(wmove)]
   elif turn == "black":
      turn = "white"
