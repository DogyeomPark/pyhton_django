# id와 pw를 모두 만족시켰을때 문구가 나오는 어플리케이션 만들기

id = 'egoing'
pw = '135'

while True:
    input_id = input('id: ')
    input_pw = input('pw: ')
    if input_id == id and input_pw == pw:
        print('Now you are ready to go!')
        break
    elif input_id != id and input_pw == pw:
        print('id or pw is wrong')
    elif input_id == id and input_pw != pw:
        print('id or pw is wrong')
    elif input_id != id and input_pw != pw:
        print('id or pw is wrong')

print('ok')
# input_id = input('id: ')
# id = 'egoing'
# input_pw = input('pw: ')
# pw = '135'
#
#
# while id =
#
# if input_id == id:
#     print('id is same')
#     input_pw
#     if input_pw == pw:
#         print('pw is same Now you can access')
#     else:
#         print('wrong pw')
#         print('input the pw: ', input_pw)
# else:
