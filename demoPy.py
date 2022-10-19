import random
import splice_generator
import post6
import scaley
import midiutil
import shutil
from random import randrange
import os


def getOctaveHumanized(variability):
    if variability == '':
        variability = "Standard"
    if variability.lower().capitalize() == "Standard":
        from random import randrange
        if randrange(0, 12, 1) < 9:
            return "0"
        else:
            return str(randrange(0, 2, 1))
    if variability.lower().capitalize() == "High":
        from random import randrange
        if randrange(0, 12, 1) < 7:
            return "0"
        else:
            return str(randrange(0, 3, 1))
    if variability.lower().capitalize() == "Low":
        from random import randrange
        if randrange(0, 12, 1) < 10:
            return "0"
        else:
            return str(randrange(0, 1, 1))


def getRandomMidiList():
    mel = post6.getStandardMelody("", "", "", "", post6.change_idea(), '', '').replace("Eighth", "0.125").replace("Quarter",
                                                                                                "0.25").replace("Whole",
                                                                                                                "1.0").replace(
        "Dotted Whole", "1.5").replace("Dotted Half", "0.75").replace("Half", "0.5")

    for key in scaley.all_chords:
        if key in mel:
            mel = mel.replace(key, str(scaley.all_chords[key]))
    mel1 = mel
    mel2sub = mel1.split("First Measure Interpreted: ")[0]
    mel1 = mel1.replace(str(mel2sub), "").replace(" Note", "")
    mel1 = mel1.split("Remaining Chords")[0].replace("First Measure Interpreted: ", "")
    midi = []
    second_measure_midi_sample = ''
    third_measure_sample = ''
    fourth_measure_sample = ''
    fifth_measure_sample = ''
    sixth_measure_sample = ''
    seventh_measure_sample = ''
    eighth_measure_sample = ''
    first_measure_midi_sample = mel1
    if "Second Time Signature" in mel:
        mel2sub = mel.split("Second Measure Actions: ")[0]
        second_measure_midi_sample = mel.replace(mel2sub, "").replace(" Note", "")
        if "Third Measure" in mel:
            second_measure_midi_sample = second_measure_midi_sample.split("Third Measure Chords")[0].replace(
                "Second Measure Actions: ", "")
        else:
            second_measure_midi_sample = second_measure_midi_sample.split("Second Measure Actions: ")[1]
        first_measure_midi_sample = mel1
        midi = first_measure_midi_sample + second_measure_midi_sample
    if "Third Time Signature" in mel:
        mel2sub = mel.split("Third Measure Actions: ")[0]
        third_ms = mel.replace(mel2sub, "").replace(" Note", "")
        if "Fourth Measure" in mel:
            third_ms = third_ms.split("Fourth Measure Chords")[0].replace("Third Measure Actions: ", "")
        else:
            third_ms = third_ms.split("Third Measure Actions: ")[1]
        third_measure_sample = third_ms.replace(" Note", "")
        midi = first_measure_midi_sample + second_measure_midi_sample + third_measure_sample
    if "Fourth Time Signature" in mel:
        mel2sub = mel.split("Fourth Measure Actions: ")[0]
        fourth_ms = mel.replace(mel2sub, "").replace(" Note", "")
        if "Fifth Measure" in mel:
            fourth_ms = fourth_ms.split("Fifth Measure Chords")[0].replace("Fourth Measure Actions: ", "")
        else:
            fourth_ms = fourth_ms.split("Fourth Measure Actions: ")[1]
        fourth_measure_sample = fourth_ms
        midi = first_measure_midi_sample + second_measure_midi_sample + third_measure_sample + fourth_measure_sample
    if "5th Time Signature" in mel:
        mel2sub = mel.split("5th Measure Actions: ")[0]
        fifth_ms = mel.replace(mel2sub, "").replace(" Note", "")
        if "6th Measure" in mel:
            fifth_ms = fifth_ms.split("6th Measure Chords")[0].replace("5th Measure Actions: ", "")
        else:
            fifth_ms = fifth_ms.split("5th Measure Actions: ")[1]
        fifth_measure_sample = fifth_ms
        midi = first_measure_midi_sample + second_measure_midi_sample + third_measure_sample + fourth_measure_sample + fifth_measure_sample
    if "6th Time Signature" in mel:
        mel2sub = mel.split("6th Measure Actions: ")[0]
        sixth_ms = mel.replace(mel2sub, "").replace(" Note", "")
        if "7th Measure" in mel:
            sixth_ms = sixth_ms.split("7th Measure Chords")[0].replace("6th Measure Actions: ", "")
        else:
            if len(sixth_ms.split("6th Measure Actions: ")) > 1:
                sixth_ms = sixth_ms.split("6th Measure Actions: ")[1]
            else:
                pass
        sixth_measure_sample = sixth_ms
        midi = first_measure_midi_sample + second_measure_midi_sample + third_measure_sample + fourth_measure_sample + fifth_measure_sample + sixth_measure_sample
    if "7th Time Signature" in mel:
        mel2sub = mel.split("7th Measure Actions: ")[0]
        seventh_ms = mel.replace(mel2sub, "").replace(" Note", "")
        if "8th Measure" in mel:
            seventh_ms = seventh_ms.split("8th Measure Chords")[0].replace("7th Measure Actions: ", "")
        else:
            if len(seventh_ms.split("7th Measure Actions: ")) > 1:
                seventh_ms = seventh_ms.split("7th Measure Actions: ")[1]
        seventh_measure_sample = seventh_ms
        midi = first_measure_midi_sample + second_measure_midi_sample + third_measure_sample + fourth_measure_sample + fifth_measure_sample + sixth_measure_sample + seventh_measure_sample
    if "8th Time Signature" in mel:
        mel2sub = mel.split("8th Measure Actions: ")[0]
        eighth_ms = mel.replace(mel2sub, "").replace(" Note", "")
        if "9th Measure" in mel:
            eighth_ms = eighth_ms.split("9th Measure Chords")[0].replace("8th Measure Actions: ", "")
        else:
            if len(eighth_ms.split("8th Measure Actions: ")) > 1:
                eighth_ms = eighth_ms.split("8th Measure Actions: ")[1]
        eighth_measure_sample = eighth_ms
        midi = first_measure_midi_sample + second_measure_midi_sample + third_measure_sample + fourth_measure_sample + fifth_measure_sample + sixth_measure_sample + seventh_measure_sample + eighth_measure_sample
    if "9th Time Signature" in mel:
        mel2sub = mel.split("9th Measure Actions: ")[0]
        ninth_ms = mel.replace(mel2sub, "").replace(" Note", "")
        ninth_measure_sample = ninth_ms
        midi = first_measure_midi_sample + second_measure_midi_sample + third_measure_sample + fourth_measure_sample + fifth_measure_sample + sixth_measure_sample + seventh_measure_sample + eighth_measure_sample + ninth_measure_sample
    midi = midi.replace("Dotted 1.0", "1.5")
    tempo = mel.split("scale at ")[1]
    tempo = int(tempo.split("bpm")[0])
    return mel, midi, tempo


def protected_vip():
    MyMIDI = midiutil.MIDIFile(1)
    time = 0
    midi_list = getRandomMidiList()
    modern_english = str(midi_list[0])
    for key in scaley.all_chords:
        if str(scaley.all_chords[key]) in modern_english:
            modern_english = modern_english.replace(str(scaley.all_chords[key]), str(key))
    string_with_empty_lines = modern_english
    lines = string_with_empty_lines.split("\n")
    non_empty_lines = [line for line in lines if line.strip() != ""]
    string_without_empty_lines = ""
    for line in non_empty_lines:
        string_without_empty_lines += line + "\n"
    print(modern_english + "\n")
    scaler = modern_english.split("in ")[1].split(" scale")[0]
    tempo = int(modern_english.split("at ")[1].split("bpm")[0])
    for i in range(25):
        string_with_empty_lines = getRandomMidiList()[1].replace(" Chord", " ").replace("'0", "0").replace("] , ",
                                                                                                           "], ").replace(
            ', 2', ', 2\']')
        lines = string_with_empty_lines.split("\n")
        non_empty_lines = [line for line in lines if line.strip() != ""]
        string_without_empty_lines = ""
        for line in non_empty_lines:
            string_without_empty_lines += line + "\n"
        string_without_empty_lines = string_without_empty_lines.replace(" Note", "").replace(" Chord", "")

        for key in scaley.all_chords:
            if str(scaley.all_chords[key]) in string_without_empty_lines:
                string_without_empty_lines = string_without_empty_lines.replace(str(scaley.all_chords[key]), (
                    str(scaley.all_chords[key]).replace("'", "").strip("[").strip("]")).replace(",", "%"))
        string_without_empty_lines = string_without_empty_lines.replace("['", "").replace("']", "").replace("'", "")
        string_without_empty_lines = string_without_empty_lines.replace("B#", "32").replace("Db", "25").replace(
            "Eb",
            "27").replace(
            "Fb", "28").replace("Gb", "30").replace("Ab", "32").replace("Bb", "34").replace("Cb", "35").replace(
            "C#",
            "25").replace(
            "A#", "34").replace("D#", "27").replace("E#", "29").replace("B#", "36").replace("F#", "30").replace(
            "G#",
            "32").replace(
            "A", "33").replace("B", "35").replace("C", "24").replace("G", "31").replace("D", "26").replace("E",
                                                                                                           "28").replace(
            "F", "29")
        string_without_empty_lines = string_without_empty_lines
        package = string_without_empty_lines.replace("st0.1", "st 0.1").replace("t0.2", "t 0.2").replace("  ",
                                                                                                         " ").replace(
            "Rest", "3591")
        packages = package
        lines = packages.split("\n")
        non_empty_lines = [line for line in lines if line.strip() != ""]
        packages = non_empty_lines
        print(non_empty_lines)
        MyMIDI.addTempo(time, time, tempo)
        track = 0
        channel = 0
        clocks_per_tick = 24
        notes_per_quarter = 8
        duration = 0
        denominator = 4
        denominator1 = 4
        octavator = random.choice([24, 36, 36, 36, 36, 36, 36, 36, 48, 48, 56])
        chord_notes = []
        possible_note_lengths = ["0.125", "0.25", "0.5", "0.75", "1.0", "0.375", "0.625", "1.5", "1.75", "0.875"]
        for u in range(len(non_empty_lines)):
            volume = int(randrange(45, 90, 1))
            for j in range(len(scaley.time_signatures) - 1):
                if scaley.time_signatures[j] in non_empty_lines[u]:
                    numerator = int(scaley.time_signatures[j].split("/")[0])
                    denominator = int(scaley.time_signatures[j].split("/")[1])
                    if denominator == 2:
                        denominator1 = 2
                        denominator = 1
                    elif denominator == 4:
                        denominator1 = 4
                        denominator = 2
                    elif denominator == 8:
                        denominator1 = 8
                        denominator = 3
                    elif denominator == 16:
                        denominator1 = 16
                        denominator = 4
                    MyMIDI.addTimeSignature(track, time, numerator, denominator, clocks_per_tick, notes_per_quarter)
                    non_empty_lines[u] = non_empty_lines[u].replace(scaley.time_signatures[j], "")
            non_empty_lines1 = list(non_empty_lines[u].split(","))
            for z in range(len(non_empty_lines1) - 1):
                for t in range(len(possible_note_lengths) - 1):
                    if possible_note_lengths[t] in non_empty_lines1[z]:
                        duration = float(possible_note_lengths[t]) * float(denominator1)
                        tyler_hero = non_empty_lines1[z]
                        non_empty_lines1[z] = non_empty_lines1[z].replace(possible_note_lengths[t], "")
                if "%" in non_empty_lines1[z]:
                    chord_notes = non_empty_lines1[z].split("%")
                    for e in range(len(chord_notes)):
                        chord_notes[e] = chord_notes[e].replace("0.125 ", "")
                        chord_notes[e] = chord_notes[e].replace("0.25 ", "")
                        chord_notes[e] = chord_notes[e].replace("0.5 ", "")
                        chord_notes[e] = chord_notes[e].replace("0.75 ", "")
                        chord_notes[e] = chord_notes[e].replace("1.0 ", "")
                        chord_notes[e] = chord_notes[e].replace("0.625 ", "")
                        chord_notes[e] = chord_notes[e].replace("0.375 ", "")
                        chord_notes[e] = chord_notes[e].replace("1.5 ", "")
                        chord_notes[e] = chord_notes[e].replace("0.875", "")
                        chord_notes[e] = chord_notes[e].replace("1.25 ", "")
                        chord_notes[e] = chord_notes[e].replace(" ", "")
                        yy = randrange(5)
                        pitch = chord_notes[e]
                        if "#" in pitch:
                            pitch = pitch.replace("#", "")
                            pitch = str(int(pitch) + 1)
                        pitch = int(pitch) + octavator
                        volume = volume + int(randrange(-6, 6, 1))
                        time_mod = time
                        time_mod += float(randrange(9999999999)/2356)
                        time_mod += float(randrange(9999999999)/2356) * -1
                        if time_mod < 0:
                            time_mod = time
                        MyMIDI.addNote(track, channel, pitch, time_mod, duration, volume, annotation=None)
                    time = time + duration
                elif "3591" in non_empty_lines1[z]:
                    time = time + duration
                else:
                    non_empty_lines1[z] = non_empty_lines1[z].replace("  ", "")
                    non_empty_lines1[z] = non_empty_lines1[z].replace(" ", "")
                    pitch = non_empty_lines1[z]
                    if "#" in pitch:
                        pitch = pitch.replace("#", "")
                        pitch = str(int(pitch) + 1)
                    if pitch != '':
                        pitch = int(pitch) + octavator
                        volume = volume + int(randrange(-6, 6, 1))
                        MyMIDI.addNote(track, channel, pitch, time, duration, volume, annotation=None)
                        time = time + duration

    fantasy_names = ["Libra", "Cobra", "Astra", "Jada", "CoolTrain", "DeanList", "Oxford", "Pegasus", "Lioness",
                     "Birdz", "Cash", "Booming", "Astral", "Lines", "Genesis", "AlphaOmega", "Delta",
                     "Gamma", "Fly", "Float"]
    namer = "Grand Interpolation_" + scaler + "_" + str(tempo) + "BPM" + "_" + random.choice(fantasy_names) + " " + str(randrange(500)) + ".MIDI"
    with open(os.path.join('/Users/celeryman/Documents/MIDI LIBRARYAI/', namer), "wb") as output_file:
        MyMIDI.writeFile(output_file)
    with open(os.path.join('/Users/celeryman/Documents/MIDI LIBRARYAI/', namer.replace(".MIDI", ".txt")), "w") as text_file:
        text_file.write(modern_english)


fantasy_names = ["Libra", "Cobra", "Pegasus", "Astra", "Astra", "Jada", "Berkley", "Oxford", "Berkley", "Oxford", "Pegasus", "Lioness",
                 "Birdz", "Cash", "Booming", "Astral", "Galactic", "Genesis", "AlphaOmega", "Delta",
                "Fly", "Float"]


# noinspection PyBroadException
def bouncer():
    for i in range(24):
        try:
            protected_vip()
        except:
            pass
    for i in range(159):
        try:
            splice_generator.get_fragments_trove()
        except:
            pass


def melodical_gen():
    bouncer()
    base_directory = '/Users/celeryman/Documents/MIDI LIBRARYAI/'
    midirectory = '/Users/celeryman/Documents/MIDI LIBRARYAI/MIDI/'
    try:
        os.mkdir(midirectory)
    except:
        pass
    frag_directory = '/Users/celeryman/Documents/MIDI LIBRARYAI/MIDI/Fragments/'
    grand_directory = '/Users/celeryman/Documents/MIDI LIBRARYAI/MIDI/Grand Interpolations/'
    english_directory = '/Users/celeryman/Documents/MIDI LIBRARYAI/English/'
    os.mkdir(english_directory)
    for file_name in os.listdir('/Users/celeryman/Documents/MIDI LIBRARYAI/'):
        if file_name.endswith(".MIDI"):
            shutil.move(f"{'/Users/celeryman/Documents/MIDI LIBRARYAI/'}{file_name}", f"{midirectory}{file_name}")
        elif file_name.endswith(".txt"):
            shutil.move(f"{'/Users/celeryman/Documents/MIDI LIBRARYAI/'}{file_name}", f"{english_directory}{file_name}")
    os.mkdir(frag_directory)
    os.mkdir(grand_directory)
    coal_dict = {"2/2": "Two Two", "2/8": "Two Eight", "2/4": "Two Four", "3/2": "Three Two", "2/12": "Two Twelve",
                 "2/16": "Two Sixteen", "3/4": "Three Four", "3/8": "Three Eight", "3/12": "Three Twelve",
                 "3/16": "Three Sixteen", "4/2": "Four Two", "4/4": "Four Four", "4/8": "Four Eight",
                 "4/12": "Four Twelve", "4/16": "Four Sixteen", "5/2": "Five Two", "5/4": "Five Four",
                 "5/8": "Five Eight", "5/12": "Five Twelve", "5/16": "Five Sixteen", "6/2": "Six Two",
                 "6/4": "Six Four", "6/8": "Six Eight", "6/12": "Six Twelve", "6/16": "Six Sixteen",
                 "7/2": "Seven Two", "7/4": "Seven Four", "7/8": "Seven Eight", "7/12": "Seven Twelve",
                 "7/16": "Seven Sixteen"}
    for file_name in os.listdir("/Users/celeryman/Documents/MIDI LIBRARYAI/MIDI/"):
        if file_name != "Fragments":
            if file_name != "Grand Interpolations":
                if os.path.getsize(f"{'/Users/celeryman/Documents/MIDI LIBRARYAI/MIDI/'}{file_name}") < 1024:
                    shutil.move(f"{'/Users/celeryman/Documents/MIDI LIBRARYAI/MIDI/'}{file_name}", f"{frag_directory}{file_name}")
                elif os.path.getsize(f"{'/Users/celeryman/Documents/MIDI LIBRARYAI/MIDI/'}{file_name}") > 1023:
                    shutil.move(f"{'/Users/celeryman/Documents/MIDI LIBRARYAI/MIDI/'}{file_name}", f"{grand_directory}{file_name}")
    for file_name in os.listdir("/Users/celeryman/Documents/MIDI LIBRARYAI/MIDI/Fragments/"):
        for value in list(coal_dict.values()):
            if value in file_name:
                if os.path.exists(f"{frag_directory}{value}/") is False:
                    os.mkdir(f"{frag_directory}{value}/")
                shutil.move(f"{'/Users/celeryman/Documents/MIDI LIBRARYAI/MIDI/Fragments/'}{file_name}", f"{frag_directory}{value}/{file_name}")
    new_pack_directory = f"{'/Volumes/External/Packs/'}{random.choice(fantasy_names)}{str(randrange(1960, 3500, 10))} Melodical/"
    npd = new_pack_directory
    try:
        os.mkdir('/Volumes/External/Packs/')
    except:
        pass
    os.mkdir(new_pack_directory)
    shutil.move('/Users/celeryman/Documents/MIDI LIBRARYAI/English/', new_pack_directory)
    shutil.move('/Users/celeryman/Documents/MIDI LIBRARYAI/MIDI/', new_pack_directory)
    for value in list(coal_dict.values()):
        for file_name in os.listdir(new_pack_directory):
            if value in file_name:
                pass
            else:
                try:
                    os.remove(f"{new_pack_directory}{file_name}")
                except:
                    pass
    new_frag_directory = f"{npd}MIDI/Fragments/"
    for file_name in os.listdir(new_frag_directory):
        if file_name.endswith(".MIDI"):
            os.remove(f"{new_frag_directory}{file_name}")
