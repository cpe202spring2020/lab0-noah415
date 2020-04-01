def weight_on_planets():
   initWeight = int(input('What do you weigh on earth? '))
   marsWeight = initWeight * .38
   jupiterWeight = initWeight * 2.34

   print('\nOn Mars you would weigh %4.2f pounds.' %(marsWeight))
   print('On Jupiter you would weigh %4.2f pounds.' %(jupiterWeight))



if __name__ == '__main__':
   weight_on_planets()
