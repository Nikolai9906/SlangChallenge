from sys import stdin
from collections import Counter

def calculatNGrams(string,number):
    """
    Function that is in charge of calculating n-grams of the word with the number of separations received
    Receives:
        string: piece of text
        number: number of separations
    """
    lenString = len(string)
    nGrams = []
    for i in range(lenString-number+1):
        nGrams.append(string[i:number+i])
    nGrams = nGrams[:-1]
    return nGrams

def mostFrequentNGram(string,number):
    """
    Function that is in charge of calculating most frequent n-gram of the word with the number of separations received
    Receives:
        string: piece of text
        number: number of separations
    """
    nGrams = (calculatNGrams(string,number))
    dic = {}
    result = []
    for i in range(len(nGrams)):
        dic[nGrams[i]] = nGrams.count(nGrams[i])

    for key in dic:
        if(dic[key] == number):
            result.append(key)
        elif(dic[key] == number - 1):
            result.append(key)

    return result[0]
        
    
    

def main():
    """
    Main function which calls the calculatNGrams() function sending two parameters separated by commas
    Send:
        string: piece of text
        number: number of separations
    """
    print("Write the word and after it a number separated by a comma. \n Ex: text,2")
    string,number = stdin.readline().strip(" ").split(",")
    print("\nCalculate n-grams result: \n" + str(calculatNGrams(string,int(number)))+"\n")
    print("Calculate most frequent n-gram result: \n" + str(mostFrequentNGram(string,int(number))))

main()


    
    
    


