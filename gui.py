import functions
import PySimpleGUI as sg

label = sg.Text("Add a todo")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("Todo App...YEAH!!", layout=[[label], [input_box, add_button]])
window.read()
window.close()
