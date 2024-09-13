grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
print(students)
classroom_journal = {'Aaron':[5, 3, 3, 5, 4], 'Bilbo':[2, 2, 2, 3], 'Johnny':[4, 5, 5, 2], 'Khendrik':[4, 4, 3], 'Steve':[5, 5, 5, 4, 5]}
print(classroom_journal)
print(sum(classroom_journal['Aaron'])/len(classroom_journal['Aaron']))
print(sum(classroom_journal['Bilbo'])/len(classroom_journal['Bilbo']))
print(sum(classroom_journal['Johnny'])/len(classroom_journal['Johnny']))
print(sum(classroom_journal['Khendrik'])/len(classroom_journal['Khendrik']))
print(sum(classroom_journal['Steve'])/len(classroom_journal['Steve']))
classroom_journal = {'Aaron': sum(classroom_journal['Aaron'])/len(classroom_journal['Aaron']),
                     'Bilbo': sum(classroom_journal['Bilbo'])/len(classroom_journal['Bilbo']),
                     'Johnny': sum(classroom_journal['Johnny'])/len(classroom_journal['Johnny']),
                     'Khendrik': sum(classroom_journal['Khendrik'])/len(classroom_journal['Khendrik']),
                     'Steve': sum(classroom_journal['Steve'])/len(classroom_journal['Steve'])}
print(classroom_journal)
