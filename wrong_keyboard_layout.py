def change_letters(input_text=None):
    if input_text is None:
        return False

    text = input_text.replace(" ", "")
    text = [str(x) for x in text]
    eng = "qwertyuiop" + "asdfghjkl" + "zxcvbnm" + "QWERTYUIOP" + "ASDFGHJKL" + "ZXCVBNM" + r"""`[];',.""" + r"""~{}:"<>""" + "/?"
    rus = "йцукенгшщз" + "фывапролд" + "ячсмить" + "ЙЦУКЕНГШЩЗ" + "ФЫВАПРОЛД" + "ЯЧСМИТЬ" + "ёхъжэбю"      + "ЁХЪЖЭБЮ"      + ".,"    
    count_rus = count_eng = 0
    for x in input_text:
        if x in eng:
            count_eng += 1
        elif x in rus:
            count_rus += 1
    
    text_is_rus = True if count_rus > count_eng else False
    output_text = ""
    
    # convert rus to eng
    if text_is_rus:
        for idx, letter in enumerate(input_text):
            index_correct_letter = rus.find(letter)
            if index_correct_letter != -1:
                output_text += eng[index_correct_letter]
            else:
                output_text += input_text[idx]
    
    # convert eng to rus
    else:
        for idx, letter in enumerate(input_text):
            index_correct_letter = eng.find(letter)
            if index_correct_letter != -1:
                output_text += rus[index_correct_letter]
            else:
                output_text += input_text[idx]
    
    return output_text


if __name__ == "__main__":        
    s = "Ghbdtn? Vbh/"  # eng
    print(f"inp: {s}\nout: {change_letters(s)}\n")
    
    s = "Руддщб Цщкдвю"  # rus
    print(f"inp: {s}\nout: {change_letters(s)}\n")

    s = "Gрbвtт? Vиh/"  # both
    print(f"inp: {s}\nout: {change_letters(s)}")

