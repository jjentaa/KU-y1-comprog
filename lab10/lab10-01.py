def readMat(fn='gauss01.txt'):
    m = []
    with open(fn) as fp:
        for line in fp:
            row = line.strip().split()
            m.append(row)
    return m

def printMat(m):
    for row in m:
        printed_row = ''
        for elem in row:
            printed_row += f'{elem:>8}'
        print(printed_row)
    print()

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.said_suan_low()

    def said_suan_low(self):
        gcd = self._find_gcd(abs(self.numerator), abs(self.denominator))
        self.numerator //= gcd
        self.denominator //= gcd
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    @staticmethod
    def _find_gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def __add__(self, other):
        new_sad = self.numerator * other.denominator + other.numerator * self.denominator
        new_suan = self.denominator * other.denominator
        return Fraction(new_sad, new_suan)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

def gaussian_elimination(mat):
    for col in range(len(mat)):
        pivot = mat[col][col]

        print(f"R{col+1} => R{col+1}/({pivot})")
        
        for j in range(col, len(mat)+1):
            mat[col][j] = mat[col][j] * Fraction(pivot.denominator, pivot.numerator)
        
        printed_mat = []
        for row in mat:
            printed_row = []
            for elem in row:
                printed_row.append(str(elem))
            printed_mat.append(printed_row)
        printMat(printed_mat)
        
        for row in range(col+1, len(mat)):
            factor = mat[row][col]

            multiplication_result = []
            for i in range(len(mat)+1):
                multiplication_result.append(str(mat[col][i] * factor))

            if(factor.numerator==0):
                continue

            print(f"R{col+1}'->({factor})*R{col+1} [{', '.join(multiplication_result)}]")
            print(f"R{row+1} ==> R{row+1}-R{col+1}'")
            
            for j in range(col, len(mat)+1):
                mat[row][j] += mat[col][j] * Fraction(-factor.numerator, factor.denominator)
            
            printed_mat = []
            for r in mat:
                printed_row = []
                for elem in r:
                    printed_row.append(str(elem))
                printed_mat.append(printed_row)
            printMat(printed_mat)

    return mat

def back_substitution(mat):

    n = len(mat)
    solutions = [None] * n

    for i in range(n - 1, -1, -1):
        rhs = mat[i][-1]
        for j in range(i + 1, n):
            rhs += Fraction(-mat[i][j].numerator, mat[i][j].denominator) * solutions[j]
        solutions[i] = rhs

    return solutions


filename = input("Enter filename: ")
mat = readMat(filename)
    
mat_num = []
for row in mat:
    sub_row = []
    for ele in row:
        sub_row.append(Fraction(int(ele), 1))
    mat_num.append(sub_row)
    
print("Augmented Matrix:")
printMat(mat)
    
ans = gaussian_elimination(mat_num)
    
print("Result from Gaussian Elimination:")

result = []

for row in ans:
    sub_row = []
    for ele in row:
        sub_row.append(str(ele))
    result.append(sub_row)

printMat(result)
    
print("After Back-Substitution:")
sols = back_substitution(ans)
    
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for idx in range(len(sols)):
    print(f"{letters[idx]} = {sols[idx]}")
