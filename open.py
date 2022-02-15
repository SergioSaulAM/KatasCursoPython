#Kata 10

def main():
    try:
        open("/path/to/mars.jpg")
    except FileNotFoundError as err:
        print("Couldn't find the config.txt file!", err)

if __name__ == '__main__':
    main()