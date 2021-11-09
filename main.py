def convert_number_to_english(number):
    numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
               6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
               11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
               15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
               19: 'nineteen', 20: 'twenty',
               30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
               70: 'seventy', 80: 'eighty', 90: 'ninety'}

    kilo = 1000
    million = 1000000
    billion = 1000000000

    if number < 0:
        return 'Number less than zero'

    if number <= 20:
        return numbers[number]

    if number < 100:
        if number % 10 == 0:
            return numbers[number]
        else:
            return numbers[(number // 10) * 10] + ' ' + numbers[number % 10]

    if number < kilo:
        if number % 100 == 0:
            return numbers[number // 100] + ' hundred'
        else:
            return numbers[number // 100] + ' hundred ' + convert_number_to_english(number % 100)

    if number < million:
        if number % kilo == 0:
            return convert_number_to_english(number // kilo) + ' thousand '
        else:
            return convert_number_to_english(number // kilo) + ' thousand ' + convert_number_to_english(number % kilo)

    if number < billion:
        if number % million == 0:
            return convert_number_to_english(number // million) + ' million'
        else:
            return convert_number_to_english(number // million) + ' million ' + \
                   convert_number_to_english(number % million)

    return 'Number is too large!!!'


def convert_number_to_persian(number):
    numbers = {0: 'صفر', 1: 'یک', 2: 'دو', 3: 'سه', 4: 'چهار', 5: 'پنج',
               6: 'شش', 7: 'هفت', 8: 'هشت', 9: 'نه', 10: 'ده',
               11: 'یازده', 12: 'دوازده', 13: 'سیزده', 14: 'چهارده',
               15: 'پانزده', 16: 'شانزده', 17: 'هفده', 18: 'هیجده',
               19: 'نوزده', 20: 'بیست',
               30: 'سی', 40: 'چهل', 50: 'پنجاه', 60: 'شصت',
               70: 'هفتاد', 80: 'هشتاد', 90: 'نود',
               100: 'یکصد', 200: 'دویست', 300: 'سیصد', 400: 'چهارصد', 500: 'پانصد', 600: 'ششصد', 700: 'هفتصد',
               800: 'هشتصد', 900: 'نهصد'}

    kilo = 1000
    million = 1000000
    billion = 1000000000

    if number < 0:
        return 'Number less than zero'

    if number <= 20:
        return numbers[number]

    if number < 100:
        if number % 10 == 0:
            return numbers[number]
        else:
            return numbers[(number // 10) * 10] + ' ' + numbers[number % 10]

    if number < kilo:
        if number % 100 == 0:
            return numbers[number]
        else:
            return numbers[(number // 100) * 100] + ' ' + convert_number_to_persian(number % 100)

    if number < million:
        if number % kilo == 0:
            return convert_number_to_persian(number // kilo) + ' هزار'
        else:
            return convert_number_to_persian(number // kilo) + ' هزار ' + convert_number_to_persian(number % kilo)

    if number < billion:
        if number % million == 0:
            return convert_number_to_persian(number // million) + ' میلیون'
        else:
            return convert_number_to_persian(number // million) + ' میلیون ' + \
                   convert_number_to_persian(number % million)

