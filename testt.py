import rutpy


def validate(rut: str) -> bool:
 return rutpy.validate(rut)

if __name__ == "__main__":
    rut= "11111111-1"
    print(validate(rut))