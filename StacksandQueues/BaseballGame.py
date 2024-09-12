class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        total = 0
        for operation in operations:
            if operation == "C":
                total -= record.pop()
            elif operation == "D":
                temp = record[-1] * 2
                record.append(temp)
                total += temp
            elif operation == "+":
                temp = record[-1] + record[-2]
                record.append(temp)
                total += temp
            else:
                record.append(int(operation))
                total += int(operation)
        
        return total

        
        
if __name__ == "__main__":
    operations = ["5","-2","4","C","D","9","+","+"]
    obj = Solution()
    print(obj.calPoints(operations))