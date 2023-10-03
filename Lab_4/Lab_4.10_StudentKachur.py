blocks = int(input("Write your number of blocks: ")) #Вводимо наявну кількість блоків
print("Your numbers of blocks : ",blocks) #Виводимо наявну кількість блоків
blocks_in_layer = 1 #Кількість блоків у шарі
height_of_pyramid = 0 #Висота піраміди
while blocks >=blocks_in_layer: #Умова побудови піраміди
    height_of_pyramid+=1 #Збальшення висоти на олин рівень
    blocks-=blocks_in_layer #Віднімаємо блоки для поточного шару (від усієї кількості)
    blocks_in_layer+=1 #Додаємо до кожного наступного шару один блок
print("The height of the pyramid: ",height_of_pyramid) #Виводимо можливу висоту нашої піраміди

