# -*- coding: utf-8 -*-
# __str = "https://www.liepin.com/company/010-000/"

# print(str[0:-4])
# print(str(1))

# urls = ["010", "020","030","040","050","060","070","999"]
# for i, j in zip(urls, range(0, 8)):
#     print(i+urls[j])

# for i, j in zip(range(10, 510, 10), range(1, 10)):
#     print(i)
#     print(j)
# if len(str(i)) == 2:
#     print("0" + str(i))
# else:
#     print(str(i))

pagenumstr = "共100页"
page_num = pagenumstr[1:-1]
print((int(page_num)))
