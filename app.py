import nextpy as xt
class ConvertState(xt.State):
        binary: str="" #holds the binary input
        decimal: str="0" #holds the converted decimal value as string

        def on_binary_change_value(self,value): #this function converts the valid binary input to decimal
                try:
                        self.decimal=str(int(value,2))
                except:
                        self.decimal="INVALID BINARY NUMBER"

def index():
        
        return xt.vstack(
            xt.text(
                "Binary to Decimal Calculator"
            ),
            xt.input(placeholder = "Enter Binary Number ",value= ConvertState.binary, on_change=lambda value: ConvertState.on_binary_change_value(value)),
            xt.text(f"Decimal value: {ConvertState.decimal}") #displays the ouput 
        )


app=xt.App()
app.add_page(index)
