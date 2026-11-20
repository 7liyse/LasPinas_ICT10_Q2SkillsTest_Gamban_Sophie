import pyscript  # type: ignore
from pyscript import document  # type: ignore

non_metals = {
    "Hydrogen": {"symbol": "H", "number": 1, "mass": "1.008"},
    "Carbon": {"symbol": "C", "number": 6, "mass": "12.011"},
    "Nitrogen": {"symbol": "N", "number": 7, "mass": "14.007"},
    "Oxygen": {"symbol": "O", "number": 8, "mass": "16.00"},
    "Phosphorus": {"symbol": "P", "number": 15, "mass": "30.974"},
    "Sulfur": {"symbol": "S", "number": 16, "mass": "32.06"},
    "Sulphur": {"symbol": "S", "number": 16, "mass": "32.06"},
    "Silicon": {"symbol": "Si", "number": 14, "mass": "28.085"},
    "Boron": {"symbol": "B", "number": 5, "mass": "10.811"},
    "Neon": {"symbol": "Ne", "number": 10, "mass": "20.1797"},
    "Krypton": {"symbol": "Kr", "number": 36, "mass": "83.798"},
    "Chlorine": {"symbol": "Cl", "number": 17, "mass": "35.45"},
    "Bromine": {"symbol": "Br", "number": 35, "mass": "79.904"},
    "Iodine": {"symbol": "I", "number": 53, "mass": "126.904"},
    "Selenium": {"symbol": "Se", "number": 34, "mass": "78.971"},
    "Fluorine": {"symbol": "F", "number": 9, "mass": "18.998"},
    "Tellurium": {"symbol": "Te", "number": 52, "mass": "127.60"},
    "Helium": {"symbol": "He", "number": 2, "mass": "4.003"},
}


def find_element(e):
    output_el = document.getElementById("output")
    input_el = document.getElementById("non_metal")

    if not output_el:
        return

    if not input_el or not hasattr(input_el, "value"):
        output_el.innerHTML = "<b>Error:</b> Input field not found."
        return

    element_name = str(input_el.value).strip().title()
    if not element_name:
        output_el.innerHTML = "Please enter a non-metal element name."
        return

    info = non_metals.get(element_name)

    if not info:
        output_el.innerHTML = f"<b>{element_name}</b> is not in the non-metals list."
        return

    output_el.innerHTML = f"""
    <b>Symbol:</b> {info["symbol"]} <br>
    <b>Element:</b> {element_name} <br>
    <b>Atomic Number:</b> {info["number"]} <br>
    <b>Atomic Mass:</b> {info["mass"]}
    """