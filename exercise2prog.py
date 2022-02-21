import exercise2class as e


def main():

    manufact1 = "Samsung"
    model1 = "Galaxy"
    price1 = 500

    phones = e.Phone(manufact1, model1, price1)

    print("Phone manufacturer is: ", phones.get_manufact())
    print("Phone model is: ", phones.get_model())
    print("Phone price is: $", phones.get_retail_price(), sep="")

    phones.set_model("iPhone")
    phones.set_manufact("Apple")
    phones.set_retail_price(1000)
    print("The phone's new manufacturer is", phones.get_manufact())
    print("The phone's new model is", phones.get_model())
    print("The phone's new price is: $", phones.get_retail_price(), sep="")


main()
