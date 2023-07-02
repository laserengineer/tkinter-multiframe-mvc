class HA:
    def __init__(self, name):
        self.name = name + "_HA"

    def launch(self):
        print(f"{self.name} is launched")

    def __str__(self):
        return f"HA({self.name})"

if __name__ == "__main__":
    app = HA("HA")
    app.launch()
