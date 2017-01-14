# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:


def clean_message(message):
    """
    (str) -> str
    Given a message, which is a string containing one line of text, return a
    copy of the message that contains only the given message's alphabetical
    character, which have been converted to uppercase.
    REQ: message should have a len(message) > 0
    REQ: the given message should not have multiple lines
    >>> clean_message("the 7th iteam is chocolate")
    'THETHITEAMISCHOCOLATE'
    >>> clean_message("$$$$     money   $$$$")
    'MONEY'
    >>> clean_message("It's BLUE!!!!!!! O.M!!")
    'ITSBLUEOM'
    >>> clean_message("94... !!!!  :)))>#&*")
    ''
    >>> clean_message("     ")
    ''
    >>> clean_message("HEY")
    'HEY'
    """
    # Create a place to store a cleaned message
    message_cleaned = ''

    # Loop through each character in the given message
    for character in message:
        # Check if the character is a alphabet
        if(character.isalpha()):
            # If the alpabet is not uppercase make it uppercase
            uppercase_character = character.upper()
            # Add the uppercase letter to the clean message string
            message_cleaned += uppercase_character

    # Return the cleaned message
    return message_cleaned


def encrypt_letter(character, keystream):
    """
    (str, int) -> str
    Given a single uppercase character and a keystream will apply the keystream
    to the letter by adding the number value of the letter(which is 1 to 26)
    with the keystream modulus 26 then returns the resulted of the encrypted
    character.
    REQ: The given string must be a single character, which is a captial
    alphabet between the ASCII value of 65 to 90, including 65, and 90.
    REQ: keystream should be an integer between 1 to 26, including 1 and 26
    >>> encrypt_letter('A', 5)
    'F'
    >>> encrypt_letter('T', 25)
    'S'
    >>> encrypt_letter('C', 18)
    'U'
    >>> encrypt_letter('J', 26)
    'J'
    >>> encrypt_letter('Z', 4)
    'D'
    """
    # Get the numebr value of the letter, which is between 1 to 26, including
    # 1 and 26
    number_value_of_letter = ord(character.upper()) - 65
    # Apply the keystream to the given charater
    applied_keystream = (number_value_of_letter + keystream) % 26
    # Get the encrypted result of the character
    encrypted_character = chr(applied_keystream + 65)
    # Return the encrypted character
    return encrypted_character


def decrypt_letter(character, keystream):
    """
    (str, int) -> str
    Given a single uppercase character and a keystream will apply the keystream
    to the letter by subtracting the number value of the letter
    (which is 1 to 26) with the keystream (considering modulus 26) then returns
    the resulted of the decrypthed character.
    REQ:The given string must be a single character, which is a captial
    alphabet between the ASCII value of 65 to 90, including 65, and 90.
    REQ: keystream should be a single letter between 1 to 26, including 1 and
    26
    >>> decrypt_letter('F', 5)
    'A'
    >>> decrypt_letter('S', 25)
    'T'
    >>> decrypt_letter('U', 18)
    'C'
    >>> decrypt_letter('J', 26)
    'J'
    >>> decrypt_letter('D', 4)
    'Z'
    """
    # Get the numebr value of the letter, which is between 1 to 26, including
    # 1 and 26
    number_value_of_letter = ord(character.upper()) - 65
    # Apply the keystream to the given charater
    applied_keystream = (number_value_of_letter - keystream) % 26
    # Get the decrypted result of the character
    decrypted_character = chr(applied_keystream + 65)
    # Return the decrypted character
    return decrypted_character


def swap_cards(deck_of_cards, index_to_swap):
    """
    (list of int, int) -> NoneType
    Given a deck of cards, which are integers, and a index within the deck,
    will preform a swap with the card at the index and the card that follows
    it. Note, the deck is treated circularly, so if the index is the last
    card(element of the list), will swap with the first card(first element
    of the list).
    REQ: -1 < index_to_swap < len(index_to_swap)
    REQ: deck_of_cards should not be empty and should have at least two cards
    >>> deck = [1, 2, 3]
    >>> swap_cards(deck, 1)
    >>> deck == [1, 3, 2]
    True
    >>> deck = [1, 2, 3]
    >>> swap_cards(deck, 0)
    >>> deck == [2, 1, 3]
    True
    >>> deck = [1, 2, 3,]
    >>> swap_cards(deck, 2)
    >>> deck == [3, 2, 1]
    True
    """
    # Get the lenght of the given list
    deck_length = len(deck_of_cards)
    # Find the index of the following, while treating the deck(list) circularly
    following_index = (index_to_swap + 1) % deck_length
    # Store the card to be swapped
    temp = deck_of_cards[index_to_swap]
    # Preforme swap
    # Place the following card in the position of the card to be swapped
    deck_of_cards[index_to_swap] = deck_of_cards[following_index]
    # Place the card to be swapped in original position of the following card
    deck_of_cards[following_index] = temp


def move_joker_1(deck_of_cards):
    """
    (list of int) -> NoneType
    Given a deck of cards, which are a list of integers, finds JOKER1 (27 card)
    and swap it with the card (element) that follows. Note, the deck is
    treated circularly, so if the first joker is the last card(last element of
    the list), will swap with the first card(first element of the list).
    REQ: deck should not be empty and should have at least two cards, where
    one card is the first Joker.
    REQ: can only be one first Joker.
    >>> deck = [1, 2, 3, 27]
    >>> move_joker_1(deck)
    >>> deck == [27, 2, 3, 1]
    True
    >>> deck = [1, 27, 2, 3]
    >>> move_joker_1(deck)
    >>> deck == [1, 2, 27, 3]
    True
    >>> deck = [27, 1, 2, 3]
    >>> move_joker_1(deck)
    >>> deck == [1, 27, 2, 3]
    True
    """
    # Find the index of the first Joker in the deck of cards(list)
    index_of_joker1 = deck_of_cards.index(JOKER1)
    # Preform a swap with the first Joker and the card following it
    swap_cards(deck_of_cards, index_of_joker1)


def move_joker_2(deck_of_cards):
    """
    (list of int) -> NoneType
    Given a deck of cards, which are a list of integers, finds JOKER2 (28 card)
    and swap it with the card that follows, then swap the second Joker again
    with the next card that follows. Note, the deck is treated circularly, so
    if the second joker is the last card(last element of the list), it will
    swap with the first card(first element of the list).
    REQ: deck should not be empty and should have at least two cards, where
    one card is the second Joker.
    REQ: can only be one seond Joker.
    >>> deck = [1, 2, 3, 27, 28]
    >>> move_joker_2(deck)
    >>> deck == [2, 28, 3, 27, 1]
    True
    >>> deck = [1, 27, 28, 2, 3]
    >>> move_joker_2(deck)
    >>> deck == [1, 27, 2, 3, 28]
    True
    >>> deck = [28, 27, 1, 2, 3]
    >>> move_joker_2(deck)
    >>> deck == [27, 1, 28, 2, 3]
    True
    """
    # Set the number of required of sorts
    number_of_swaps = 2

    # Preform required number of swaps
    for count in range(number_of_swaps):
        # Find the index of the second Joker in the deck of cards(list)
        index_of_joker2 = deck_of_cards.index(JOKER2)
        # Preform swap with the second Joker and the next card following it
        swap_cards(deck_of_cards, index_of_joker2)


def triple_cut(deck_of_cards):
    """
    (list of int) -> NoneType
    Given a deck of cards, which are a list of integers, preforms a triple cut
    by locating the position of the first Joker in the deck(list) and the
    position of the second Joker in the deck(list), and swaps the
    cards above the first Joker with the cards below the second Joker.
    REQ: the given deck of card must have at least two jokers with valuse of 27
    and 28
    >>> deck = [1, 28, 2, 3, 27, 4, 5]
    >>> triple_cut(deck)
    >>> deck == [4, 5, 28, 2, 3, 27, 1]
    True
    >>> deck = [28, 1, 2, 27, 3, 4, 5]
    >>> triple_cut(deck)
    >>> deck == [3, 4, 5, 28, 1, 2, 27]
    True
    >>> deck = [1, 2, 27, 3, 4, 5, 28]
    >>> triple_cut(deck)
    >>> deck == [27, 3, 4, 5, 28, 1, 2]
    True
    >>> deck = [27, 1, 2, 3, 4, 5, 28]
    >>> triple_cut(deck)
    >>> deck == [27, 1, 2, 3, 4, 5, 28]
    True
    >>> deck = [1, 2, 3, 28, 27, 4, 5]
    >>> triple_cut(deck)
    >>> deck == [4, 5, 28, 27, 1, 2, 3]
    True
    >>> deck = [1, 2, 3, 4, 5, 28, 27]
    >>> triple_cut(deck)
    >>> deck == [28, 27, 1, 2, 3, 4, 5]
    True
    """
    # Find the position of JOKER1
    position_of_joker1 = deck_of_cards.index(JOKER1)
    # Find the position of JOKER2
    position_of_joker2 = deck_of_cards.index(JOKER2)
    # Determine which of the two Jokers come first the first Joker
    is_joker1_first = position_of_joker1 < position_of_joker2
    # Determine the position of the first Joker and the second Joker
    if(is_joker1_first):
        first_joker_position = position_of_joker1
        second_joker_position = position_of_joker2 + 1
    else:
        first_joker_position = position_of_joker2
        second_joker_position = position_of_joker1 + 1
    # Create a list for the cards above the first Joker
    above_first_joker = deck_of_cards[:first_joker_position]
    # Create a list for the cards between the first and second Joker
    between_jokers = deck_of_cards[first_joker_position:second_joker_position]
    # Create a list for the crards below the second Joker
    below_second_joker = deck_of_cards[second_joker_position:]

    # Preform the triple cut
    deck_of_cards[:] = (below_second_joker + between_jokers +
                        above_first_joker)


def insert_top_to_bottom(deck_of_cards):
    """
    (list of int) -> NoneType
    Given a deck of cards, get's the value of te bottom card and moves that
    many cards from the rop of the deck to the bottom, position them just above
    the original botoom card of the deck. Note, if the bottom card has the
    value of JOKER2, then the value of JOKER1 would be used to preform the
    swap.
    REQ: the largest card in the given deck must be equal to or less than the
    total nunmber of cards in the deck (length of the list)
    REQ: the smallest card in the given deck must be equal to or greater than
    zero
    >>> deck = [1, 2, 3, 4, 5]
    >>> insert_top_to_bottom(deck)
    >>> deck == [1, 2, 3, 4, 5]
    True
    >>> deck = [3, 1, 4, 5, 2]
    >>> insert_top_to_bottom(deck)
    >>> deck == [4, 5, 3, 1, 2]
    True
    >>> deck = [3, 1, 2, 5, 4, 0]
    >>> insert_top_to_bottom(deck)
    >>> deck == [3, 1, 2, 5, 4, 0]
    True
    >>> deck = [5, 4, 2, 1, 3]
    >>> insert_top_to_bottom(deck)
    >>> deck == [1, 5, 4, 2, 3]
    True
    """
    # Determine of the last card(element) is the highest value in the deck
    is_max_value = (deck_of_cards[-1] == max(deck_of_cards))
    # Check is the last card(element) is the highest value in the deck(list)
    if(is_max_value):
        # Store the value of the one less the last card in the deck(list)
        last_card_value = deck_of_cards[-1] - 1
    else:
        # Store the value of the last card(element) in the deck(list)
        last_card_value = deck_of_cards[-1]
    # Get the posisiton of the second last card
    index_before_last_card = len(deck_of_cards) - 1
    # Get the cards at the beginning of the deck need to be moved
    cards_to_move = deck_of_cards[:last_card_value]
    # Get the cards between the last card of the part of the deck to be moved
    # and the last card in the deck
    cards_between = deck_of_cards[last_card_value: index_before_last_card]
    # Insert the cards (elements) form the first part of the deck just before
    # the last card(element)
    deck_of_cards[:-1] = cards_between + cards_to_move


def get_card_at_top_index(deck_of_cards):
    """
    (list of int) -> int
    Given a deck of cards =, will look a the card(element) at the top of the
    deck(the first element in the list), and using the value of that card
    (element) returns the card(element) in that deck(list) at that index.
    Note, if the card at the top of the deck(first element in the list) is the
    JOKER2(largest card in the deck) then uses JOKER1(the second largest value
    in the deck, which has a value one lower than JOKER2), and finds the card
    in that deck at that index.
    REQ: The largest card (element) in the deck(list) should be equal to or
    less than the length of the deck(list of int).
    REQ: The smallest card(element) in the deck(list) should be equal to or
    greater than zero.
    >>> deck = [1, 2, 3, 4, 5]
    >>> get_card_at_top_index(deck)
    2
    >>> deck = [0, 1, 2, 3, 4, 5]
    >>> get_card_at_top_index(deck)
    0
    >>> deck = [3, 2, 4, 1, 5, 0]
    >>> get_card_at_top_index(deck)
    1
    >>> deck = [3, 2, 3, 4, 2, 5]
    >>> get_card_at_top_index(deck)
    4
    """
    # Determine if the zeroth elemnet in
    value_of_first_card = deck_of_cards[0]
    # Check if the top card is the largest value in the deck
    if(deck_of_cards[0] == max(deck_of_cards)):
        # Store the value of one less than the largest value, which is the
        # frist card in the deck
        value_of_first_card = deck_of_cards[0] - 1
    else:
        # Store the value of the the card(element) of the zeroth element in the
        # list
        value_of_first_card = deck_of_cards[0]

    # Get the card(element) at the index value which is the first/top
    # card(element) in the deck(list)
    card_at_index = deck_of_cards[value_of_first_card]
    # Return the element at the at the index value of the first element
    return card_at_index


def get_next_value(deck_of_cards):
    """
    (list of int) -> int
    Given a deck of cards (list of int), will preform Bruce Schneier's
    encryption algorithm, and returns a potential keystream value.
    REQ: the given deck of card must not be empty and should  have at least two
    jokers with valuse of 27
    and 28.
    REQ: The largest card (element) in the deck(list) should be equal to or
    less than the length of the deck(list of int).
    REQ: The smallest card(element) in the deck(list) should be equal to or
    greater than zero.
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,\
    13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> get_next_value(deck)
    28
    >>> deck = [22, 23, 24, 25, 26, 27, 28, 1, 2, 3, 4,\
    5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    >>> get_next_value(deck)
    23
    >>> deck = [9, 3, 1, 6, 12, 28, 21, 10, 14, 2, 18, 25, 27,\
    4, 24, 7, 20, 11, 22, 19, 26, 15, 16, 17, 8, 23, 13, 5]
    >>> get_next_value(deck)
    25
    >>> deck = [9, 3, 1, 6, 12, 21, 28, 10, 14, 2, 18, 25, 27,\
    4, 24, 7, 20, 11, 22, 19, 26, 15, 16, 17, 8, 23, 13, 5]
    >>> get_next_value(deck)
    14
    """
    # Find JOKER1 and swap it with the card that follows it, treating the deck
    # circularly. (Step 1 of algorithm)
    move_joker_1(deck_of_cards)
    # Step 2 of algorithm
    # Find JOKER2 and move it two cards down, treating the deck circularly.
    move_joker_2(deck_of_cards)
    # Step 3 of algorithm
    # Find the two jokers (the two largest cards) and preform a triple cut with
    # deck(list)
    triple_cut(deck_of_cards)
    # Step 4 of algorithm
    # Move the value of the last elemnet in the list number of cards from the
    # top of the deck to just before the last element of the deck
    insert_top_to_bottom(deck_of_cards)
    # Get potential keystream
    potential_keystream = get_card_at_top_index(deck_of_cards)
    # Return the postential keystream
    return potential_keystream


def get_next_keystream_value(deck_of_cards):
    """"
    (list of int) -> int
    Given a deck of cards, will repreat Bruce Schneier's algorithm to get a
    valid potential keystream is produced, which is not JOKER1 or JOKER2
    (the two highest cards in the deck- list of int)
    REQ: the given deck of card must not be empty and should  have at least two
    jokers with valuse of 27 and 28.
    REQ: The largest card (element) in the deck(list) should be equal to or
    less than the length of the deck(list of int).
    REQ: The smallest card(element) in the deck(list) should be equal to or
    greater than zero.
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,\
    13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> get_next_keystream_value(deck)
    8
    >>> deck = [10, 14, 2, 18, 25, 27, 9, 3, 1, 6, 12, 21, 28,\
    19, 26, 15, 16, 17, 4, 24, 7, 20, 11, 22, 8, 23, 13, 5]
    >>> get_next_keystream_value(deck)
    12
    >>> deck = [10, 14, 2, 18, 25, 9, 3, 1, 6, 12, 21, 28, 19,\
    20, 11, 22, 8, 23, 13, 5, 26, 15, 16, 17, 4, 24, 7, 27]
    >>> get_next_keystream_value(deck)
    24
    """
    # Set the check if the potential keystrem is not valid to true
    is_not_valid_keystream = True
    # Get a valid potential key stream, which is between 0 and 27, excluding 0
    # and 27
    while(is_not_valid_keystream):
        # Get a potential keystream value
        potential_keystream = get_next_value(deck_of_cards)
        # Check if the potential keystream value is not valid
        is_not_valid_keystream = not (1 <= potential_keystream <= 26)

    # return the potential keystream value
    return potential_keystream


def process_message(deck_of_cards, message, mode):
    """
    (list of int, str, str) -> str
    Given a deck of cards, a message to be either encrypted or decrypted, and
    the mode that indicates whether to encrypt or decrypt, which is either
    'e' (to encrypt) or 'd' (to decrypt), executes the required algorithm
    and returns the encrypted or decrypted message depending on the given
    mode.
    REQ: the given deck of card must not be empty and should  have at least two
    jokers with valuse of 27
    and 28.
    REQ: The largest card (element) in the deck(list) should be equal to or
    less than the length of the deck(list of int).
    REQ: The smallest card(element) in the deck(list) should be equal to or
    greater than zero.
    REQ: message must not be empty(len(message > 0))
    REQ: mode must either be 'e' or 'd'
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,\
    13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> process_message(deck, "HELLO", 'e')
    'PUWTU'
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,\
    13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> process_message(deck, "Goo3d By3E!!@** ", 'e')
    'OEZLHXJ'
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,\
    13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> process_message(deck, "XULKK", 'd')
    'PEACE'
    """
    # Get the cleanned message
    cleanned_message = clean_message(message)
    # Create a place to store the preformed upon message
    preformed_upon_message = ''
    # Create a place to sotre the keystreams needed
    keystreams = []

    # Get a list of keystream keys
    for index in range(len(cleanned_message)):
        # Generate each keystream
        keystreams.append(get_next_keystream_value(deck_of_cards))

    # Determine the mode, which is either 'e' or 'd'
    is_encrypt_mode = (mode == 'e')
    # Check the mode, whih is either encrypt or decrypt
    if(is_encrypt_mode):
        # Loop through each letter of the message
        for index in range(len(cleanned_message)):
            # Encrypt each letter from the message and store
            preformed_upon_message += encrypt_letter(cleanned_message[index],
                                                     keystreams[index])
    else:
        # Loop through each letter of the message
        for index in range(len(cleanned_message)):
                # Decrypt each letter from the message and store
                preformed_upon_message += decrypt_letter(message[index],
                                                         keystreams[index])
    # Return the result of the preformed upon message
    return preformed_upon_message


def process_messages(deck_of_cards, messages, mode):
    """
    (list of int,  list of str, str) -> list of str
    Given a deck of cards, a list of messages to be either encrypted or
    decrypted, and the mode that indicates whether to encrypt or decrypt, which
    is either 'e' (to encrypt) or 'd' (to decrypt), executes the required
    algorithm and returns a list encrypted or decrypted messages depending on
    the given mode.
    REQ: the given deck of card must not be empty and should  have at least two
    jokers with valuse of 27
    and 28.
    REQ: The largest card (element) in the deck(list) should be equal to or
    less than the length of the deck(list of int).
    REQ: The smallest card(element) in the deck(list) should be equal to or
    greater than zero.
    REQ: the lsit of messages must not be empty
    REQ: mode must either be 'e' or 'd'
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,\
    13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> messages = ['hey', 'Yo!!', 'Su399p']
    >>> process_messages(deck, messages, 'e')
    ['PUJ', 'GU', 'RZQ']
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,\
    13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> messages = ['JOP', 'IAQJWIPH', 'XEDIJ']
    >>> process_messages(deck, messages, 'd')
    ['BYE', 'AUREVOIR', 'PEACE']
    """
    # Create a place to sotre the preformed up messges
    preformed_upon_messages = []
    # Loop through each message in the given list of messages
    for message in messages:
        # Get each of the processed messages
        preformed_upon_messages.append(process_message(deck_of_cards, message,
                                                       mode))
    # Returned the preformed upon list of messages
    return preformed_upon_messages


def read_messages(file_handle):
    """
    (file open for reading) -> str
    Given an open file for reading, which contains one meassage per line, will
    read each line and return each line(message) as a list of messages.
    REQ: the given file handle must be open for reading only
    REQ: the given file must not be empty
    """
    # Create a list to store the each message(line) from the file
    messages = []
    # Loop through each line of the file
    for next_line in file_handle:
        # Strip the current line being read of tralling space and newline
        next_line = next_line.rstrip('\n')
        # Check if the next line is empty
        if(not(next_line == '')):
            # Store the line from the file in a list of messages
            messages.append(next_line)
    # Close the file
    file_handle.close()
    # Return all the messages form the file
    return messages


def read_deck(file_handle):
    """
    (file open for reeding) -> list of int
    Given an open file for reading, which contains various number of integer
    per line, will read each line and return a list of integers, where each
    element of the list contains one integer from the file in the order of
    wich the file is read.
    REQ: the given file handle must be open for reading only
    REQ: the given file must not be empty
    REQ: the integers in the file must be seperated by a single space only
    REQ: the file should only contain spaces and integers
    """
    # Create a list to store the each card in the deck when it's a str
    deck_of_cards_str = []
    # Create a list to store the convert str to int list
    deck_of_cards = []
    # Loop through each line of the file
    for next_line in file_handle:
        # Strip the current line being read of tralling space and newline
        next_line = next_line.rstrip('\n')
        next_line = next_line.rstrip()
        # Check if the next line is empty
        if(not(next_line == '')):
            # Store the integer from the file in a list of cards
            deck_of_cards_str[:] += next_line.split(' ')
    # Convert the list of str to a list of int
    for element in deck_of_cards_str:
        # Convert str element to int element
        deck_of_cards.append(int(element))
    # Return the list of integers from the file
    return deck_of_cards
