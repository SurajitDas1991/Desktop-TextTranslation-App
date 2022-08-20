import PySimpleGUI as sg

from googletranslate import TranslateWithGoogle
from ktraintranslate import TranslateWithKTrain
#sg.ChangeLookAndFeel('Dark')

#sg.ChangeLookAndFeel('DarkTanBlue')

sg.theme('Dark')
sg.set_options(element_padding=(0, 0))


dict_of_libs={0:'Google',1:'TextBlob'}
dict_of_langs={"zh":"Chinese","ar":"Arabic","ru":"Russian","de":"German","af":"Afrikaans","fr":"French","es":"Spanish","it":"Italian","pt":"Portugese"}

def main():
    # Define the window's contents
    core_layout = [[sg.Text("Choose a library to use",size=(40,1)),sg.Push()],
              [sg.Radio('Google Translate', "RADIO1", default=True,enable_events=True,k="-google-"),
                sg.Radio('Ktrain', "RADIO1",enable_events=True,k="-tb-"),sg.Push()],
                [sg.Combo(list(dict_of_langs.values()),enable_events=True, size=(12,20), key='-LANG-',expand_x=True, expand_y=True,default_value="Spanish",readonly=True)],
                [sg.Text("Enter the text to translate")],
                [sg.Multiline(size=(45,5), expand_x=True, expand_y=True, k='-MLINE-',autoscroll=True)],
                [sg.Button('Translate',k='-translate-',button_color=('white', 'firebrick3'),pad=(10,5))],
                [sg.Multiline(size=(45,5), expand_x=True, expand_y=True, k='-TLINE-',autoscroll=True)],
                [sg.ProgressBar(max_value=100, size=(100, 20), key='bar', metadata=5)],
                [sg.Button('Ok',button_color=('white', 'springgreen4'),pad=(15,15)),
                 sg.Button('Quit',button_color=('white', 'black'),pad=(15,15))]]

    layout = [[sg.Text('Translate to English',font='bold')],

          [sg.Frame('', [[sg.VPush()]]  + core_layout + [[sg.VPush()]], size=(500, 400), border_width=1, element_justification='c')]]

    # Create the window
    window = sg.Window('Language Translation App', layout, resizable=True,grab_anywhere=True,keep_on_top=True,finalize=True)




    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()


        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        elif event=='-translate-':
            window['-TLINE-'].update("")
            radio_value_google =window['-google-'].get()
            radio_value_textblob =window['-tb-'].get()
            if radio_value_google==True:
                tp_translate_text=window['-MLINE-'].get()
                translated_text=translate_based_on_selection(tp_translate_text,0,'')
                #print(type(translated_text))
                window['-TLINE-'].update(translated_text.text)
                window.refresh()
            if radio_value_textblob==True:
                tp_translate_text=window['-MLINE-'].get()
                source_lang=get_key(window['-LANG-'].get())
                window['-TLINE-'].update("Translating....")
                window['bar'].Widget['value'] += step
                translated_text=window.perform_long_operation(lambda:translate_based_on_selection(tp_translate_text,1,str(source_lang)),'-END KEY-')
                #window['-TLINE-'].update(translated_text)
                #window.refresh()
            #
        elif event=='-google-':
            pass
        elif event == '-END KEY-':
            return_value = values[event]
            window['-TLINE-'].update(f"{return_value}")

        # Output a message to the window
        # window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

    # Finish up by removing from the screen
    window.close()


def translate_based_on_selection(text_to_translate:str,selection:int,src_lang:str):
        if selection==0:
            translate_with_google=TranslateWithGoogle()
            return translate_with_google.translate_text(text_to_translate)
        elif selection==1:
           translate_with_ktrain=TranslateWithKTrain()
           return translate_with_ktrain.translate_text_ktrain(text_to_translate,src_lang)


def get_key(val):
    for key, value in dict_of_langs.items():
        if val == value:
            return key

    return "key doesn't exist"

if __name__=="__main__":
    main()
