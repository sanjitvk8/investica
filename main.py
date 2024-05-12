import arrr
from pyscript import document

def translate_english(event):
    input_text = document.querySelector('#english')
    english = input_text.value
    output_div = new_func()
    output_div.innerText = arrr.translate(english)

def new_func():
    output_div = document.querySelector('#output')
    return output_div