class Katsuo(Nigiri):
    top = "カツオ"
    topping = "生姜とネギ"
    price = 100

    def show_attributes(self):
        super().show_attributes()
        print("topping: {}".format(self.tooping))

