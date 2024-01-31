def main():
    print("This Program converts USD to Pounds Sterling")
    print()


    dollars= eval(input("Enter The amount of Dollars: "))

    pounds= convert_to_pounds(dollars)

    print("That is ",pounds, "pounds.")

convert_to_pounds= lambda dollars: dollars*0.82

main()