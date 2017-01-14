"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message-decrypted.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt. Print the decrypted message to the screen.
    """

    # Get the open file handle for the deck file
    deck_file_handle = open(DECK_FILENAME, 'r')
    # Get the open file handle for the message file
    msg_file_handle = open(MSG_FILENAME, 'r')

    # Get the list of integers, which is the deck of cards, form the deck file
    deck_of_cards = cipher_functions.read_deck(deck_file_handle)
    # Get th list of messages form the message, from the message file
    messages = cipher_functions.read_messages(msg_file_handle)

    # Process the gevin messages using the given deck and mood
    processed_messages = cipher_functions.process_messages(deck_of_cards,
                                                           messages, MODE)
    # Output the processed_messages
    for message in processed_messages:
        print(message)

main()

