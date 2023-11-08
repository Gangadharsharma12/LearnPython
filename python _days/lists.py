# list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
#
# l1 = [x for row in list_of_lists for number in row for x in number]
# print(l1)
#
#
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# for each in countries:
#     print([{"country":each[0][0].upper(), "city": each[0][1].upper()}])



# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# l = [[i[0][0], i[0][0][0:3], i[0][1].upper()] for i in countries]
# print(l)



# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# l = [i for i in numbers if i <= 0]
# print(l)


# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# l = [i[0][0] + " " + i[0][1] for i in names]
# print(l)

