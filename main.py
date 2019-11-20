import onp_translation
import textpika
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--pikatchu", action='store_true')
parser.add_argument("-l", "--lines", action='store_true')
lili = parser.parse_args().lines
piki = parser.parse_args().pikatchu

def show_image(message):
    a = open("error_art.txt", 'r', encoding="utf-8").read()
    a = f"\033[1;31m  {message[:-5].upper()}  {a}\033[0m"
    return a

def print_whole_list_of_lists(li):
    for i in li:
        print(f"\033[33;1m{i}\033[0m")

def read_data(li = []): # def read_data(list_temp):
    while (True):
        try:
            # if list_temp == []:
            print("\033[36;1m> \033[0m", end="", sep="")
            list_temp = input("\033[1m").split()
            # if listtemp[0] in ("exit", "quit"):
                # textpika.goodbye(language)
                # break
            list_temp = onp_translation.to_onp(list_temp)

            if lili == False: print(f"\033[33;1m{list_temp}\033[0m")
            else: li.append(list_temp)

        except EOFError:
            print("\033[0m")
            if lili == True: return li
            break

        except KeyboardInterrupt:
            print("\033[0m\n")
            if lili == True: return li
            break
        except (ValueError, IndexError) as Error:
            print("\033[0m", end="")
            print(show_image(sys.exc_info()[0].__name__), end="")
            # print(show_image(type(Error).__name__))

def main():
    #print(piki)

    # reading everything and then printing
    # lists = read_whole_list_of_lists()
    # lists_changed = onp_translation.to_onp(lists)
    # print_whole_list_of_lists(lists_changed)

    ## reding each line separetly
    read_data()
    if lili == True: print_whole_list_of_lists(read_data())

if __name__ == "__main__":
    main()
