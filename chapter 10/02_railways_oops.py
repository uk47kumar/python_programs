class Railwayform:
    formType = "Railwayform"

    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")


ujjwalsApplication = Railwayform()
ujjwalsApplication.name = "ujjwal"
ujjwalsApplication.train = "Rajdhani Express"
ujjwalsApplication.printData()
