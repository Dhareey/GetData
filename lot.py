def realLots(lot):
    if lot[-1]== '.':
        lot = lot.rstrip('.')
    asd = lot.split('-')
    realLot= ''
    if len(asd) == 3:
        numb = 4- len(asd[0])
        numb2 = 1-len(asd[1])
        numb3 = 5- len(asd[2])
        realLot+= ((numb*'0')+asd[0]+(numb2*'0')+asd[1]+(numb3*'0')+asd[2]+'000000')
    elif len(asd) == 4:
        numb = 4- len(asd[0])
        numb2 = 1-len(asd[1])
        numb3 = 5- len(asd[2])
        numb4 = 4- len(asd[3])
        realLot+= ((numb*'0')+asd[0]+(numb2*'0')+asd[1]+(numb3*'0')+asd[2]+(numb4*'0')+asd[3]+'00')
    elif len(asd) == 5:
        numb = 4- len(asd[0])
        numb2 = 1-len(asd[1])
        numb3 = 5- len(asd[2])
        numb4 = 4- len(asd[3])
        numb5 = 2-len(asd[4])
        realLot+= ((numb*'0')+asd[0]+(numb2*'0')+asd[1]+(numb3*'0')+asd[2]+(numb4*'0')+asd[3]+(numb5*'0')+asd[4])
    elif len(asd) == 2:
        numb = 4- len(asd[0])
        numb2 = 1-len(asd[1])
        realLot+= ((numb*'0')+asd[0]+(numb2*'0')+asd[1]+'00000000000')
    else:
        numb = 4- len(asd[0])
        realLot+= ((numb*'0')+asd[0]+'000000000000')
    return realLot