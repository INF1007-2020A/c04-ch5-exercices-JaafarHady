#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:

    if number > 0 :
        pass
    else:
        number = number*(-1)

    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'

    word_list = []

    for pre in prefixes :
        word_list.append(pre+suffixe)
    return word_list


def prime_integer_summation() -> int:
    prime = [2, 3, 5]
    number = 6
    while len(prime)<100 :
        premier = True
        for i in range(2, number-1) :
            if number%i == 0 :
                premier = False
                number += 1
                break
        if premier :
            prime.append(number)
            number += 1
    return sum(prime)


def factorial(number: int) -> int:
    factorielle = 1
    for i in range(0,number-1) :
        factorielle *= (number-i)
    return factorielle


def use_continue() -> None:
    for i in range(1,10) :
        if i == 5 :
            continue
        else:
            print(i)




def verify_ages(groups: List[List[int]]) -> List[bool]:
    acceptable = []
    for i in range(len(groups)) :
        if len(groups[i]) <= 2 :
            acceptable.append(False)
        elif len(groups[i]) > 9 :
            acceptable.append(False)
        else:
            for age in groups[i] :
                if age == 25 :
                    acceptable.append(True)
                    break
                elif age < 18 :
                    acceptable.append(False)
                    break
                elif age == 50 :
                    for age in groups[i] :
                        if age > 70 :
                            acceptable.append(False)
                    break
                elif age > 70 :
                    for age in groups[i] :
                        if age == 50 :
                            acceptable.append(False)
                    break
                else :
                    acceptable.append(True)
                    break







    return [acceptable]


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
