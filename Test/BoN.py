class BoN:
    def __init__(self, name):
        self.name = name + "_BoN"

    def launch(self):
        print(f"{self.name} is launched")

    def __str__(self):
        return f"BoN({self.name})"

if __name__ == "__main__":
    app = BoN("BoN")
    app.launch()
