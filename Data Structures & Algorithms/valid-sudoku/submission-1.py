class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        aux = {}

        for i in range(9):
            line = f"line{i}"
            aux[line] = {}

            for j in range(9):
                column = f"column{j}"

                if not column in aux:
                    aux[column] = {}

                value = board[i][j]

                if value == ".":
                    continue

                box_line, box_column = i // 3, j // 3

                box = f"box{box_line}{box_column}"

                if not box in aux:
                    aux[box] = {}
                    
                if not value in aux[box]:
                    aux[box][value] = (i, j)
                else:
                    return False

                if value in aux[line] or value in aux[column]:
                    return False

                aux[column][value] = (i, j)
                aux[line][value] = (i, j)

        
        return True