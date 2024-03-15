from . import dictionary
from .models import PersianWord, EnglishWord
from . import serializers

def abjad_clalc_FA(word):
    kabir_letters = []
    list_kabir_number = []
    kabir_number = 0

    saghit_letters = []
    list_saghit_number = []
    saghit_number = 0

    vasit_letters = []
    list_vasit_number = []
    vasit_number = 0
    
    for i in word.replace(' ', ''):
        kabir_letters.append(i)
        saghit_letters.append(i)
        vasit_letters.append(i)

        list_kabir_number.append(dictionary.kabir_abjad[i])
        list_saghit_number.append(dictionary.saghir_abjad[i])
        list_vasit_number.append(dictionary.vasit_abjad[i])

        kabir_number += dictionary.kabir_abjad[i]
        saghit_number += dictionary.saghir_abjad[i]
        vasit_number += dictionary.vasit_abjad[i]

    box_data = {
        'kabir': {'word': word, 'kabir_number': kabir_number, 'letters': kabir_letters, 'list_kabir_number': list_kabir_number},
        'saghit': {'word': word, 'saghit_number': saghit_number, 'letters': saghit_letters, 'list_saghit_number': list_saghit_number},
        'vasit': {'word': word, 'vasit_number': vasit_number, 'letters': vasit_letters, 'list_vasit_number': list_vasit_number},
    }


    obj, create = PersianWord.objects.get_or_create(
        word=word.strip(), kabir_abjad=kabir_number, saghir_abjad=saghit_number, vasit_abjad=vasit_number)

    obj.search += 1
    obj.save()

    objects = PersianWord.objects.filter(kabir_abjad=obj.kabir_abjad)
    table_data = serializers.PersianWordSerilaizer(objects, many=True).data

    return {'box_data': box_data, 'table_data': table_data}


def abjad_clalc_EN(word):
    hebrew_letters = []
    list_hebrew_numbers = []
    hebrew_number = 0

    english_letters = []
    list_english_numbers = []
    english_number = 0

    simple_letters = []
    list_simple_numbers = []
    simple_number = 0
    
    for i in word.replace(' ', ''):
        hebrew_letters.append(i)
        english_letters.append(i)
        simple_letters.append(i)

        list_hebrew_numbers.append(dictionary.abjad_hebrew[i])
        list_english_numbers.append(dictionary.abjad_english[i])
        list_simple_numbers.append(dictionary.abjad_simple[i])

        hebrew_number += dictionary.abjad_hebrew[i]
        english_number += dictionary.abjad_english[i]
        simple_number += dictionary.abjad_simple[i]

    box_data = {
        'hebrew': {'word': word, 'hebrew_number': hebrew_number, 'letters': hebrew_letters, 'list_hebrew_numbers': list_hebrew_numbers},
        'english': {'word': word, 'english_number': english_number, 'letters': english_letters, 'list_english_numbers': list_english_numbers},
        'simple': {'word': word, 'simple_number': simple_number, 'letters': simple_letters, 'list_simple_numbers': list_simple_numbers},
    }


    obj, create = EnglishWord.objects.get_or_create(
        word=word.strip(), abjad_hebrew=hebrew_number, abjad_english=english_number, abjad_simple=simple_number)

    obj.search += 1
    obj.save()

    objects = EnglishWord.objects.filter(abjad_hebrew=obj.abjad_hebrew)
    table_data = serializers.EnglishWordSerilaizer(objects, many=True).data

    return {'box_data': box_data, 'table_data': table_data}

