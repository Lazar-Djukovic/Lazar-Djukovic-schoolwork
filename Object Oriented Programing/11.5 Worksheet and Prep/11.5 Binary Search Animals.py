# Binary Search Animals
#recursive search


nameList = ["baboon","cheetah","elephant","giraffe","hippo","leopard","lion","mongoose","rhino","warthog"]

animal = "lion"

def search(pos):
    if nameList[pos] == animal:
        print("found the animal at position > " + str(pos))
        return(pos)
    else:
      search(pos + 1)
    if pos > len(nameList):
      return("not in list")

mysearch = search(0)
